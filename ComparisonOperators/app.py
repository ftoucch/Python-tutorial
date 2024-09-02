name = input("please enter your name: ")
name_character_length = len(name)

if name_character_length < 3 :
    print("Name must be at least  characters")
elif name_character_length > 50 :
    print("name can be a maximum of 50 characters")
else:
    print("that looks good")

