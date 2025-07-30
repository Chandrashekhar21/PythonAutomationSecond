from time import process_time

My_list_1 = [1,2,3,4,5,6,7,8,9]
My_list_2 = [1,True,"Chandrashekhar",3]

print(My_list_1)
print(My_list_2)
print(len(My_list_1))


print(My_list_1[1])

for i in range(len(My_list_1)):
    print(My_list_1[i])

print("Hello")

for item in My_list_1:
    print(item, end=" ")


print("Hello,  How are you")

for item in My_list_1:
    print(item, end=" ")


print("Hello, How are you")

for i in iter(My_list_1):
    print(i," Hello",end=" ")
