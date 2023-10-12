import random

def raceGenerator():
    raceName = ["Humanoid", "Machine", "Mammalian","Reptilian","Avian","Arhtropoid",
                "Molluscoid","Fungoid","Plantoid","Lithoid","Necroid",
                "Aquatic","Toxoid"]
    raceAmount = len(raceName)
    raceResult = random.randint(0, raceAmount-1)
    return raceResult, raceName[raceResult]

def raceTypeGenerator(raceReslut):
    raceTypes = [19,13,18,17,18,18,16,16,17,16,16,15,15]
    raceAmount =raceTypes[raceReslut]
    raceTypeResult = random.randint(1, raceAmount)
    return raceTypeResult

def traitGenerator(traitNames, traitRace, race, traitOppsite):
    traitOppsiteClone = traitOppsite.copy()
    traitNamesClone = traitNames.copy()
    traitRaceClone = traitRace.copy()
    if race == "Lithoid":
        print("IS ltipid")
        for i in range(len(traitNamesClone)):
            if "LITHOID" not in traitRaceClone[i]:
                traitNamesClone[i] = ""
                traitRaceClone[i] = ""
    if race == "Machine":
        print("IS Machine")
        for i in range(len(traitNamesClone)):
            if "ROBOT" not in traitRaceClone[i] and "MACHINE" not in traitRaceClone[i]:
                traitNamesClone[i] = ""
                traitRaceClone[i] = ""
    listLenght = len(traitNamesClone)
    k = 0
    for i in range(listLenght):
        if traitNamesClone[i - k] == "":
            k += 1
            print("Delted someshit")
            traitNamesClone.remove("")
            traitRaceClone.remove("")
    print(traitNamesClone)
    return traitNamesClone

def qualityGenerator(race):
    return