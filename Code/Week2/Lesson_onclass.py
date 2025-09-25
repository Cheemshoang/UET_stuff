# a = float(input("number1: "))
# b = float(input("number2: "))

n = int(input("num: "))
x = str(input("str1: "))
y = str(input("str2: "))


class my_num_function:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        if self.y == 0: 
            return "null"
        else:
            return self.x / self.y
    
    def power(self):
        return self.x ** self.y 
    
    def factorial(self):
        if self.x < 0:
            return "DNF"
        else:
            fact = 1
            for i in range(1, int(self.x) + 1):
                fact *= i
        return fact
    
    def compare(self):
        if self.x > self.y:
            return "x greater than y"
        elif self.x == self.y:
            return "x = y"
        else:
            return "x smaller than y"
    def get_result(self):
        print("Addition: ", self.add())
        print("Subtraction: ", self.subtract())
        print("Multiplication: ", self.multiply())
        print("Division: ", self.divide())
        print("Power: ", self.power())
        print("Factorial of first number: ", self.factorial())
        print("Compare: ", self.compare())
        
        
class my_string_function:
    def __init__(self, x,y,n):
        self.x = x
        self.y = y
        self.n = n
    
    def combine_string(self):
        return self.x + self.y 
    
    def mul_string(self):
        for i in range(0, self.n+1):
            self.x += self.x
            return self.x
        

    
    def get_result(self):
        print("Combine string: ", self.combine_string())
        print("Mul_string: ", self.mul_string())
    

# calc = my_num_function(a, b)
# calc.get_result()``

string = my_string_function(x,y,n)
string.get_result()


