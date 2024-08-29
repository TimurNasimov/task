my_dict = {"Alex": 1988, "Denis": 2000, "Inna": 1994}
print("Dict:", my_dict)
print("Existing value:", my_dict.get("Alex"))
print("Not existing value:", my_dict.get("Abram"))
my_dict.update({"Fedor": 1992,
                "Liza": 2010})
data_Inna = my_dict.pop("Inna")
print("Deleted value:",data_Inna)
print(my_dict)
my_set = {234, 345, "площадь", "диамитр", 234, 345.544, "площадь"}
print(my_set)
my_set.add((23,34,45))
my_set.add("Zoom")
my_set.remove(234)
print(my_set)
