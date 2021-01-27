#!user/bin/python

class MyEnv:
    """
    """
    def __init__(self):
        self.my_env = {
            "subnet": "<your_lab_subnet/mask>",
            "gateway": "<your_lab_gateway_ip_address>",
            "ansible_addr": "<ansible_container_ip_address>",
            "web_addr": "<wev_container_ip_address>",
            "db_addr": "<db_container_ip_address>",
            "phsical_nic": "<NIC name of docker host>"
        }
