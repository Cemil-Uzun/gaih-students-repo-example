#Getting necessary info from the user
i=0
d={}
for i in range (0,5):
    student=input("Student Name:")
    midterm=int(input("Midterm Grade:"))
    project=int(input("Project Grade:"))
    final=int(input("Final Grade:"))
    total=0.3*midterm+0.3*project+0.4*final
    d[student]=total
    i +=1
print(d)

#Appending dictionary values (total scores) to list
list=[]
for k in d.values():
    list.append(k)

#Sorting values from higher to lower
list.sort()
list=list[::-1]
print(list)

#Calling keys by values
listOfKeys=[]
for x in list:
    y =[key for (key, value) in d.items() if value == x]
    listOfKeys.append(y)

#flatten list
flat_list = [item for sublist in listOfKeys for item in sublist]
print(flat_list)