student_1 = {"id" : 1, "name" : "Chandrashekahr", "address":{"home_address": "Pune", "office_address": "Nagpur"} }

student_2= {"id" : 2, "name": "Raksha", "address" : {"home_address": "Pune", "office_address": "Nagpur"}}


print(student_1)
print(student_2)
print(student_2["id"])
print(student_2["name"])
print(student_2["address"]["office_address"])


# Adding two dictionary in one list using [ dic1 , dict2] -> you can access using indexing which is starting from 0
student_list = [student_1, student_2]

print(student_list[0]["address"])

print("\n")
for key, value in student_1.items():
    print(key,'------------> ', value)