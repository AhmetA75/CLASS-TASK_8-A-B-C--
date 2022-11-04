class Animals ():
    
    def __init__(self, name, age, legs,tail, horns ):
        print("This is the init function of the animals class.")
        self.name = name
        self.age = age
        self.legs = legs
        self.tail = tail
        self.horns = horns
    


    def change_name(self,new_name):
        self.name = new_name

    def add_age(self,age):
        self.age.append(age)
    
    def show_info(self):
        print("This is the animals class.")

        print("Name: {}\nAge: {}\nLegs: {}\nTail: {}\nHorns: {}\n".format(self.name,self.age,self.legs,self.tail,self.horns))

class Orkinos(Animals):
    def __init__(self, name, age, legs,tail, horns, color, ):
        print("This is the init function of the Orkinos class.")
       
        self.color = color
        super().__init__(name, age, legs,tail, horns)
       

    def change_2(self, fins):
        self.legs=fins
    def change_1(self, new_color):
        self.color = new_color

    def show_info(self):
        print("This is the Orkinos class.")

        print("Name: {}\nAge: {}\nLegs: {}\nTail: {}\nHorns: {}\nColor:{}\n".format(self.name,self.age,self.legs,self.tail,self.horns,self.color))



orkinos=Orkinos("orkinos", 7 , False , True , False   , "blue")
orkinos.change_1("black")
orkinos.change_2("fins")

orkinos.show_info()

