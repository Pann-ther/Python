import supervision_module

class Serveur: 
    id = 1
    
    def __init__(self,  name, is_physical_server, mac_list, os, state, cpu_usage, ram_usage, total_storage, used_storage, running_service, id=None):
        self.id = Serveur.id
        Serveur.id += 1
        self.name = name
        self.is_physical_server = is_physical_server
        self.mac_list = []
        self.mac_list.append(mac_list)
        self.os = os
        self.state = state
        self.cpu_usage = cpu_usage
        self.ram_usage = ram_usage
        self.total_storage = total_storage
        self.used_storage = used_storage
        self.running_service = running_service
        
    #getters
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name 
    
    def get_is_physical_server(self):
        if self.is_physical_server:
            return True
        else:
            return False
    
    def get_mac_list(self):
        return self.mac_list
    
    def get_os(self):
        return self.os
    
    def get_state(self):
        return self.state
    
    def get_cpu_usage(self):
        return self.cpu_usage
    
    def get_ram_usage(self):
        return self.ram_usage
    
    def get_total_storage(self):
        return self.total_storage
    
    def get_used_storage(self):
        return self.used_storage
    
    def get_running_service(self):
        return self.running_service
    
    
    #setters
    def set_is_physical_server(self,type):
        self.is_physical_server = type
        
    def set_mac_list(self, mac):
        self.mac_list.append(mac)
        
    def set_state(self, state):
        self.state = state
        
    def set_cpu_usage(self, usage):
        self.cpu_usage = usage
    
    def set_ram_usage(self, usage):
        self.ram_usage = usage
    
    def set_total_storage(self,total):
        self.total_storage = total
        
    def set_used_storage(self,utilise):
        self.used_storage = utilise
        
    def set_running_service(self,services):
        self.running_service = services
        
    #methodes
    
    def demarrer(self):
        self.state = True
        
    def eteindre(self):
        self.state = False
        
    def __str__(self):
        return f"Serveur {self.name}, ID: {self.id}, OS: {self.os}, Etat: {'On' if self.state else 'Off'}"
    
    
srv1 = Serveur("ADDS","VM","00:11:22:33:44:55","WS2025",True,10,50,1900,500,"Active Directory") 
list_srv = supervision_module.Supervision()
list_srv.add_server(srv1)
print(list_srv.full_display())
print(srv1.get_id())
