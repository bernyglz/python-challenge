import os
import csv

# Path to collect data from the Resources folder
csvpath=os.path.join("election_data.csv")

voterid=[]
county=[]
candidate=[]
uniquelist=[]

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    totalvoters=0
    votosKhan=0
    votosCorrey=0
    votosLi=0
    votosOTooley=0

    first_row = next(csvreader)

    for row in csvreader:

        totalvoters=totalvoters+1
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

        if row[2] not in uniquelist:
            uniquelist.append(row[2])
        
        if row[2]=="Khan":
            votosKhan=votosKhan+1
        
        if row[2]=="Correy":
            votosCorrey=votosCorrey+1
        
        if row[2]=="Li":
            votosLi=votosLi+1
        
        if row[2]=="O'Tooley":
            votosOTooley=votosOTooley+1
        
    pctKhan=round(votosKhan/totalvoters,4)*100
    pctCorrey=round(votosCorrey/totalvoters,4)*100
    pctLi=round(votosLi/totalvoters,4)*100
    pctOTooley=round(votosOTooley/totalvoters,4)*100

    

        
#print(uniquelist)
str1= ("Election Results")
str2=("-------------------------------")
str3=(f"Total Voters {totalvoters}")
str4=(f"Khan obtuvo {pctKhan}% con {votosKhan} votos")
str5=(f"Correy obtuvo {pctCorrey}% con {votosCorrey} votos")
str6=(f"Li obtuvo {pctLi}% con {votosLi} votos")
str7=(f"O'Tooley obtuvo {pctOTooley}% con {votosOTooley} votos")
str8=("----------------------------------------------------------")

print(str1)
print(str2)
print(str3)
print(str4)
print(str5)
print(str6)
print(str7)
print(str8)

with open("Output.txt", "w") as text_file:
    print(str1)
    print(str2)
    print(str3)
    print(str4)
    print(str5)
    print(str6)
    print(str7)
    print(str8)

 



    