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

class Eagle(Animals) :
    def __init__(self, name, age, legs,tail, horns, color, ):
        print("This is the init function of the Eagle class.")

    
        self.color = color
        super().__init__(name, age, legs,tail, horns)
    def change(self,eagle_thorns):
        self.horns = eagle_thorns
    def change(self,new_color):
        self.color = new_color
    def show_info(self):
        print("This is the eagle class.")
        print("Name: {}\nAge: {}\nLegs: {}\nTail: {}\nHorns: {}\nColor:{}\n".format(self.name,self.age,self.legs,self.tail,self.horns,self.color))

eagle=Eagle("American_Eagle", 5, 2, True, False, "Black_White")
eagle.show_info()