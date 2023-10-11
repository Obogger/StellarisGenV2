import tkinter as tk
import random 
import randomRaceGen
import worldGen
import governmentGen
import os
import json
import re

window = tk.Tk()

window.geometry("1500x750")
window.title("Stellaris GEN :)")

resulution = 1
vanillaTraitsFile = open("D:/SteamLibrary/steamapps/common/Stellaris/common/traits/04_species_traits.txt")
vanilaRoboticTraitsFile = open("D:/SteamLibrary/steamapps/common/Stellaris/common/traits/05_species_traits_robotic.txt")

OriginLines = []
TraitLines = vanillaTraitsFile.readlines() + vanilaRoboticTraitsFile.readlines()

activeModsNumber = []
activeModsFile = open("C:/Users/kevdo/Documents/Paradox Interactive/Stellaris/dlc_load.json")
activeModsData = json.load(activeModsFile)
for i in activeModsData['enabled_mods']:        
    activeModsNumber.append(re.findall(r'\d+', i))
    
rootDirectory = "D:/SteamLibrary/steamapps/workshop/content/281990/"
rootEndDirectory = "/common/governments/civics"

print(activeModsNumber)
for i in activeModsNumber:
    filename = i
    filename = filename[0]
    directory = os.path.join(rootDirectory, filename)
    directory += rootEndDirectory
    print(directory)
    print(os.path.exists(directory))
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            if "origin" in filename:
                file = os.path.join(directory, filename)
                currentFile = open(file)
                currentFileText = currentFile.readlines()
                OriginLines += currentFileText
    else:
        print("File path does not exist")

os.system("pause")

directory = "D:/SteamLibrary/steamapps/workshop/content/281990/1928831043/common/traits"

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    currentFile = open(file)
    currentFileText = currentFile.readlines()
    TraitLines += currentFileText

originNames = []
traitNames = []
traitAllowedType = []
traitNotCopatible = []
charactersToRemove = ["=", "{", " ", "}", "allowed_archetypes","\n","\t","PRESAPIENT"]

def stringCleanUp(stringToClean):
    for x in range(len(charactersToRemove)):
            stringToClean = stringToClean.replace(charactersToRemove[x], "")
    return stringToClean

label = []
questionTextWidget = []
       
def randomGeneratorOutput():
    stringToWrite = []
    stringQuestionToWrite = ["Race:", "Race Type:", "Planet:", "Origin:", "Government Class:", "Authoority", "Ethics:"]
    raceNumber, race = randomRaceGen.raceGenerator()
    stringToWrite.append(race)
    stringToWrite.append(randomRaceGen.raceTypeGenerator(raceNumber))
    stringToWrite.append(worldGen.planetClassGenerator())
    stringToWrite.append(worldGen.originGenerator(originNames))
    ethics, governmentClass = governmentGen.governmentEthicsGen(race)
    stringToWrite.append(governmentClass)
    stringToWrite.append(governmentGen.governmentAuthority(ethics, governmentClass))
    stringToWrite.append(ethics)
    stringToWrite.append(randomRaceGen.traitGenerator(traitNames, traitAllowedType, race, traitNotCopatible))
    if len(label) == 0:
        for i in range(len(stringToWrite)):
            label.append(tk.Label(window, text="", font=('Arial', 16), width=25))
            label[i].place(relx=0.725,
                           rely=0.10 +(0.05 * i))
        for i in range(len(stringQuestionToWrite)):
            questionTextWidget.append(tk.Label(window, text=stringQuestionToWrite[i], font=('Arial', 16), width=15))
            questionTextWidget[i].place(relx=0.625,
                           rely=0.10 +(0.05 * i))
    
    for i in range(len(stringToWrite)):
        label[i].configure(text=stringToWrite[i])



foundTrait = False
for i in range(len(TraitLines)):
    if "allowed_archetypes" in TraitLines[i]:
        tempLine = TraitLines[i]
        traitAllowedType.append(stringCleanUp(tempLine))
    if TraitLines[i][0] == 't' and TraitLines[i][1]== 'r':
        if foundTrait:
            traitNotCopatible.append('opposite" "')
        foundTrait = True
        tempLine = TraitLines[i]
        traitNames.append(stringCleanUp(tempLine))
    if "opposites" in TraitLines[i]:
        foundTrait = False
        tempLine = TraitLines[i]
        if "}" in TraitLines[i]:
            traitNotCopatible.append(stringCleanUp(tempLine))
        else:
            print("exvep")
            while "}" not in TraitLines[i + 1]:
                print (tempLine)
                tempLine += TraitLines[i + 1]
                i += 1
            traitNotCopatible.append(stringCleanUp(tempLine))

while len(traitNames) > len(traitNotCopatible):
    traitNotCopatible.append('opposite" "')

    

for i in range(len(OriginLines)):
    if OriginLines[i][0] == 'o' and OriginLines[i][1]== 'r':
            tempLine = OriginLines[i]
            originNames.append(stringCleanUp(tempLine))
    if ("playable" in OriginLines[i] or "potential" in OriginLines[i]) and ("always = no" in OriginLines[i + 1] or "always = no" in OriginLines[i]):
        print("NPCS IRGIN")
        originNames.pop(len(originNames) - 1)
    if "potential" in OriginLines[i] and "#Origin related to the story and player choices" in OriginLines[i]:
        print("Non playanle")
        originNames.pop(len(originNames) - 1)
    if "has_humanoids = no" in OriginLines[i] or "has_aquatics = no" in OriginLines[i]:
        print("Too many dlc manen")
        originNames.pop(len(originNames) - 1)
def showList():
    traitList.place(x=0,
                    y=0)
    traitAllowedTypeList.place(x=250,
                            y=0)

    traitNotCopatibleList.place(x=500,
                                  y=0)
    originList.place(x=750,
                    y=0)
    debugDataButton.configure(command=hideList)

def hideList():
    traitList.place_forget()
    traitAllowedTypeList.place_forget()
    traitNotCopatibleList.place_forget()
    originList.place_forget()
    debugDataButton.configure(command=showList)


restartButton = tk.Button(window, height=1, width=15, text="Clicker me NOW!", font=('Arial', 16), command=randomGeneratorOutput, bg="Lime")
restartButton.place(relx=0.70,
                    rely=0.8)
debugDataButton = tk.Button(window, height=1, width=5, text="Debug", font=('Arial', 16), command=showList, bg="Red")
debugDataButton.place(relx=0.90,
                    rely=0)


traitList = tk.Listbox(window, height=int(30 * resulution), font=('Arial', 16))
traitAllowedTypeList = tk.Listbox(window, height=int(30 * resulution), font=('Arial', 16))
traitNotCopatibleList = tk.Listbox(window, height=int(30 * resulution), font=('Arial', 16))

originList = tk.Listbox(window, height=int(30 * resulution), font=('Arial', 16)) 

for i in range(len(traitNames)):
    traitList.insert(i, str(i+1) + " " + traitNames[i])
for i in range(len(traitAllowedType)):
    traitAllowedTypeList.insert(i, str(i+1) + " " + traitAllowedType[i])
for i in range(len(traitNotCopatible)):
    traitNotCopatibleList.insert(i, str(i+1) + " " + traitNotCopatible[i])
for i in range(len(originNames)):
    originList.insert(i,str(i+1) + " " + originNames[i])
    
window.mainloop()