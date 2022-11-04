class Animals ():
    
    def __init__(self, name, age, legs,tail, horns ):
        print("This is the init function of the animals class.")
        self.name = name
        self.age = age
        self.legs = legs
        self.tail = tail
        self.horns = horns
    
    def show_info(self):
        print("This is the animals class.")

        print("Name: {}\nAge: {}\nLegs: {}\nTail: {}\nHorns: {}\n".format(self.name,self.age,self.legs,self.tail,self.horns))

class Dinosaur(Animals):
    def __init__(self, name, age, legs,tail, horns, color, ):
        print("This is the init function of the dinosaur class.")

       
        self.color = color
        
        super().__init__(name, age, legs,tail, horns)
    def change(self,dinosaur_thorns):
        self.horns = dinosaur_thorns 

    def change(self,new_color):
        self.color = new_color
        
    def show_info(self):
        print("This is the dinosaur class.")
       

        print("Name: {}\nAge: {}\nLegs: {}\nTail: {}\nHorns: {}\nColor:{}\n".format(self.name,self.age,self.legs,self.tail,self.horns,self.color))


dinosaur=Dinosaur("T-Rex", 35, 4, True, 2, "Red")
dinosaur.show_info()
    




