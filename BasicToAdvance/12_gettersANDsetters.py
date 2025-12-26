# Getters and setters are used to access and update private data safely.
# They are a core part of Encapsulation (OOP principle).

class Employee:
    def __init__(self,salary):
        self.__salary = salary   # private variable

    @property
    def salary(self):
        """Getter method to access salary"""
        return self.__salary
    @salary.setter
    def salary(self, amount):
        """Setter method to update salary with validation"""
        if amount < 0:
            print("Salary cannot be negative.")
        else:
            self.__salary = amount
e=Employee(50000)
print(e.salary)  # Accessing salary using getter
e.salary = 60000  # Updating salary using setter
print(e.salary)
e.salary = -1000  # Attempting to set a negative salary    
# Output:
# 50000
# 60000     
# Salary cannot be negative. 


# Normal way
class Employee:
    def __init__(self, salary):
        self.__salary = salary   # private variable

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary")
e = Employee(30000)
print(e.get_salary())     # 30000
e.set_salary(40000)
print(e.get_salary())     # 40000
e.set_salary(-5000)      # Invalid salary