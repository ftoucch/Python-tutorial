# unlike positional arguments the order does not matter in keyword arguments

def greet_user(first_name, last_name) :
    print(f'Hi {first_name} {last_name} ! ')
    print ('welcome aboard')

greet_user(first_name="fatai", last_name="james")