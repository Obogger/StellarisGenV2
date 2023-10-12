import random
import time
fanaticEthics = [["Fanatic Authoritarian", "Fanatic Libetarian"], 
                 ["Fanatic Xenophobe", "Fanatic Xenophile"], 
                 ["Fanatic Militarist", "Fanatic Pacifist"],
                 ["Fanatic Spiritualist", "Fanatic Materialist"],
                 ["Fanatic Cooperative", "Fanatic Competitive"],
                 ["Fanatic Ecocentric", "Fanatic Anthropocentric"],
                 ["Fanatic Elitist", "Fanatic Pluralist"]]
ethics = []
for duals in fanaticEthics:
    str1 = duals[0].replace("Fanatic ", "")
    str2 = duals[1].replace("Fanatic ", "")
    ethics.append([str1, str2])
    
    
innerRing = [["Introspective" , "Extrospective"],
             ["Autonomous", "Convergent"],
             ["Affective", "Impassive"]]

outerRing = ["Progression", "Analysis", 
             "Enncroahcment", "Connection", 
             "Convalence", "logistics"]


def governmentEthicsGen(raceType):
    ethicsPreResult = []
    hiveType = True if random.randint(0,9) == 5 else False
    gestaltType = False
    if raceType == "Machine":
        gestaltType = True
        governmentClass = "AI"
    elif hiveType:
        gestaltType = True
        governmentClass = "Hivemind"         
    else:
        gestaltType = False
        governmentClass = "Normal"
    
    if gestaltType:
        outerAmount = random.randint(0, 1)
        innerAmount = random.randint(2 - outerAmount, 3)
        
        innerRingClone = innerRing.copy()
        outerRingClone = outerRing.copy()
        
        ethicsPreResult.append(outerRingClone[random.randint(0,(len(outerRingClone) - 1))]) if outerAmount == 1 else []
        
        for i in range(innerAmount):
            group = random.randint(0, (len(innerRingClone) - 1))
            ethicsPreResult.append(innerRingClone[group][random.randint(0, 1)])
            innerRingClone.pop(group) 
    else:
        fanaticEthicsClone = fanaticEthics.copy()
        ethicsClone = ethics.copy()
        fanaticAmount = random.randint(0,2)
        ethicMinimum = 0 if 3 - fanaticAmount*2 < 0 else 3 - fanaticAmount*2
        ethicAmount = random.randint((ethicMinimum),5-(fanaticAmount*2))
        for i in range(fanaticAmount):
            ethicGroup = random.randint(0, (len(fanaticEthicsClone) - 1))
            ethicsPreResult.append(fanaticEthicsClone[ethicGroup][random.randint(0,1)])
            fanaticEthicsClone.pop(ethicGroup)
            ethicsClone.pop(ethicGroup)
        for i in range(ethicAmount):
            ethicGroup = random.randint(0, (len(ethicsClone) - 1))
            ethicsPreResult.append(ethicsClone[ethicGroup][random.randint(0,1)])
            ethicsClone.pop(ethicGroup)
            fanaticEthicsClone.pop(ethicGroup)
    
    ethicsResult = ""
    for i in ethicsPreResult:
        ethicsResult += i + "\n"
    return ethicsResult, governmentClass

def governmentAuthority(currentEthics, currentGovernmentClass):
    autority = ""
    avalableAthority = []
    if currentGovernmentClass == "AI":
        autority = "Machine intelligence"
    elif currentGovernmentClass == "Hivemind":
        autority = "Hivemind"
    else:
        company = True if random.randint(0,7) == 2 else False
        if company:
            avalableAthority = ["Corporation"]
            if "Libertarian" in currentEthics or "Cooperative" in currentEthics:
                avalableAthority.append("Group Firm")
            if "Authoritarian" in currentEthics or "Competitive" in currentEthics:
                avalableAthority.append("Dynastic Enterprise")
            if "Fanatic Authoritarian" in currentEthics or "Fanatic Libetarian" in currentEthics:
                avalableAthority.remove("Corporation")
        else:
            avalableAthority = ["Indirectly Democratic", "Oligarchic","Dictatorial"]
            if "Libertarian" in currentEthics:
                avalableAthority.append("Directly Democratic")
                avalableAthority.remove("Dictatorial")
            if "Authoritarian" in currentEthics:
                avalableAthority.append("Imperial")
                avalableAthority.remove("Indirectly Democratic")
            if "Fanatic Authoritarian" in currentEthics or "Fanatic Libetarian" in currentEthics:
                avalableAthority.remove("Oligarchic")
        print(avalableAthority)
        try:
            autority = avalableAthority[random.randint(0, (len(avalableAthority) - 1))]
        except:
            print("No avalable autority")
            autority = "ERROR"
    
    return autority