class laptop :
    def __init__(self,name,owner):
        self.name = name
        self.owner = owner
        
        
        
    def user(self):
        print(f"this  laptop is {self.name} {self.owner}.")
 #object defines below      
laptop1=laptop("hp","avi")
laptop1.user()
#An object is an instance of a class. When a class is defined, no memory is allocated until an object is created.