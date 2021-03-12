#I created 5 cv and inserted them in a list after that i printed them with a for loop.
CV1={"Name":"Derya",
     "Surname":"Er",
     "Birthday":"10.10.1995",
     "Gender":"Female",
     "Number":"+905458965647",
     "Title":"Software Engineer"}
CV2={"Name":"Sefa",
     "Surname":"Oral",
     "Birthday":"03.01.1998",
     "Gender":"Male",
     "Number":"+905468953422",
     "Title":"IT Engineer"}
CV3={"Name":"Elgiz",
     "Surname":"Gündoğan",
     "Title":"Computer Engineer",
     "Birthday":"05.10.1994",
     "Gender":"Female",
     "Number":"+905325698657",}
CV4={"Name":"Rasim",
     "Surname":"Öztekin",
     "Title":"Software Engineer",
     "Birthday":"05.06.1997",
     "Gender":"Male",
     "Number":"+905344822537",}
CV5={"Name":"Poyraz",
     "Surname":"Karayel",
     "Title":"Software Engineer",
     "Birthday":"08.10.1990",
     "Gender":"Male",
     "Number":"+905443526987",}
d=[CV1,CV2,CV3,CV4,CV5]
for i in d:
    for k,v in i.items():
      print( k,":" , v)
    print("---------")
