# -*- coding: utf-8 -*-
__version__ = "0.1dev0"
import thaianalysisrule
import os

templates_dir = os.path.join(os.path.dirname(thaianalysisrule.__file__), 'corpus')

def readfile_dict(filename:str) -> str:
    _path = os.path.join(templates_dir, filename)
    with open(_path, "r", encoding="utf-8-sig") as f:
        _data = ["'"+i.strip()+"'" for i in f.readlines()]
    return " | ".join(_data)

VERE_dict = readfile_dict("VERB.txt")
ADV_dict = readfile_dict("ADV.txt")
PREP_dict = readfile_dict("PREP.txt")
DET_dict = readfile_dict("DET.txt")
CLAS_dict = readfile_dict("CLAS.txt")
NUM_dict = readfile_dict("NUM.txt")
LAUX_dict = readfile_dict("LAUX.txt")
RAUX_dcit = readfile_dict("RAUX.txt")
CONJ_dict = readfile_dict("CONJ.txt")
VATT_dict = readfile_dict("VATT.txt")

# TODO : build rule, add dict and use nltk.RecursiveDescentParser