
import src.model.server as srv

def test_initialisation():
    srv1 = srv.Server("ADDS","192.168.100.1","Paris", True, True, 20, 50, 40)
    assert srv1.get_name() == "ADDS"
    assert srv1.get_is_physical() == True
    assert srv1.get_cpu_usage() == 20

def test_setters():
    srv1 = srv.Server("ADDS","192.168.100.1","Paris", True, True, 20, 50, 40)
    srv1.set_cpu_usage(25)
    assert srv1.get_cpu_usage() == 25
    
def test_update_all():
    srv1 = srv.Server("ADDS","192.168.100.1","Paris", True, True, 20, 50, 40)
    srv1.update_all() 
    assert srv1.get_cpu_usage() != 20
    assert srv1.get_ram_usage() != 50
    assert srv1.get_disk_usage() != 40

