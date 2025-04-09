
'''Info Header Start
Author : Wieland PlusPlusOne@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2023.12000
Info Header End'''
import os
from typing import Union
Suspect = Union[textDAT, COMP]
import functools, pathlib
import naiveStubser

class CompReleaseManager:
	"""
	CompReleaseManager description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
		
	def createStubs(self, target:textDAT, meta:dict):
		if not self.ownerComp.par.Generatestubs.eval(): return
		try:
			sourcePath = pathlib.Path( target.par.file.eval() )
			outputPath = pathlib.Path( 
				self.ownerComp.par.Folder.eval(), 
				f'{meta["compName"]}_stubs', 
				sourcePath.with_suffix(".pyi").name )
			outputPath.parent.mkdir(parents=True, exist_ok=True)
			outputPath.touch(exist_ok=True)
			outputPath.write_text( naiveStubser.stubify(target.text))
		except Exception as e:
			debug("Exception while creating Stubs", e)
		return

	def prepare(self, target:Suspect, meta:dict):
		if self.ownerComp.par.Tag.eval() in target.tags:
			if hasattr( target.par, "externaltox"):
				target.par.externaltox = ""
			if hasattr( target.par, "file"):
				self.createStubs( target, meta)
				target.par.file = ""
			if isinstance( target, COMP):
				self.run_prerelease( target )
			target.tags.remove( self.ownerComp.par.Tag.eval() )

	def run_prerelease(self, target:COMP):
		prerelease_script = target.op("pre_release") or self.ownerComp.op("empty_prerelease")
		try:
			prerelease_script.run()
		except Exception as e:
			debug( f"Failed to run prereleasescript of {target}. Reason\n{e}")

	def Release(self, target_component:COMP ):
		for child in op( "/sys/quiet" ).findChildren( depth=1):
			child.destroy()

		release_candidate:COMP = op( "/sys/quiet" ).copy( target_component )
		meta = {
			"compName" : release_candidate.name
		}
		op( "/sys/quiet" ).allowCooking = self.ownerComp.par.Releasemode.eval() == "loud"
		for child in release_candidate.findChildren( type = DAT):
			self.prepare(child, meta)
		for child in release_candidate.findChildren( type = COMP):
			self.prepare( child, meta )

		self.prepare( release_candidate, meta )
		self.run_prerelease( release_candidate )
		
		
		release_candidate.save( os.path.join( self.ownerComp.par.Folder.eval(), target_component.name) + ".tox", createFolders = True)
		
		release_candidate.destroy()
		op( "/sys/quiet" ).allowCooking = False