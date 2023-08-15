'''Info Header Start
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.28040
Info Header End'''
import hashlib

class DatDirtWatcher:
	"""
	DatDirtWatcher description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp

	def Snoop(self, target_operator):
		return False
		old_texthash = target_operator.fetch("texthash", "")
		texthash = hashlib.md5(target_operator.text.encode()).hexdigest()
		return texthash != old_texthash

	def Clean(self, target_operator):
		texthash = hashlib.md5(target_operator.text.encode()).hexdigest()
		target_operator.store( "texthash", texthash )