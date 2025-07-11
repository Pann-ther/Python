import src.model.monitored_device as md
class NetworkDevice(md.MonitoredDevice):
    def __init__(self, name, ip, location, status, state, cpu_usage, latency, bandwidth_usage, id=None):
        super().__init__(name, ip, location, status, state, cpu_usage, id)
        self.latency = latency
        self.bandwidth_usage = bandwidth_usage
        
    # Getters
    def get_latency(self):
        return self.latency
    
    def get_bandwidth_usage(self):
        return self.bandwidth_usage
    
    # Setters
    def set_latency(self, latency):
        self.latency = latency
        
    def set_bandwidth_usage(self, bandwidth):
        self.bandwidth_usage = bandwidth
        
    # Gestion de l'actualisation des valeurs dynamiques  
    def update_latency(self):
        new_value = self.generate_random_value(-10,10,self.get_latency())
        self.latency = max(0,min(100,new_value))
        
    def update_bandwidth_usage(self):
        new_value = self.generate_random_value(-20,20,self.get_bandwidth_usage())
        self.bandwidth_usage = max(0,min(100,new_value))
        
    def update_all(self):
        self.update_cpu_usage()
        self.update_latency()
        self.update_bandwidth_usage()
    
    