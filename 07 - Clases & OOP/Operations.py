from collections import Counter
import statistics

class Operations:
    def __init__(self, list:list):
        self.list = list
   
    def factorial(self,num:int):
        if num > 0 and type(num)==int:
            x=1
            f=1
            while x <= num:
                f=f*x
                x+=1
            return "The factorial of",num,"is",f
        elif num == 0 and type(num)==int:
            return "The factorial of",num,"is 1"
        else:
            return "The number must be a positive integer"
    def temperature_converter(self,num:int,scale:str,to:str):
        if scale == "celsius" and to == "kelvin":
            return num + 273.15
        elif scale == "celsius" and to == "farenheit":
            return num*(9/5)+32
        elif scale == "kelvin" and to == "celsius":
            return num - 273.15
        elif scale == "kelvin" and to == "farenheit":
            res = (num - 273.15)
            return res*(9/5)+32
        elif scale == "farenheit" and to == "celsius":
            return (num-32)*(5/9)
        elif scale == "farenheit" and to == "kelvin":
            res = (num-32)*(5/9)
            return res + 273.15
        elif scale == to:
            return num
        else:
            return "Enter valid parameters"

    def mode(self,list):
        mode = statistics.mode(list)
        count = Counter(list)
        return mode,count[mode]   
    
    def is_prime(self,num):
        for div in range(2,num):
            if num % div == 0:
                return False
            else:
                return True