def get_full_name(first_name, last_name):
    fullname = first_name.title() + " " + last_name.title()
    return fullname

print(get_full_name('john', 'doe'))

def get_full_name_typed(first_name: str, last_name: str):
    fullname = first_name.title() + " " + last_name.title()
    return fullname


#simple Types 
#int
#float
#bool
#bytes

def process_names(items: list[str]):
    for item in items:
        print (item)

process_names(['faith', 'alimi', 'fatai'])


def union(items: int | str):
    print(items)

#classes as types 

class Person:
    def __init__(self, name:str):
        self.name = name

def get_person_name(onePerson: Person):
    return onePerson.name