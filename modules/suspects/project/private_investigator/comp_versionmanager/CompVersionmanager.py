'''Info Header Start
Name : CompVersionmanager
Author : Wieland@AMB-ZEPH15
Version : 0
Build : 5
Savetimestamp : 2023-04-02T21:06:37.533232
Saveorigin : Project.toe
Saveversion : 2022.28040
Info Header End'''
import TDFunctions
import os, datetime
class CompVersionmanager:
	"""
	CompVersionmanager description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

	def Init(self, target_operator):
		vc_table = target_operator.op("vc_data") or target_operator.copy( self.ownerComp.op("parameter_template/vc_data") )
		vc_table.expose = False

		page_name = "Version Ctrl"

		target_page = TDFunctions.getCustomPage( target_operator, page_name ) or target_operator.appendCustomPage(page_name)
		source_page = TDFunctions.getCustomPage( self.ownerComp.op("parameter_template"), page_name)
		for source_parameter in source_page.pars:
			try:
				new_parameter = target_page.appendPar( source_parameter.name, par=source_parameter, replace = False )
				new_parameter.copy( source_parameter )
			except tdError as e:
				pass
		target_operator.par.Vcoriginal = True
		self.Update( target_operator )

	def Update(self, target_operator):
		target_operator.par.Vcname = target_operator.name
		userdomain = ("@" + os.environ.get("userdomain", "") ).removesuffix("@")
		target_operator.par.Vcauthor = self.ownerComp.par.Username.eval()  or (os.getlogin() + userdomain)
		target_operator.par.Vcbuild.val = target_operator.par.Vcbuild.eval() + 1
		target_operator.par.Vcsavetimestamp = datetime.datetime.now().isoformat()
		target_operator.par.Vcsaveorigin = project.name
		target_operator.par.Vcsaveversion.val = project.saveBuild
		pass
	
	def Get_Info_Dict(self, target_operator):
		return {
			"Name"	 : target_operator.par.Vcname.eval(),
			"Author" : target_operator.par.Vcauthor.eval(),
			"Version"	 : target_operator.par.Vcversion.eval(),
			"Build"	 : target_operator.par.Vcbuild.eval(),
			"Savetimestamp" : target_operator.par.Vcsavetimestamp.eval(),
			"Saveorigin"	: target_operator.par.Vcsaveorigin.eval(),
			"Saveversion"	: target_operator.par.Vcsaveversion.eval(),
		}
		