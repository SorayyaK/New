# # This code aims to show the performance of the immutable objects
# #They both bound to the same thing
# result = True
# another_result = result
# print(id(result))
# print(id(another_result))
#
# #We get another id
#
# reslut = False
# print(id(reslut))


result = "Correct"
another_result = result
print(id(result))
print(id(another_result))
#Because string is immuatble so python makes new id and apply the changes to the new variable
result +="ish"
print(id(result))
print(id(another_result))

# This is the second chabnge