
class Human:

    def __init__(self, name , age):

        self.age = age
        self.name = name





class Profession:

    def __init__(self,type):

        self.type = type
        self.people = []

    def add_people(self, human):

        self.people.append(Human)


ved = Human("ved", 21)

veena = Human("veena",200)

profession1 = Profession("CS")
profession2 = Profession("teacher")


profession1.add_people(ved)
profession2.add_people(veena)

print(profession2.people, profession1.people)




