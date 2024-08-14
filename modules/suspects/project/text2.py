'''Info Header Start
Name : text2
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.32660
Info Header End'''
op("td_pip").Import_Module("mypy")
import mypy.stubgen
mypy.stubgen.main(['modules/suspects/project/private_investigator/PrivateInvestigator.py'])