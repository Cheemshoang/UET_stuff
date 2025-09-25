a,b = map(float, input().split())

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
    
    def mod(self):
        return self.x%self.y
    
    def div(self):
        return self.x//self.y
    
    def get_result(self):
        print("Addition: ", self.add())
        print("Subtraction: ", self.subtract())
        print("Multiplication: ", self.multiply())
        print("Division: ", self.divide())
        print("Mod", self.mod())
        print("Div", self.div())
        
calc = my_num_function(a,b)
calc.get_result()