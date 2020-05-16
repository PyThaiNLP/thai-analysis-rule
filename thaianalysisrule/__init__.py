# -*- coding: utf-8 -*-
__version__ = "0.1dev0"
import os

import thaianalysisrule
from nltk.parse.generate import generate
import nltk
from pythainlp.tokenize import word_tokenize

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
N_dict = readfile_dict("N.txt")

RULE = """
S -> NP VP
VP -> V | V NP | V NP S | V NP PP ADV
PP -> PREP NP
V -> VERB | LAUX VERB | VERB RAUX | LAUX VERB RAUX
NP -> N | N DET | N CLAS DET | N CLAS VATT | N NUM CLAS DET | N VATT CLAS DET | NP PP | NP CONJ NP 
N -> {}
VERB -> {}
ADV -> {}
PREP -> {}
DET -> {}
CLAS -> {}
NUM -> {}
LAUX -> {}
RAUX -> {}
CONJ -> {}
VATT -> {}
""".format(N_dict, VERE_dict, ADV_dict, PREP_dict, DET_dict, CLAS_dict, NUM_dict, LAUX_dict, RAUX_dcit, CONJ_dict, VATT_dict)
thaigrammar = nltk.CFG.fromstring(RULE)
rd_parser = nltk.RecursiveDescentParser(thaigrammar)
parser2 = nltk.ChartParser(thaigrammar)
def generate_sent(n:int=1) -> list:
    global thaigrammar
    return [' '.join(i) for i in generate(thaigrammar, n=n)]

def parser(list_word:list, limit:int = 1) -> list:
    global parser2
    i = 0
    _list_data = []
    for tree in parser2.parse(list_word):
        if i<limit:
            _list_data.append(tree)
        else:
            break
        i+=1
    return _list_data

def word_seg_parser(txt:str) -> list:
    return parser(word_tokenize(txt))