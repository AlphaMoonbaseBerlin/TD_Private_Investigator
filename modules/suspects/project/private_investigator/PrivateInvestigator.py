'''Info Header Start
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.28040
Info Header End'''


class PrivateInvestigator:
	"""
	PrivateInvestigator description
	"""
	def __init__(self, ownerComp):
		# The component to which this extension is attached
		self.ownerComp = ownerComp
	
	def possible_suspects(self, op_type):
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
		return False
		for item in self.ownerComp.op("state").col("dirty")[1:]:
			if int(item): return True
		return False

	def Add(self, operator):
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

	def Save(self, operator):
		if isinstance(operator, COMP)	: 
			operator.par.Vcoriginal.val = False
			self.ownerComp.op("comp_versionmanager").Update( operator )
			self.ownerComp.op("comp_externalizer").Save( operator )
			operator.par.Vcoriginal.val = True

		self.Update()
		pass

	def Release(self, operator):
		if not isinstance(operator, COMP)	: 	return
		if self.Get_Dirt( operator )		:	self.ownerComp.op("comp_externalizer").Save( operator )
		self.ownerComp.op("comp_releasemanager").Release( operator )
		pass

	def Get_Dirt(self, operator):
		if isinstance(operator, textDAT): return self.ownerComp.op("dat_dirtwatcher").Snoop( operator )
		if isinstance(operator, COMP)	: return operator.dirty
		return False

	def Get_Info(self, operator):
		if isinstance(operator, textDAT): return self.ownerComp.op("dat_versionmanager").Get_Info_Dict( operator )
		if isinstance(operator, COMP)	: return self.ownerComp.op("comp_versionmanager").Get_Info_Dict( operator )

	def Edit(self, operator):
		if isinstance(operator, textDAT): 
			operator.par.edit.pulse()

		if isinstance(operator, COMP)	: 
			ui.panes.createFloating().owner = operator
		return

	def View(self, operator):
		ui.panes.createFloating().owner = operator.parent()

	def Reload(self, operator):
		if isinstance(operator, textDAT): 
			self.ownerComp.op("dat_externalizer").Reload( operator )

		if isinstance(operator, COMP)	: 
			self.ownerComp.op("comp_externalizer").Reload( operator )

		self.Update()