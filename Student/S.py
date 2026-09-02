class CSStudent:
    stream = 'cse'            
    def __init__(self, roll):
        self.roll = roll    
    def setAddress(self, address):
        self.address = address  
    def getAddress(self):   
        return self.address  
add = CSStudent(101)
add.setAddress("Surat,Gujarat")
print(add.getAddress())  
a = CSStudent(20)
b = CSStudent(21)
print(a.stream)
print(b.stream)
print(a.roll)
print(CSStudent.stream)