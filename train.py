# 
class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        
    def GetStatus(self):
        print(f"The name of train is {self.name}")
        print(f"the seats available in the train are {self.seats}")
        
        
    def FareInfo(self):
        print(f"the price of the tickets is: Rs {self.fare}")
        
    
    def BookTicket(self):
        if(self.seats>0):
            print(f"your ticket is booked!......... your seat number is : {self.seats}")
            self.seats = self.seats-1 
        else:
            print("Sorry this train is full:...")
    
    
    def CancelTicket(self,seats):
        pass
    
    
maharaja = Train("maharaja Express: 14520",90,2)
maharaja.GetStatus()
maharaja.BookTicket()
maharaja.BookTicket()
maharaja.BookTicket()
maharaja.GetStatus()
