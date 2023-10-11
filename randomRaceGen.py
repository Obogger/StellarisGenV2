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

def traitGenerator(traitNames, traitRace, race, traitOppsite, quality):
    traitOppsiteClone = traitOppsite.copy()
    traitNamesClone = traitNames.copy()
    traitRaceClone = traitRace.copy()
    if race == "Lithoid":
        print("IS ltipid")
        for i in range(len(traitNamesClone)):
            if "LITHOID" not in traitRaceClone[i]:
                traitNamesClone[i] = ""
                traitRaceClone[i] = ""
    elif race == "Machine":
        print("IS Machine")
        for i in range(len(traitNamesClone)):
            if "ROBOT" not in traitRaceClone[i] and "MACHINE" not in traitRaceClone[i]:
                traitNamesClone[i] = ""
                traitRaceClone[i] = ""
    else:
        print("IS Nomral")
        for i in range(len(traitNamesClone)):
            if "BIOLOGICAL" not in traitRaceClone[i]:
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
    randomTraits = []
    result = ""
    for i in range(5):
        currentTrait = random.randint(0,len(traitNamesClone) - 1)
        randomTraits.append(traitNamesClone[currentTrait])
        traitNamesClone.pop(currentTrait)
    for i in range(len(randomTraits)):
        result = result + randomTraits[i] + "\n"
    print(result, randomTraits)  
    return result

def qualityGenerator(race):
    qualityText = ["Failure", "Incapable", "Inferior", "Normal", "Superior", "Gifted", "Perfect"]
    qualityTextMachine = ["Scrap","Normal","Excellent"]
    
    if race == "Machine":
        quality = random.choices(qualityTextMachine, weights=[15, 80, 15])
    else:
        quality = random.choices(qualityText, weights=[5, 5, 10, 60, 10, 5, 5])
        
    return quality