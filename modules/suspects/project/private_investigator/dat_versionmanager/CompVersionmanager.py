


'''Info Header Start
Name : CompVersionmanager
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.28040
Info Header End'''
import TDFunctions
import os, datetime, re
class CompVersionmanager:
	"""
	CompVersionmanager description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		self.comment_seperator = " : "
		self.comment_definition = { 
			row[0].val : 
			{ 	"start" : row[1].val, 
				"end" : row[2].val, 
				"comment" : row[3].val,
				"ending" : row[4].val } 
			for row in self.ownerComp.op("comment_definition").rows() }


	def Init(self, target_operator):
		language 			= target_operator.par.extension.eval()
		if language == "languageext" : 
			target_operator.par.extension = self.ownerComp.par.Defaultdatextension.eval()
			language = target_operator.par.extension.eval()
		target_operator.text = "\n" + target_operator.text
		text 				= target_operator.text
		comment_definition 	= self.comment_definition.get(language, self.comment_definition["default"] )
		comment 			= self.find_comment( text, comment_definition)
		if not comment:
			initital_comment = self.update_comment({
				"Name" : target_operator.name,
				"Author" : "",
				"Saveorigin" : "",
				"Saveversion" : ""
			})
			self.update_comment( initital_comment )
			self.write_comment( target_operator, initital_comment)
		self.Update( target_operator )

	def parse_comment(self, text):
		comment_dict = {}
		for line in text.split("\n"):
			if not line: continue
			key, value = line.split( self.comment_seperator )
			comment_dict[key] = value
		return comment_dict

	def get_op_commentdefinition(self, target_operator):
		language 			= target_operator.par.extension.eval()
		comment_definition 	= self.comment_definition.get(language, self.comment_definition["default"] )
		return comment_definition

	def Get_Info_Dict(self, target_operator):
		text 				= target_operator.text
		comment 			= self.find_comment( text, self.get_op_commentdefinition(target_operator))
		if not comment: return {}
		parsed_comment = self.parse_comment( comment.group(1) )
		return parsed_comment

	def Update(self, target_operator):
		parsed_comment 	= self.Get_Info_Dict( target_operator )
		updated_comment = self.update_comment( parsed_comment )

		target_operator.text = self.replace_comment(
			self.compose_comment(target_operator, updated_comment),
			target_operator.text,
			self.get_op_commentdefinition( target_operator )
		)
		#self.write_comment( target_operator, updated_comment)

	def compose_comment(self, target_operator, comment:dict):
		definition = self.get_op_commentdefinition(target_operator)
		formatted_comment = definition["start"]
		for key, value in comment.items():
			formatted_comment += f"\n{key}{self.comment_seperator}{value}"
		formatted_comment += f"\n{definition['end']}"
		return formatted_comment

	def write_comment(self, target_operator,  comment:dict):
		target_operator.text = self.compose_comment(target_operator, comment) + target_operator.text

	def update_comment(self, comment:dict):
		userdomain = ("@" + os.environ.get("userdomain", "") ).removesuffix("@")
		comment["Author"] 			=  os.getlogin() + userdomain
		comment["Build"]			= int(comment.get("Build", 0)) + 1
		comment["Saveorigin"]		= project.name
		comment["Saveversion"]		= var("CUR_TOUCHBUILD")
			#"Version" : 0,
			#"Build" : 0,
			#"Savetimestamp" : 0,
		comment.pop("Version", None)
		comment.pop("Build", None)
		comment.pop("Savetimestamp", None)
		return comment

	def find_comment(self, text, definition):
		return re.search( f"{definition['start']}((.|\n)*){definition['end']}", text)

	def replace_comment(self, new_comment, text, definition):
		return re.sub( f"{definition['start']}((.|\n)*){definition['end']}", new_comment, text)