class cat:
    name="def"
    age=None
    happy=True
    def __init__(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
    def set_data(self,his_name,hes_age):
        self.name=his_name
        self.age=hes_age
    def get_data(self):
        print(self.name,self.age,self.color)    
cat1=cat("ads",5,"red")
cat1.get_data()

   