
class Person():

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


class Relationship:

    def __init__(self, name, relative_name, relationship):
        self.name = name
        self.relative_name = relative_name
        self.relationship = relationship


class Node():
    def __init__(self, person: Person): 
        """
        self.data = data
        self.name = data.name
        self.mother = None
        self.father = None
        self.spouse = None
        self.children = []
        self.siblings = []
        """
        self.person = person
        self.mother = None
        self.father = None
        self.spouse = None
        self.children = set()
        self.siblings = set()

    def add_relationship(self, relationship: Relationship):
        if relationship.relationship == 'Father':
            self.father = relationship.relative_name
        if relationship.relationship == 'Mother':
            self.mother = relationship.relative_name
        if relationship.relationship == 'Married' or relationship.relationship == 'Divorced':
            self.spouse = relationship.relative_name
        if relationship.relationship == 'Offspring':
            self.children.add(relationship.relative_name)
        if relationship.relationship == 'Sibling':
            self.siblings.add(relationship.relative_name)

from typing import List

class Graph:
    def __init__(self):
        self.name_to_person = {}
        self.name_to_nodes = {}


    def make_member(self, person: Person, relationship: Relationship):
        
            if person.name not in self.name_to_person:
                self.name_to_person[person.name] = person
            if person.name not in self.name_to_nodes:
                self.name_to_nodes[person.name] = Node(person)
            
            if relationship.name == person.name:
                self.name_to_nodes[person.name].add_relationship(relationship)

    def displayRelationship(self, name):
        node = self.name_to_nodes[name]
        #for relationship in node.relationships:
            #if mem == name:
        print("For member: " + str(node.person.name) + ". Mother is " + str(node.mother) + ". Father is " + str(node.father)
             + ". Spouse is " + str(node.spouse) + ". Children: " + str(node.children) + ". Siblings: " + str(node.siblings))

    def displayInfo(self, name):
        node = self.name_to_person[name]
        #for relationship in node.relationships:
            #if mem == name:
        print("For member: " + str(node.name) + ". Gender is " + str(node.gender) + ". Age is " + str(node.age))
              
              
