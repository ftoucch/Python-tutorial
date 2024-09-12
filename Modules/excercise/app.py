from utils import Arithmentics
users_number = input('please enter numbers seperated by a comma: ')
numbers = list(map(int, users_number.split(',')))
arithmetics = Arithmentics(numbers)
try:
    minnumber = arithmetics.minnumber()
    maxnumber = arithmetics.maxnumber()
    print(f"Min Number: {minnumber}, Max Number: {maxnumber}")
except TypeError:
    print('all entry in numbers must be a type int')