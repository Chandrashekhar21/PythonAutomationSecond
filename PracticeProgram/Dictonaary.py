

my_dict_Student1 = {"id" : 1, "name" : "Chandrashekahr", "address":{"Address1": "Pune", "Address2": "Nagpur"}}
print(my_dict_Student1)
my_dict_Student2 = {"id" : 2, "name" :"Raksha", "address":{"Address1": "Pune", "Address2": "Baramati"}}
print(my_dict_Student2)

del my_dict_Student2["address"]
print(my_dict_Student2)
my_dict_Student2["address"] = {"Address1": "Aurngabad", "Address2": "Nagpur"}
print(my_dict_Student2)

print("\n")
for key, value in my_dict_Student2.items():
    print(key,"----> ", value)


# empty dictionary

dict = {}
print(dict)

# Check the value present in dictionary

print("name" in my_dict_Student2)


# Chekc with student information
my_dict_Student3 = {"id" : 1, "name" : "Chandrashekahr", "address":{"Address1": "Pune", "Address2": "Nagpur"}}
my_dict_Student4 = {"id" : 1, "name" : "Chandrashekahr", "address":{"Address1": "Pune", "Address2": "Nagpur"}}

# You can create dictionary using dict

student =  dict(name = "Chandrashekahr", address = "Chandrapur")
print(student)