class FamilyTree():

    def __init__(self):
        self.graph = Graph()

    def add_family_member(self, persons:List[Person], relationships:List[Relationship]):
        for person in persons:
            for relationship in relationships:
                self.graph.make_member(person, relationship)
                
    def displayInfo(self, name):
        self.graph.displayInfo(name) 
        
    def displayRelationship(self, name):
        self.graph.displayRelationship(name)
        
    def remove_relationship(self, relationship):
        if relationship.relationship == 'Mother':
            self.graph.name_to_nodes[relationship.name].mother = None
        elif relationship.relationship == 'Father':
            self.graph.name_to_nodes[relationship.name].father = None
        elif relationship.relationship == 'Spouse':
            self.graph.name_to_nodes[relationship.name].spouse = None
        elif relationship.relationship == 'Offspring':
            self.graph.name_to_nodes[relationship.name].children.remove(relationship.relative_name)
        elif relationship.relationship == 'sibling':
            self.graph.name_to_nodes[relationship.name].sibling.remove(relationship.relative_name)
            
 
    def data_assortion_check(self, relationships):
        # 1. People can't be the relative of themselves.
        for relationship in relationships:
            if relationship.name == relationship.relative_name and (relationship.relationship == 'Married' or relationship.relationship == 'Divorced'):
                print("A person can not marry themselves.")
                self.remove_relationship(relationship)
            if relationship.name == relationship.relative_name and (relationship.relationship == 'Father' or relationship.relationship == 'Mother'):
                print("A person can not be their own parent.")
                self.remove_relationship(relationship)
            if relationship.name == relationship.relative_name and relationship.relationship == 'Sibling':
                print("A person can not be their own sibling.")
                self.remove_relationship(relationship)
            if relationship.name == relationship.relative_name and relationship.relationship == 'Offspring':
                print("A person can not be their own child.")
                self.remove_relationship(relationship)
        # 2. The relative's gender should be associated with the relationship.

            if relationship.relationship == 'Father' and self.graph.name_to_person[relationship.relative_name].gender == 'F':
                print("A woman can not be someone's father.")
                self.remove_relationship(relationship)
            if relationship.relationship == 'Mother' and self.graph.name_to_person[relationship.relative_name].gender == 'M':
                print("A man can not be someone's mother.")
                self.remove_relationship(relationship)
            
        # 3. The previous generation cannot be younger than the next generation
        
            if (relationship.relationship == 'Offsping' and self.graph.name_to_person[relationship.name].age != None 
                and self.graph.name_to_person[relationship.relative_name].age != None 
                and self.graph.name_to_person[relationship.name].age <= self.graph.name_to_person[relationship.relative_name].age):
            
                print("Parents can not be younger than their children.")
                
                self.remove_relationship(relationship)
            if ((relationship.relationship == 'Father' or relationship.relationship == 'Mother') 
                and self.graph.name_to_person[relationship.relative_name].age != None 
                and self.graph.name_to_person[relationship.name].age >= self.graph.name_to_person[relationship.relative_name].age):
                print("Parents can not be younger than their children.")
                self.remove_relationship(relationship)

       

    def add_person_(self):
        var1 = input("Please enter name: ")
        var2 = input("Please enter gender: ")
        var3 = input("Please enter age: ")
        person1 = Person(var1, var2, var3)
        self.graph.name_to_person[var1]= person1
        

    def add_relationship_(self):
        var1 = input("Please enter name: ")
        var2 = input("Please enter relative name: ")
        var3 = input("Please enter relationship: ")
        relationship1 = Relationship(var1, var2, var3)
        self.graph.name_to_nodes[var1].add_relationship(relationship1)
        self.data_assortion_check([relationship1])

    def modify_info_person(self):
        var1 = input("Please enter person's name you want to make a change: ")
        var2 = input("Please enter the category you want to change: ")
        var3 = input("Please enter new value: ")
       
        if var2 == 'name':
            self.graph.name_to_person[var1].name = var3
        elif var2 == 'gender':
            self.graph.name_to_person[var1].gender = var3
        else:
            self.graph.name_to_person[var1].age = var3
    
    def modify_info_relationship(self):
        
        var1 = input("Please enter person's name you want to make a change: ")
        var2 = input("Please enter the category you want to change: ")
        var3 = input("Please enter the value you want to change: ")
        var4 = input("Please enter new value: ")
    
        if var2 == 'name':
            self.graph.name_to_nodes[var1].name = var4
        elif var2 == 'mother':
            self.graph.name_to_nodes[var1].mother = var4
        elif var2 == 'father':
            self.graph.name_to_nodes[var1].father = var4
        elif var2 == 'spouse':
            self.graph.name_to_nodes[var1].spouse = var4
        elif var2 == 'children':
            self.graph.name_to_nodes[var1].children.remove(var3)
            self.graph.name_to_nodes[var1].children.add(var4)
        elif var2 == 'sibling':
            self.graph.name_to_nodes[var1].sibling.remove(var3)
            self.graph.name_to_nodes[var1].sibling.add(var4)
            

"""
if __name__ == "__main__":
    ft = FamilyTree()
    person = Person('Patrick Earnsha', 'M', None)
    relationships = [
        Relationship('Patrick Earnsha', 'Hannah Earnsha', 'Married'),
        Relationship('Patrick Earnsha', 'bbb Earnsha', 'Father'),
        Relationship('bbb Earnsha', 'Patrick Earnsha', 'Offspring')
    ]
    ft.add_family_member(person, relationships)
    #ft.make_member(['Patrick Earnsha', 'bbbb Earnsha', 'Father', 'M', None])
    #ft.make_member(['lalal Earnsha', 'Catheline Earnsha', 'Offspring', 'F', None])
    ft.displayInfo('Patrick Earnsha')
    #ft.add_family_member(ft.add_person_(), ft.add_relationship_())
    #ft.displayInfo('sss')


"""



