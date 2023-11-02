"""Info Header Start
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.32660
Info Header End"""
from typing import Union
Suspect = Union[DAT, COMP]

class PrivateInvestigator:
    """
	PrivateInvestigator description
	"""

    def __init__(self, ownerComp):
        pass

    def possible_suspects(self, op_type: str):
        pass

    def ReinitSuspects(self):
        pass

    def Scan(self):
        pass

    def Update(self):
        pass

    @property
    def State(self):
        pass

    def Add(self, operator: Suspect):
        pass

    def Save(self, operator: COMP):
        pass

    def Release(self, operator: COMP):
        pass

    def Get_Dirt(self, operator: Suspect):
        pass

    def Get_Info(self, operator: Suspect):
        pass

    def Edit(self, operator: Suspect):
        pass

    def View(self, operator: Suspect):
        pass

    def Reload(self, operator: Suspect):
        pass