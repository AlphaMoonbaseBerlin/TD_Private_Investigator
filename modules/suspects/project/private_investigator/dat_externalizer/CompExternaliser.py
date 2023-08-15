'''Info Header Start
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.28040
Info Header End'''
import os

def pathjoin(*args):
	return "/".join( [ arg.strip("/\\") for arg in args])

class CompExternaliser:
	"""
	CompExternaliser description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

	def Init(self, target_operator):
		joined_savepath =  pathjoin( self.ownerComp.par.Folder.eval(), target_operator.path ) + "." + target_operator.par.extension.eval()
		savepath = target_operator.save( joined_savepath , createFolders = True)
		target_operator.par.file.val		= savepath
		target_operator.par.loadonstart.val = True
		target_operator.par.syncfile.val 	= True

	def Save(self, target_operator):
		if target_operator.par.file.eval():
			target_operator.save(target_operator.par.file.eval())
		else:
			self.Init( target_operator )
			
			
	def Reload(self, target_operator):
		target_operator.par.loadonstartpulse.pulse()