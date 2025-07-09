import src.model.monitor as m
import src.model.server as srv
import src.model.network_device as nd

def test_add_and_remove_server():
    m1 = m.Monitor([],[])
    srv1 = srv.Server("ADDS","192.168.100.1","Paris", True, True, 20, 50, 40)
    # Ajout serveur
    m1.add_server(srv1)
    assert len(m1.servers_list) == 1
    
    #Voir si le doublon n'est pas ajouté commme prevu
    m1.add_server
    assert len(m1.servers_list) == 1
    
    # Ajout d'un 2ème serc=veur
    srv2 = srv.Server("DNS","192.168.100.2","Paris", True, True, 20, 50, 40)
    m1.add_server(srv2)
    assert m1.servers_list[1].get_name() == "DNS"
    assert len(m1.servers_list) == 2
    
def test_add_and_remove_network_equipment():
    m1 = m.Monitor([],[])
    # Ajout d'un equipement reseau
    nd1 = nd.NetworkDevice("FORTI1","192.168.100.3","Paris", True, True, 10,20,5,500)
    m1.add_network_device(nd1)
    assert len(m1.network_devices_list) == 1
    
    # Voir si le doublon n'est pas ajouté comme prevu
    m1.add_network_device(nd1)
    assert len(m1.network_devices_list) == 1
    
    #Ajout d'un 2eme serveur
    nd2 = nd.NetworkDevice("FORTI2","192.168.100.4","Paris", True, True, 10,20,5,500)
    m1.add_network_device(nd2)
    assert len(m1.network_devices_list) == 2
    assert m1.network_devices_list[1].get_name() == "FORTI2"
    
def test_update_all():
    m1 = m.Monitor([],[])
    nd1 = nd.NetworkDevice("FORTI1","192.168.100.3","Paris", True, True, 10,20,5,500)
    srv1 = srv.Server("ADDS","192.168.100.1","Paris", True, True, 20, 50, 40)
    m1.add_server(srv1)
    m1.add_network_device(nd1)
    m1.updates_all()
    # Verifie si les valeurs ont bien été mise à jour
    assert m1.servers_list[0].get_cpu_usage() != 20
    assert m1.network_devices_list[0].get_cpu_usage() != 10
    
    