# Создать класс Country: Столица, Площадь, Численность населения.
# Создать список объектов. Вывести:
# a) список стран по заданной площади;
# b) список стран по заданной численности населения. – 3 балла


class Country:
    def __init__(self, name, capital, square, population):
        self.__name = name
        self.__capital = capital
        self.__square = square
        self.__population = population

    @property
    def name(self):
        return self.__name

    @property
    def capital(self):
        return self.__capital

    @property
    def square(self):
        return self.__square

    @property
    def population(self):
        return self.__population

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            self.__name = "None"
        else:
            self.__name = new_name

    @capital.setter
    def capital(self, new_capital):
        if not isinstance(new_capital, str):
            self.__capital = "None"
        else:
            self.__capital = new_capital

    @square.setter
    def square(self, new_square):
        if not isinstance(new_square, float) or new_square <= 0:
            self.__square = "None"
        else:
            self.__square = new_square

    @population.setter
    def population(self, new_population):
        if not (isinstance(new_population, float) or isinstance(new_population, int)) or new_population <= 0:
            self.__population = "None"
        else:
            self.__population = new_population

    def __str__(self):
        return f"{self.name:<15} {self.capital:<12} {self.square:<9} {self.population:<9}"


list_of_country = [Country("Belarus", "Minsk", 388.8, 1_975_000),
                   Country("Spain", "Madrid", 604.3, 3_223_000),
                   Country("The USA", "Washington", 177, 701_974),
                   Country("Brazil", "Brasilia", 480.8, 4_291_0000),
                   Country("Pakistan", "Islamabad", 220, 1_009_000)
                   ]

square = float(input("Enter square: "))
flag = False
for country in list_of_country:
    if country.square > square:
        if not flag:
            print("List of country with square more than %d\n" % square)
            print("{:<15} {:<12} {:<9} {:<9}".format("Country", "Capital", "Square", "Population"))
            print("-------------------------------------------------")
            flag = True
        print(country)
if not flag:
    print("We haven't found such country")

population = float(input("Enter population: "))
flag = False
for country in list_of_country:
    if country.population > population:
        if not flag:
            print("List of country with population more than %d\n" % population)
            print("{:<15} {:<12} {:<9} {:<9}".format("Country", "Capital", "Square", "Population"))
            print("-------------------------------------------------")
            flag = True
        print(country)
if not flag:
    print("We haven't found such country")
