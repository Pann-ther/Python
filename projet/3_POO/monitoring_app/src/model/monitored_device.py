import random
class MonitoredDevice:
    # Pour avoir un compteur commun a tout les appareils du parc
    id = 1

    def __init__(self, name, ip, location,status,state, cpu_usage, id=None):
        self.id = MonitoredDevice.id
        MonitoredDevice.id += 1
        self.name = name
        self.ip = ip
        self.location = location
        self.is_on = status
        self.is_physical = state
        self.cpu_usage = cpu_usage

    # Getters
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_ip(self):
        return self.ip
    
    def get_location(self):
        return self.location
    
    def get_is_on(self):
        return self.is_on
    
    def get_is_physical(self):
        return self.is_physical
    
    def get_cpu_usage(self):
        return self.cpu_usage

    # Setters
    def set_name(self,name):
        self.name = name

    def set_ip(self,ip):
        self.ip = ip

    def set_location(self,location):
        self.location = location

    def set_is_on(self,status):
        self.is_on = status

    def set_is_physical(self,state):
        self.is_physical = state
    
    def set_cpu_usage(self,usage):
        self.cpu_usage = usage

    # Gestion de l'actualisation des valaurs dynamiques des appareils
    def generate_random_value(self,min_var,max_var,value):
        variation = random.uniform(min_var,max_var)
        return value + variation
    
    def update_cpu_usage(self):
        new_value = self.generate_random_value(20,20,self.get_cpu_usage())
        self.cpu_usage = max(0, min(100,new_value))

   
    