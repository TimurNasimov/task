immutable_var = 123, "string", True
print(immutable_var)
 # immutable_var [0] = 324 - Картеж это такая же колекция как и список, но её особенность в том что он не изменямая!
mutable_list = [1,2,3,"string",5]
mutable_list[0] = 33
mutable_list[3] = "main"
mutable_list[4] = True
print(mutable_list)
