import src.model.network_device as dv

def test_initialisation():
    dv1 = dv.NetworkDevice("FORTI","192.168.100.1","Paris",True,True,20,5,500)
    assert dv1.get_is_physical() == True
    assert dv1.get_is_on() == True
    assert dv1.get_ip() == "192.168.100.1"
    
def test_setters():
    dv1 = dv.NetworkDevice("FORTI","192.168.100.1","Paris",True,True,20,5,500)
    dv1.set_location("Bussy")
    dv1.get_location() == "Bussy"

def test_update_all():
    dv1 = dv.NetworkDevice("FORTI","192.168.100.1","Paris",True,True,20,5,500)
    dv1.update_all()
    assert dv1.get_bandwidth_usage() != 500
    assert dv1.get_latency() != 5
    assert dv1.get_cpu_usage() != 20