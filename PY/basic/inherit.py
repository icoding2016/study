
'''
Note:

  - For a derived class C(A, B), the order or A/B DOES matter.

'''

from unittest import mock


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

    def SuperSwim(self):
        print("Start Super-Swim, the enhanced swimming ability.")

class Mermaid3(Mammal, Fish):

    defaultName = "A Mermaid"

    def Sing(self):
        print("The mermaid sings with a touching voice.")
    
    def SuperClimb(self):        
        print("Start Super-Cimb, the enhanced climbing ability.")
        

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

    # mock.create_autospec
    mockMermaid = mock.create_autospec(Mermaid2, spec_set=True)
    mockMermaid.SuperSwim.return_value = "Fake SuperSwim" 
    mockMermaid.SuperSwim()
    mockMermaid.SuperClimb.return_value = "Fake SuperClimb"      # exception will raise
    mockMermaid.SuperClimb()
