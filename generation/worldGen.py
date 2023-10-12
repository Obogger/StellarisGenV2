import random

def planetClassGenerator():
    planetResult = random.randint(1,9)
    return planetResult

def originGenerator(originNames):
    originResult = random.randint(0, len(originNames)- 1)
    return originNames[originResult]
    