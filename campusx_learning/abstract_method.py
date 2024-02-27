from abc import ABC, abstractmethod

class BankApp(ABC):
    @abstractmethod
    def security(self):
        pass
    def database(self):
        print("Connected database")
        
    
class MobileApp(BankApp):
    def mobile_demo(self):
        print("mobile_demo_app") 
    def security(self):
        print("mobile_app_security")
        
obj=MobileApp()
obj.mobile_demo()
obj.database()

