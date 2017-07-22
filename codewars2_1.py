class Fraction:
    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator

    # Equality test

    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num

    # The rest goes here

    def __add__(self, other):
        return Fraction(self.top * other.bottom + other.top * self.bottom, self.bottom * other.bottom)

    def __repr__(self):
        a = self.top
        b = self.bottom
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return str(self.top // (a + b)) + '/' + str(self.bottom // (a + b))

        # Happy Coding ;)