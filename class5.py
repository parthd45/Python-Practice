#dictionary
student = {101:{"name":"Parth","age":20,"marks":78},#nested addition
           102:{"name":"Rahul","age":22,"marks":85},
           103:{"name":"Priya","age":21,"marks":92}}
for std, details in student.items():
    avg = sum(details["marks"])/len(details["marks"])
    passed