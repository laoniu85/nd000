class Parent():
    def __init__(self,name,eye_color):
        print "Parent custructor called!!!"
        self.name=name
        self.eye_color=eye_color
class Child(Parent):
    def __init__(self,name,eye_color,number_toys):
        print "Child custructor called!!!"
        Parent.__init__(self,name,eye_color)
        self.number_toys=number_toys

billy=Parent("billy","blue")
shit=Child("shit","shit",2)

print billy.name
print shit.number_toys
