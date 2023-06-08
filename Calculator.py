from typing import Union
import math


class Calculator:

    def __init__(self):
        '''Empty init'''
        pass

    def divide(self, number1: Union[int, float], number2: Union[int, float]):
        '''
        Parameter:
            number1 (int or float): First number to division
            number2 (int or float): Second number to division

        Returns:
            Float: Returns a division of two numbers informed
        '''

        self.number1 = number1
        self.number2 = number2

        try:
            self.result = self.number1 / self.number2

        except TypeError:
            raise TypeError

        except ZeroDivisionError:
            raise ZeroDivisionError

        return self.result

    def multiply(self, number1: Union[int, float], number2: Union[int, float]):
        '''
        Parameter:
            number1 (int or float): First number to multiplication
            number2 (int or float): Second number to multiplication

        Returns:
            Float or Int: Returns a multiplication of two numbers informed
        '''

        self.number1 = number1
        self.number2 = number2

        if isinstance(self.number1, str) or isinstance(self.number2, str):
            raise TypeError

        self.result = self.number1 * self.number2
        return self.result

    def sum(self, number1: Union[int, float], number2: Union[int, float]):
        '''
        Parameter:
            number1 (int or float): First number to sum
            number2 (int or float): Second number to sum

        Returns:
            Float or Int: Returns a sum of two numbers informed
        '''

        self.number1 = number1
        self.number2 = number2

        try:
            self.result = self.number1 + self.number2

        except TypeError:
            raise TypeError

        return self.result

    def subtract(self, number1: Union[int, float], number2: Union[int, float]):
        '''
        Parameter:
            number1 (int or float): First number to subtraction
            number2 (int or float): Second number to subtraction

        Returns:
            Float or Int: Returns a subtraction of two numbers informed
        '''

        self.number1 = number1
        self.number2 = number2

        try:
            self.result = self.number1 - self.number2

        except TypeError:
            raise TypeError

        return self.result
    
    def calculate_average(self, numbers):
        if not numbers:
            return None
        total = sum(numbers)
        return total/len(numbers)

    def calculate_stdev(self, numbers):
        if not isinstance(numbers, list):
            raise TypeError
        n = len(numbers)
        if n < 2:
            raise ValueError("Standard deviation requires at least two data points.")
        

        mean = sum(numbers) / n
        squared_diff_sum = sum((x - mean) ** 2 for x in numbers)

        variance = squared_diff_sum / (n - 1)
        standard_deviation = round(math.sqrt(variance), 3)

        return standard_deviation

    def calculate_var(self, numbers):
        if not isinstance(numbers, list):
            raise TypeError
        n = len(numbers)
        if n < 2:
            raise ValueError("Standard deviation requires at least two data points.")

        mean = sum(numbers) / n
        squared_diff_sum = sum((x - mean) ** 2 for x in numbers)

        variance = round(squared_diff_sum / (n - 1), 3)

        return variance

    def calculate_z_score(self, x, numbers):
        self.x = x
        self.numbers = numbers
        if not isinstance(self.numbers, list):
            raise TypeError
        elif not isinstance(self.x, int):
            raise TypeError
        mean = self.calculate_average(numbers)
        stdev = self.calculate_stdev(numbers)
        z_score = (x - mean) / stdev
        return z_score
        