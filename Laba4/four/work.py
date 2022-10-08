class Worker:
    def __init__(self, name, id, age):
        self.__name = name
        self.__id = id
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def id(self):
        return self.__id

    @property
    def age(self):
        return self.__age

    @name.setter
    def name(self, name):
        if name == "":
            self.__name = "None"
        else:
            self.__name = name

    @id.setter
    def id(self, id):
        if id == "":
            self.id = "None"
        else:
            self.__id = id

    @age.setter
    def age(self, age):
        if age <= 18:
            self.__age = 18
        elif age > 60:
            self.__age = 60
        else:
            self.__age = age

    def __str__(self):
        return f"{self.__name:<15} {self.__id:<10} {self.__age:<3}"


# worker = Worker("Maks", "45fd8e8f", 19)
# print(worker)
# worker.id = ""
# worker.name = ""
# worker.age = 98
# print(worker)

