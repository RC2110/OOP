class User:
    def __init__(self, name, birthyear):
        self.name = name
        self.birthyear = birthyear


    def get_name(self):
        return self.name.upper()
        pass

    def age(self, current_year):
        return current_year - self.birthyear
        pass

traveler =User("john", 1991)
get = traveler.age(2023)
get2 = traveler.get_name()
print(get)
print(get2)


