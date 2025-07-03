class Supervision:
    def __init__(self, servers_list=None, network_equipment_list=None):
        self.servers_list = []
        self.network_equipment_list = []
        
    def add_network_equipment(self,equipment):
        self.network_equipment_list.append(equipment)
        
    def remove_network_equipment(self, equipment_name):
        for e in self.network_equipment_list:
            if e.nom() == equipment_name:
                self.network_equipement_list(e)
                break

    def add_server(self,server):
        self.servers_list.append(server)
        
    def remove_server(self,server_name):
        for s in self.servers_list:
            if s.get_name() == server_name:
                self.servers_list.remove(s)
                break
        
    def full_display(self):
        for n in self.network_equipment_list:
            return n.get_name()
        
        for s in self.servers_list:
            return s.get_name()
        
    
