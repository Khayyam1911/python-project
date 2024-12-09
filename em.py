from abc import ABC, abstractmethod  # For abstraction

class Employee(ABC):
    def __init__(self, name, emp_id, salary):
        self.__name = name        
        self.__emp_id = emp_id     
        self.__salary = salary    
   
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    
    def get_emp_id(self):
        return self.__emp_id
    
    def set_emp_id(self, emp_id):
        self.__emp_id = emp_id

    
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    
    @abstractmethod
    def calculate_bonus(self):
        pass

    def __str__(self):
        return f"Employee ID: {self.__emp_id}, Name: {self.__name}, Salary: {self.__salary}"

class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, salary, department):
        super().__init__(name, emp_id, salary)
        self.department = department  
    
    def calculate_bonus(self):
        return self.get_salary() * 0.10 
    def __str__(self):
        return super().__str__() + f", Department: {self.department}"


class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, salary, hours_worked):
        super().__init__(name, emp_id, salary)
        self.hours_worked = hours_worked 

    
    def calculate_bonus(self):
        return self.hours_worked * 50  
    def __str__(self):
        return super().__str__() + f", Hours Worked: {self.hours_worked}"


class Intern(Employee):
    def __init__(self, name, emp_id, salary, mentor):
        super().__init__(name, emp_id, salary)
        self.mentor = mentor  
    
    def calculate_bonus(self):
        return 0 
    def __str__(self):
        return super().__str__() + f", Mentor: {self.mentor}"


if __name__ == "__main__":
    
    emp1 = FullTimeEmployee("Alice", 101, 50000, "IT")
    emp2 = PartTimeEmployee("Bob", 102, 20000, 20)
    emp3 = Intern("Charlie", 103, 15000, "David")

    
    employees = [emp1, emp2, emp3]

    
    print("Employee Details and Bonuses:")
    for emp in employees:
        print(emp)
        print(f"Bonus: {emp.calculate_bonus()}")  
        print("-" * 30)
