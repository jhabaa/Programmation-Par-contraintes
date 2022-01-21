"""FlyOrder.py
Application de commande de billets d'avions pour le cours d'informatique décisionnelle partie 3
tailles des avions (nombre de places), la classe de voyage, les escales et heures de vols.
Voici le problème:
Un utilisateur veut commander un billet d'avion. Pour cela, il doit choisir:
Sa destination
Sa classe de voyage
Vol de jour ou de nuit
Avec escale ou non 

Avions:
Les avions 1,2 et 4 disposent d'une Première Classe
Les avions 1 et 3 font escale à Rio
Les avions 1 et 4 font escale à Bruxelles
L'avion 5 fait escale à Miami
l'avion 4 décole avant midi
Les avions 
Liste des destinations:
1 -> Yaoundé
2 -> Bruxelles
3 -> Miami
4 -> New Delhi
5 -> Rio

Contraintes:
1 - Nous ne pouvons prendre qu'un seul avion à la fois
2 - L'utilisateur peut décider de souhaiter une escale ou pas
"""
#=========================================== Used Library ========================================================
from tkinter import *
from tkinter import ttk
from constraint import *

varDest = []
varClass = []
varTime = []
varEscale = []
Planes = []

#============================================ Planes Dictionnary (Unused) ==================================================
planeDict1 = {'plane':1, 'destination':"Yaounde", 'day':1, 'type':1, 'escales':"Rio,Bruxelles", 'firstClass':1, 'night':1}
planeDict2 = {'plane':2, 'destination':"Bruxelles", 'day':1, 'type':0, 'escales':"",'firstClass':1,'night':1}
planeDict3 = {'plane':3, 'destination':"Miami", 'day':1, 'type':1, 'escales':"Rio",'firstClass':0, 'night':1}
planeDict4 = {'plane':4, 'destination':"New-Delhi", 'day':1, 'type':1, 'escales':"Bruxelles",'firstClass':1, 'night':0}
planeDict5 = {'plane':5, 'destination':"Rio", 'day':1, 'type':1, 'escales':"Miami",'firstClass':0, 'night':1}
 
listPlane = list((planeDict1, planeDict2, planeDict3, planeDict4, planeDict5))

def retrieve1():# Unused
    global varDest, varClass, varTime, varEscale
    
    #Fill variables up to entries
    for element in listPlane:
        varClass.append(element['plane'])
        if element['destination'] == Combo.get():
            varDest.append(element['plane'])
        if element['firstClass'] == flyClass.get():
            varClass.append(element['plane'])
        if element['day'] == day.get():
            varTime.append(element['plane'])
        if element['night'] == night.get():
            varTime.append(element['plane'])
        if element['type'] == escale.get():
            varEscale.append(element['plane'])
    print(varDest)
    print(varClass)
    print(varEscale)
    print(varTime)    
    
    #print(varDest[1])

def retrieve():
    global varDest, varClass, varTime, varEscale
#Fill Destination list by Planes
    if Combo.get() == "Yaounde":
        varDest = [1]
    if Combo.get() == "Bruxelles":
        varDest.append(1)
        varDest.append(2)
        varDest.append(4)
    if Combo.get() == "Miami":
        varDest.append(3)
        varDest.append(5)
    if Combo.get() == "New-Delhi":
        varDest.append(4)
    if Combo.get() == "Rio":
        varDest = [1,3,5]
    #Fill classes
    if flyClass.get() == 1:
        varClass.append(1)
        varClass.append(2)
        varClass.append(4)
    if flyClass.get() == 0:
        varClass = [1,2,3,4,5]
    #Fill Time of flight
    if night.get() == 1 & day.get() == 1:
        varTime = [1,2,3,4,5]
    if day.get() == 0 & night.get() == 1:
        varTime = [1,2]
    if day.get() ==1 & night.get() ==0:
        varTime = [3,4,5]
    if day.get() == 0 & night.get() == 0:
        varTime = [1,2,3,4,5]
    
    #RoundTrip
    if escale.get() == 1:
        varEscale = [1,3,4,5]
    if escale.get() == 0:
        varEscale = [1]





def findAFly():
    global resultText, planesToTake, Planes
    retrieve()
    problem = Problem()
    problem.addVariable("Destination", varDest)
    problem.addVariable("Classe", varClass)
    problem.addVariable("Time", varTime)
    problem.addVariable("Escale", varEscale)
    problem.addConstraint(lambda a, b, c, d: a == b == c == d, ("Destination","Time","Escale","Classe"))
    for a in problem.getSolutions() :
        
        if a.get("Destination") == 1:
            planesToTake.set(planesToTake.get() + "Avion 1 \n")
        if a.get("Destination") == 2:
            planesToTake.set(planesToTake.get() + "Avion 2 \n")
        if a.get("Destination") == 3:
            planesToTake.set(planesToTake.get() + "Avion 3 \n")
        if a.get("Destination") == 4:
            planesToTake.set(planesToTake.get() + "Avion 4 \n")
        if a.get("Destination") == 5:
            planesToTake.set(planesToTake.get() + "Avion 5 \n")
            
    resultText.set(problem.getSolutions())
    print(problem.getSolutions())


#====================================== INTERFACE ==============================================    
window = Tk()
window.geometry("400x500")
frame = Frame(window)
frame.pack()

planesToTake = StringVar()
resultText = StringVar()
resultText.set("Result Of your Search")

labelTitle = ttk.Label(frame, text="Welcome To our Fly Picker APP")
labelTitle.pack()  

#Choose your destination in List
vlist = ["Yaounde", "Bruxelles", "Miami",
          "New-Delhi", "Rio"]
 
Combo = ttk.Combobox(frame, values = vlist)
Combo.set("Choisir une Destination")
Combo.pack()


searchButton = ttk.Button(window, text="Search", command=findAFly)
searchButton.pack()
#First Class or Eco
flyClass = IntVar()
firstclass = ttk.Radiobutton(frame, text="Première classe", variable=flyClass, value = 1)
ecoClass = ttk.Radiobutton(frame, text="Classe Eco", variable=flyClass, value=0)
firstclass.pack()
ecoClass.pack()
#Vol de jour ou de nuit
day = IntVar()
night = IntVar()
dayFlight = ttk.Checkbutton(frame, text="Day", variable=day)
nightFlight = ttk.Checkbutton(frame, text="Night", variable=night)
dayFlight.pack()
nightFlight.pack()
#Escale ou pas
escale = IntVar()
escaleCheck = ttk.Checkbutton(frame, text="Escale", variable = escale)
escaleCheck.pack()

#Response Frame
responseFrame = ttk.Frame(window)
responseFrame.pack()
labelresult = ttk.Label(responseFrame, textvariable = planesToTake, wraplength = 350)
labelresult.pack()
window.title("Fly Selector")
window.mainloop()

