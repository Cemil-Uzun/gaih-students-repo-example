
listOdd=[1,15,37,45,69,43]
listEven=[22,26,24,48,96]
listMerged=listOdd+listEven
listMerged=[element * 2 for element in listMerged]

for i in listMerged:
    print(i, type(i))