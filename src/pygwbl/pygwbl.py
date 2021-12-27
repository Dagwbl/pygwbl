import os

__name__ ='pygwbl'
__all__=["svg2emf","about"]


def svg2emf(FileName):
    os.system("inkscape --export-type=emf "+ FileName)

def about():
    print("Hi, I am Dagwbl. ")

