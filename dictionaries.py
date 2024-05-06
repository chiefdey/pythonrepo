# collection of key value pairs enclosed with {}
my_dict={
    "name":"denis",
    "gender":"male",
    "age":20,
    "address":{"town":"kiambu",
               "code":254,
               "location":["kikuyu",28]}
}
# accessing values using the keys
# print(my_dict["address"][1])
print(my_dict["address"]["location"][1])
# modifying values
my_dict["name"]="muriithi"
# adding
my_dict["id"]=10209309
my_dict['occupation']="developer"
del my_dict["address"]
print(my_dict)