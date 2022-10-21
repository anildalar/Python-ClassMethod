class Person:
    #1. Property
    age=25
    #2. Constructor
    
    #3. Method
    def printAge(self):
        print("The age is : ", self.age)
        
        
    def printAge2(cls):
        print("The age is : ", cls.age)
    
    #4. Nested Class
    
    
#person = Person();

#person.printAge();
#Person.printAge2()
Person.printAge2 = classmethod(Person.printAge2)
Person.printAge2()