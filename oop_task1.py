class Texnika:
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type

    def info(self):
        print(f"Brendi: {self.brand}\nModeli: {self.model}\nTuri: {self.type}")


class Notebooks(Texnika):
    def __init__(self, video_card, ram, display, brand, model, type):
        super().__init__(brand, model, type)
        self.video_card = video_card
        self.ram = ram
        self.display = display

    def notebook_info(self):
        print(f"Brendi: {self.brand}\nModeli: {self.model}\nTuri: {self.type}\nVideo Card{self.video_card} GB\nRam "
              f"{self.ram}\nDisplay {self.display} Hz")


# note = Notebooks(4, 32, 144, "Xbrend", "Xmodel", "Xtype")
# print(note.notebook_info())


class Television(Texnika):
    def __init__(self, size, display, brand, model, type):
        super().__init__(brand, model, type)
        self.size = size
        self.display = display

    def tv_info(self):
        print(f"Brendi: {self.brand}\nModeli: {self.model}\nTuri: {self.type}\nSize: "
              f"{self.size}\nDisplay: {self.display} Hz")


# tv = Television(32, 144, "Xbrend", "Xmodel", "Xtype")
# print(tv.tv_info())


class Smartphones(Texnika):
    def __init__(self, brend, model, type, size, sim_count):
        super().__init__(brend, model, type)
        self.size = size
        self.sim_count = sim_count

    def phone_info(self):
        print(f"Brendi: {self.brand}\nModeli: {self.model}\nTuri: {self.type}\nSize: "
              f"{self.size}\nSim_count: {self.sim_count}")


phone = Smartphones("Xbrend", "Xmodel", "Xtype", 32, 2)
print(phone.phone_info())