class Arithmentics :
    def __init__(self, numbers):
        self.numbers = numbers


    def maxnumber(self):
        numbers = self.numbers
        max= numbers[0]
        for number in numbers:
            if number > max:
                max = number
        return(max)
    

    def minnumber(self):
        numbers = self.numbers
        min= numbers[0]
        for number in numbers:
            if number < min:
                min = number
        return(min)