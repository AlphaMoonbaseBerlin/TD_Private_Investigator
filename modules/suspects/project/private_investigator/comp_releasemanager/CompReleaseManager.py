'''Info Header Start
Name : CompReleaseManager
Author : Admin@DESKTOP-RTI312L
Version : 0
Build : 2
Savetimestamp : 2022-12-21T19:15:39.997695
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

	def Release(self, target_component ):
		release_candidate = op("/sys/quiet").copy( target_component )
		for child in release_candidate.findChildren( type = DAT):
			if hasattr( child.par, "file"):
				child.par.file = ""

		for child in release_candidate.findChildren( type = COMP):
			if hasattr( child.par, "externaltox"):
				child.par.externaltox = ""

		release_candidate.par.externaltox = ""
		release_candidate.save( os.path.join( self.ownerComp.par.Folder.eval(), target_component.name) + ".tox", createFolders = True)
		release_candidate.destroy()
