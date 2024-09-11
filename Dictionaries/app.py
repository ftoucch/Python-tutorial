# used when we want to store key value pairs 

customer = {
    "name" : "John Doe",
    "age" : 30,
    "is_verified" : True
}

print(customer["name"])

# we can use the get method if we do not want python to yell at us 

print(customer.get("birthdate", "Jan 1 1980")) # i am adding the value here to make this better. 