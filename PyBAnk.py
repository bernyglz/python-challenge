import os
import csv

# Path to collect data from the Resources folder
csvpath=os.path.join("budget_data.csv")

Date=[]
ProfLos=[]
Change=[]


with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    maxproflos=0
    sumchange=0
    rec=86
    totproflos=0
    minproflos=0
    sumchange=0
    contador=0
    proflosant=0
    proflosact=0

    
    first_row = next(csvreader)

    for row in csvreader:
        
        Date.append([0])
        ProfLos.append([1])
        totproflos=totproflos+int(row[1])
        contador=contador+1
        
        proflosact=int(row[1])
                
        Change.append(proflosact-proflosant)

        proflosant=int(row[1])     

        #if proflosact>maxproflos:
         #   maxproflos=proflosact
        
        #if proflosact<minproflos:
         #   minproflos=proflosact
        
        minchg=min(Change)
        maxchg=max(Change)
        avechg=(sum(Change)-867884)/85
        
        
print(f"Financial Analysis")
print(f"------------------------------------")
print(f"Total months= {contador}")
print(f"Total Amount of $ {totproflos}")
print(f"Average Profit of $ {avechg}")
print(f"Greatest Increase in Profits: {maxchg}")
print(f"Greatest Decreas in Profits: {minchg} ")
#print(Change)
#print(contador)