'''Info Header Start
Author : Wieland PlusPlusOne@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2023.12000
Info Header End'''

from typing import Union, List
import os 

Suspect = Union[DAT,COMP]

class PrivateInvestigator:
	"""
	PrivateInvestigator description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp:COMP = ownerComp
	
	@property
	def PrefabAuthor(self):
		userdomain = ("@" + os.environ.get("userdomain", "") ).removesuffix("@")
		return os.getlogin() + userdomain

	@property
	def Author(self):
		return self.ownerComp.par.Username.eval()

	def possible_suspects(self, op_type:str):
		return self.ownerComp.par.Root.eval().findChildren(type = op_type, tags = [self.ownerComp.par.Tag.eval()])
	
	def ReinitSuspects(self):
		for suspect in self.possible_suspects(textDAT) + self.possible_suspects(COMP) :
			self.Add( suspect )

	def Scan(self):
		self.ownerComp.op("suspects").clear( keepFirstRow = True )
		for child in self.possible_suspects( COMP ):
			if not getattr( child.par, "Vcoriginal", None): continue
			self.ownerComp.op("suspects").appendRow( child.path )
		for child in self.possible_suspects( textDAT ):
			self.ownerComp.op("suspects").appendRow( child.path )
		self.Update()
		pass

	def Update(self):
		#self.ownerComp.op("state").cook( force = True )
		self.ownerComp.op("state").lock = False
		self.ownerComp.op("state").lock = True
		#update the dirty-state
		pass

	@property
	def State(self):
		for cell in self.ownerComp.op("state").col("Dirty")[1:]:
			if cell.val == "True": return True
		return False

	def Add(self, operator:Suspect):
		valid = False
		if isinstance(operator, textDAT): 
			valid = True
			self.ownerComp.op("dat_versionmanager").Init( operator )
			self.ownerComp.op("dat_externalizer").Init( operator )
			self.ownerComp.op("dat_dirtwatcher").Clean( operator )

		if isinstance(operator, COMP)	: 
			valid = True
			self.ownerComp.op("comp_versionmanager").Init( operator )
			self.ownerComp.op("comp_externalizer").Init( operator )
		
		if not valid: return
		operator.tags.add( self.ownerComp.par.Tag.eval() )
		self.ownerComp.op("suspects").appendRow( operator.path )
		self.Update()
		pass


	@property
	def Suspects(self):
		return [
			op( row[0].val ) for row in self.ownerComp.op("state").rows()[1:]
		]
	@property
	def DirtySuspects(self):
		return [
			op( row[0].val ) for row in self.ownerComp.op("state").rows()[1:] if row[8].val == "True"
		]
	
	
	
	def SaveAllDirty(self):
		"""
			Saves all components that are marked as dirty.
		"""
		self.SaveItems( self.DirtySuspects )

	
	def ResaveAll(self):
		"""
			Force all Components to be resaved, even if they might not be marked as dirty.
		"""
		self.SaveItems( self.Suspects )
	
	def ReleaseAll(self):
		for suspect in self.Suspects:
			self.Release(suspect)

	def SaveItems(self, items:List[COMP]):
		"""
			Save a list of given operators.
		"""
		for item in items:
			self.Save( item )
	
	def Save(self, operator:COMP):
		"""
			Save the given operator.
		"""
		if isinstance(operator, COMP)	: 
			operatorACLGroup = self.ownerComp.op("comp_versionmanager").GetGroup( operator )
			
			if self.ownerComp.par.Useac.eval() and operatorACLGroup:
				#Fetch all groups that match the Operator ACL Group. Wildcards supported.
				
				groupKeys = tdu.match(
					operatorACLGroup, list( self.ownerComp.op("ACL").Data.Groups.keys() )
				)
				isAllowed = False
				
				for groupKey in groupKeys:
					groupList = [ item.Value for item in self.ownerComp.op("ACL").Data.Groups.get( groupKey, []) ]
					for member in groupList:
						isAllowed = bool( tdu.match( member, [self.Author]) )
						if isAllowed: break
					if isAllowed: break
				else:
					ui.messageBox(
						"No Access", 
						f"You are not part of the group {operatorACLGroup}. Please update ACL or Cancel the Operation.", 
						buttons=["OK"] )
					return False
							
			operator.par.Vcoriginal.val = False
			self.ownerComp.op("comp_versionmanager").Update( operator )
			self.ownerComp.op("comp_externalizer").Save( operator )
			operator.par.Vcoriginal.val = True
		elif isinstance( operator, textDAT):
			self.ownerComp.op("dat_versionmanager").Update( operator )
			self.ownerComp.op("dat_externalizer").Save( operator )
		self.Update()
		pass

	def Release(self, operator:COMP):
		if not isinstance(operator, COMP)	: 	return
		if self.Get_Dirt( operator )		:	self.ownerComp.op("comp_externalizer").Save( operator )
		self.ownerComp.op("comp_releasemanager").Release( operator )
		pass

	def Get_Dirt(self, operator:Suspect):
		if isinstance(operator, textDAT): return self.ownerComp.op("dat_dirtwatcher").Snoop( operator )
		if isinstance(operator, COMP)	: return operator.dirty
		return False

	def Get_Info(self, operator:Suspect):
		if isinstance(operator, textDAT): return self.ownerComp.op("dat_versionmanager").Get_Info_Dict( operator )
		if isinstance(operator, COMP)	: return self.ownerComp.op("comp_versionmanager").Get_Info_Dict( operator )

	def Edit(self, operator:Suspect):
		if isinstance(operator, textDAT): 
			operator.par.edit.pulse()

		if isinstance(operator, COMP)	: 
			ui.panes.createFloating().owner = operator
		return

	def View(self, operator:Suspect):
		ui.panes.createFloating().owner = operator.parent()

	def Reload(self, operator:Suspect):
		if isinstance(operator, textDAT): 
			self.ownerComp.op("dat_externalizer").Reload( operator )

		if isinstance(operator, COMP)	: 
			self.ownerComp.op("comp_externalizer").Reload( operator )

		self.Update()