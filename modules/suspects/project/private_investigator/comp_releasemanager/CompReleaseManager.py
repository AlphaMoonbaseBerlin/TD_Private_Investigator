


'''Info Header Start
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.28040
Info Header End'''
import os
class CompReleaseManager:
	"""
	CompReleaseManager description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

	def prepare(self, target):
		if self.ownerComp.par.Tag.eval() in target.tags:
			if hasattr( target.par, "externaltox"):
				target.par.externaltox = ""
			if hasattr( target.par, "file"):
				target.par.file = ""
			target.tags.remove( self.ownerComp.par.Tag.eval() )

	def Release(self, target_component ):
		release_candidate = op("/sys/quiet").copy( target_component )
		
		for child in release_candidate.findChildren( type = DAT):
			self.prepare(child)
		for child in release_candidate.findChildren( type = COMP):
			self.prepare( child )

		self.prepare( release_candidate )

		prerelease_script= release_candidate.op("pre_release")
		if isinstance( prerelease_script, textDAT): prerelease_script.run()
		
		release_candidate.save( os.path.join( self.ownerComp.par.Folder.eval(), target_component.name) + ".tox", createFolders = True)
		release_candidate.destroy()
