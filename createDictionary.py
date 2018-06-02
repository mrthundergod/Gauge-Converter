import csv

file =open("AWG-SWG Dictionary.csv")

csvFile = csv.reader(file)
gauge = []
AWG = []
SWG =[]

AWGDict = {}
SWGDict = {}

for row in csvFile:
    gauge.append(row[0])
    AWG.append(row[1])
    SWG.append(row[2])


#print(gauge)
#print('\n')
print(AWG)
#print('\n')
print(SWG)

for i in range(len(gauge)):
    AWGDict[gauge[i]] = AWG[i]
    SWGDict[gauge[i]] = SWG[i]

#print (AWGDict)
#print (SWGDict)
