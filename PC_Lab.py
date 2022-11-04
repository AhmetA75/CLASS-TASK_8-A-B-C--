class PC_Lab():
    def __init__(self, lab_name,pc_count, pc_list, lab_manager, lab_assistant):
        self._lab_name = lab_name
        self._pc_list = pc_list
        self._lab_manager = lab_manager
        self._lab_asistant=lab_assistant
        self._pc_count = pc_count

    def prnt_lab_name(self):
        print(self._lab_name)
    def add_pc(self,pc):
         self._pc_list.append(pc)
         self._pc_count += 1


    def add_name(self,name):
        self._lab_name.append(name)


    def add_name_manager(self,name):
        self._lab_manager.append(name)

    def add_name_asistant(self,name):
        self._lab_asistant.append(name)

    def show_info(self):    
        print("Lab Name: {}\nPC Count: {}\npc_list{}\nLab Manager: {}\nLab Assistant: {}\n".format(self._lab_name,self._pc_count,self._pc_list,self._lab_manager,self._lab_asistant))

    def show_pc_list(self):
        for pc in self._pc_list:
            print(pc)
pc_lab=PC_Lab([],3,["pc1","pc2","pc3"],[],[])
pc_lab.show_info()

   
    

pc_lab.add_pc("pc4")
pc_lab.show_info()

print(pc_lab._lab_asistant)
pc_lab.add_name("veli")
pc_lab.add_name_manager("Ahmet")
pc_lab.add_name_asistant("Veli")
pc_lab.add_pc("pc5")
pc_lab.show_info()