import random                                                                                        
                                                                                                     
class Student:                                                                                       
    def __init__(self, name, age):                                                                   
        self.name = name                                                                             
        self.age = age                                                                               
        self.money = 100                                                                             
        self.progress = 20                                                                           
        self.alive = True                                                                            
                                                                                                     
    def work(self):                                                                                   
        self.money += 50                                                                             
        self.progress -= 5                                                                           
                                                                                                     
    def study(self):                                                                                  
        self.progress += 15                                                                          
        self.money -= 10                                                                             
                                                                                                     
    def rest(self):                                                                                   
        self.money -= 20                                                                             
        self.progress -= 2                                                                           
                                                                                                     
    def live(self):                                                                                  
        for day in range(1, 366):                                                                    
            if self.money < 20:                                                                      
                self.work()                                                                          
            elif self.progress < 15:                                                                 
                self.study()                                                                         
            else:                                                                                    
                self.rest()                                                                          
                                                                                                     
            # Перевірка на критичний стан                                                            
            if self.money < 0:                                                                       
                print(f"--- День {day}: {self.name} став банкрутом і кинув навчання. ---")           
                self.alive = False                                                                   
                break                                                                                
                                                                                                     
