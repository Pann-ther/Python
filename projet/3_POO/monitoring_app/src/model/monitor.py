class Monitor:
    def __init__(self, servers_list, network_devices_list):
        self.servers_list = []
        self.network_devices_list = []
      
    #  Gestion du monitoring des appareils
    def add_server(self, server):
        for s in self.servers_list:
            if s.get_id() == server.get_id():
                print(f"{server.get_name()} a deja ete ajouté")
                return
        self.servers_list.append(server)
        print(f"{server.get_name()} a bien été ajouté")
        
    def remove_server(self, server_name):
        for s in self.servers_list:
            if server_name == s.get_name():
                self.servers_list.remove(s)
                print(f"{server_name} a bien été supprimé")
                return
        print(f"{server_name} n'a pas été trouvé")
            
        
    def add_network_device(self, device):
        for n in self.network_devices_list:
            if n.get_id() == device.get_id():
                print(f"{device.get_name()} a deja été ajouté")
                return
        self.network_devices_list.append(device)
        print(f"{device.get_name()} a bien été ajouté")
            
    def remove_network_device(self, device_name):
        for n in self.network_devices_list:
            if n.get_name() == device_name:
                self.network_devices_list.remove(n)
                print(f"{device_name} a bien été supprimé")
                return
        print(f"{device_name} n'a pas été trouvé ")
            
    # Affichage des appareils monitorés
    def display_servers(self):
        if not self.servers_list:
            print("Aucun serveur n'est monitoré")
        else:
            print("----------Serveur-------------")
            for s in self.servers_list:
                print(s.__str__())
                
    def display_network_devices(self):
        if not self.network_devices_list:
            print("Aucun appareil reseau n'est monitoré")
        else:
            for n in self.network_devices_list:
                print("----------Appareils reseau----------")
                print(n.__str__())
    
    def display_all(self):
        Monitor.display_servers()
        Monitor.display_network_devices()
            
    
    # raffrechissemrnts des valaeurs dynamiques des appareils
    def updates_all(self):
        for s in self.servers_list:
            s.update_all()
        for n in self.network_devices_list:
            n.update_all()