import monitored_device as md
class Server(md.MonitoredDevice):
    
    def __init__(self,name, ip, location,status,state, cpu_usage, ram_usage, disk_usage, id=None):
        super().__init__(name,ip,location,status,state,cpu_usage,id=None)
        self.ram_usage = ram_usage
        self.disk_usage = disk_usage
        
    # Getters
    
    def get_ram_usage(self):
        return self.ram_usage
    
    def get_disk_usage(self):
        return self.disk_usage
    
    def get_disk_free(self):
        return self.disk_free
    
    # Setters
    def set_ram_usage(self, usage):
        self.ram_usage = usage
        
    def set_disk_usage(self, usage):
        self.disk_usage = usage
        
    # Gestion de l'actualisation des valeurs dynamiques
    def update_ram_usage(self):
        new_value = md.MonitoredDevice.generate_random_value(-20,20,self.ram_usage())
        self.ram_usage = max(0,min(100,new_value))
        
    def update_disk_usage(self):
        new_value = md.MonitoredDevice.generate_random_value(-2,2,self.disk_usage())
        self.disk_usage = max(0, min(100, new_value))