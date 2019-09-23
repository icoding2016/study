
'''
Note:

  - For a derived class C(A, B), the order or A/B DOES matter.

'''

class Creature(object):
    defaultName = "A Creature"
       
    def __init__(self, name=None):
        if name:
            self.name = name
        else:
            self.name = self.defaultName

    def Name(self):
        return self.name
        
    def Type(self):
        return "CREATURE"


class Mammal(Creature):

    defaultName = "A Mammal"
       
    def Type(self):
        return "MAMMAL"

    def Walk(self):
        print("{} walks.".format(self.name))

        
class Fish(Creature):
    
    defaultName = "A Fish"

    def Type(self):
        return "FISH"

    def Swim(self):
        print("{} swims.".format(self.name))
    

class Mermaid(Mammal, Fish):

    def Sing(self):
        print("The mermaid sings with a touching voice.")


class Mermaid2(Fish, Mammal):

    def Sing(self):
        print("The mermaid sings with a touching voice.")
        

class Mermaid3(Fish, Mammal):

    defaultName = "A Mermaid"

    def Sing(self):
        print("The mermaid sings with a touching voice.")
    
        

def test(T):
    if T not in [Mermaid, Mermaid2, Mermaid3]:
        return "Invalid Type"

    mermaid = T()
    print(mermaid.Type())
    print(mermaid.Name())
    mermaid.Swim()
    mermaid.Walk()
    mermaid.Sing()


if __name__ == '__main__':
    test(Mermaid)
    test(Mermaid2)
    test(Mermaid3)
