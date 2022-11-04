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

class Deer(Animals):
    def __init__(self, name, age, legs,tail, horns, color, ):
        print("This is the init function of the deer class.")
       
        self.color=color
        super().__init__(name, age, legs,tail, horns)
    def change_1(self,deer_horns):
        self.horns = deer_horns
    def change_2(self,new_color):
        self.color = new_color
    def show_info(self):
        print("This is the deer class.")

        print("Name: {}\nAge: {}\nLegs: {}\nTail: {}\nHorns: {}\nColor:{}\n".format(self.name,self.age,self.legs,self.tail,self.horns,self.color))


deer=Deer("The_Elk", 7 , 4 , True , 2   , "Brown")
deer.show_info()