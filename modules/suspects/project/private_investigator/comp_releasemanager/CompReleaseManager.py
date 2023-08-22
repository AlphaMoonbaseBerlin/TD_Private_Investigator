
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
			if isinstance( target, COMP):
				self.run_prerelease( target )
			target.tags.remove( self.ownerComp.par.Tag.eval() )

	def run_prerelease(self, target):
		prerelease_script = target.op("pre_release") or self.ownerComp.op("empty_prerelease")
		try:
			prerelease_script.run()
		except Exception as e:
			debug( f"Failed to run prereleasescript of {target}. Reason\n{e}")

	def Release(self, target_component ):
		release_candidate = op( "/sys/quiet" ).copy( target_component )
		
		op( "/sys/quiet" ).allowCooking = self.ownerComp.par.Releasemode.eval() == "loud"
		for child in release_candidate.findChildren( type = DAT):
			self.prepare(child)
		for child in release_candidate.findChildren( type = COMP):
			self.prepare( child )

		self.prepare( release_candidate )
		self.run_prerelease( release_candidate )
		
		
		release_candidate.save( os.path.join( self.ownerComp.par.Folder.eval(), target_component.name) + ".tox", createFolders = True)
		release_candidate.destroy()
		op( "/sys/quiet" ).allowCooking = False