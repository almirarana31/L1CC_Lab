

person1 = {
    "First_name":"Jeff",
    "Last_name":"-",
    "Age":"10",
}

person2 = {
    "First_name":"-",
    "Last_name":"-",
    "Age":"-",
}

L1cc = [person1,person2]

i = 1

for person in L1cc:
    print(str(i)+". name: " + person["First_name"],"\nage: " +person["Age"])
    i+=1
