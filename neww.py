class Tiger:
    def __init__(self, gender, origin):
        self.gender=gender
        self.origin=origin

    def roar(self):
        print("hrrerr hoor")

# overriding the parent method in inheritance

class Bigcats(Tiger):
    def huntingbeaviour(self):
        ab = self.gender + self.origin
        print(ab)
        return ab

    def roar(self):
        print("krrr..howrrrrkkrr")


cub=Tiger("male", "Sundarban")
cub.roar()
animal=Bigcats("Female", "Bengal")
print(animal.origin)
print(animal.gender)
animal.huntingbeaviour()
animal.roar()
