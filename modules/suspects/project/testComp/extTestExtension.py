'''Info Header Start
Name : extTestExtension
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.32660
Info Header End'''


class extTestExtension:
	"""
	extTestExtension description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp:COMP = ownerComp

		# properties
		

		# attributes:
		self.a = 0 # attribute
		self.B = 1 # promoted attribute

		# stored items (persistent across saves and re-initialization):
		storedItems = [
			# Only 'name' is required...
			{'name': 'StoredProperty', 'default': None, 'readOnly': False,
			 						'property': True, 'dependable': True},
		]
		# Uncomment the line below to store StoredProperty. To clear stored
		# 	items, use the Storage section of the Component Editor
		
		# self.stored = StorageManager(self, ownerComp, storedItems)

	def myFunction(self, v):
		foobar = op("foobar")
		debug("Ketzt geht nix")
		debug(v)

	def PromotedFunction(self, v):
		debug(v)