#create dictionary with student details
students ={
    101: {"name": "Rahul", "Score":[20, 30, 40]},
    102: {"name": "Arpit", "Score":[30, 40,60]},
    103: {"name": "Bhushan", "Score":[40, 50]},
    104: {"name": "HD", "Score":[12, 12,12]},
    105: {"name": "PD", "Score":[60, 70,80,21]},
}

#calculate avegrage score and flag pass/fail
for sid,details in students.items():
    avg= sum(details["Score"])/len(details["Score"])#average using sum and len
    details["Average"]=avg
    details["Passed"]= avg >=30 #Boolean flag

#print name of students who passed
print("Students who passed:")
for sid, details in students.items():
    if details["Passed"]:
        print(details ["name"])