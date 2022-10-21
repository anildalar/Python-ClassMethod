class Person:
    age=30
    
    @classmethod
    def showAge(cls):
        print("The age is : ",cls.age)
        
        
Person.showAge()
