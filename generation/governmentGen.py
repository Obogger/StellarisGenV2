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
    gestaltType = False
    governmentClass = "Normal"
    
    if raceType == "Machine":
        gestaltType = True
        governmentClass = "AI"
    elif random.randint(0, 9) == 5:
        gestaltType = True
        governmentClass = "Hivemind"         

    ethicsPreResult = []

    if gestaltType:
        outerAmount = random.randint(0, 1)
        innerAmount = random.randint(2 - outerAmount, 3)
        
        innerRingClone = innerRing.copy()
        outerRingClone = outerRing.copy()
        
        if outerAmount == 1:
            ethicsPreResult.append(random.choice(outerRingClone))
            
        for i in range(innerAmount):
            group = random.randint(0, (len(innerRingClone) - 1))
            ethicsPreResult.append(innerRingClone[group][random.randint(0, 1)])
            innerRingClone.pop(group) 
    else:
        fanaticEthicsClone = fanaticEthics.copy()
        ethicsClone = ethics.copy()
        
        fanaticAmount = random.randint(0,2)
        ethicMinimum = max(0, 3 - fanaticAmount * 2)
        ethicAmount = random.randint(ethicMinimum, 5 - fanaticAmount * 2)
        for i in range(fanaticAmount):
            ethicGroup = random.randint(0, (len(fanaticEthicsClone) - 1))
            ethicsPreResult.append(random.choice(fanaticEthicsClone[ethicGroup]))
            fanaticEthicsClone.pop(ethicGroup)
            ethicsClone.pop(ethicGroup)
        for i in range(ethicAmount):
            ethicGroup = random.randint(0, (len(ethicsClone) - 1))
            ethicsPreResult.append(random.choice(ethicsClone[ethicGroup]))
            ethicsClone.pop(ethicGroup)
            fanaticEthicsClone.pop(ethicGroup)
    
    return "\n".join(ethicsPreResult), governmentClass

def governmentAuthority(currentEthics, currentGovernmentClass):
    autority = ""
    
    if currentGovernmentClass == "AI":
        autority = "Machine intelligence"
    elif currentGovernmentClass == "Hivemind":
        autority = "Hivemind"
    else:
        company = random.randint(0,7) == 2
        
        if company:
            available_authorities = ["Corporation"]
            if "Libertarian" in currentEthics or "Cooperative" in currentEthics:
                available_authorities.append("Group Firm")
            if "Authoritarian" in currentEthics or "Competitive" in currentEthics:
                available_authorities.append("Dynastic Enterprise")
            if "Fanatic Authoritarian" in currentEthics or "Fanatic Libetarian" in currentEthics:
                available_authorities.remove("Corporation")
        else:
            available_authorities = ["Indirectly Democratic", "Oligarchic","Dictatorial"]
            if "Libertarian" in currentEthics:
                available_authorities.append("Directly Democratic")
                available_authorities.remove("Dictatorial")
            if "Authoritarian" in currentEthics:
                available_authorities.append("Imperial")
                available_authorities.remove("Indirectly Democratic")
            if "Fanatic Authoritarian" in currentEthics or "Fanatic Libetarian" in currentEthics:
                available_authorities.remove("Oligarchic")
        print(available_authorities)
        
        if available_authorities:
            autority = random.choice(available_authorities)
        else:
            print("No avalable autority")
            autority = "ERROR"
    
    return autority