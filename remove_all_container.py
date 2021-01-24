#!user/bin/python

import os
import subprocess
import env

env_object = env.MyEnv()
cmd_rm_ansible_container = [
    'docker', 'rm', '-f', 'ans'
]
cmd_rm_apache2_container = [
    'docker', 'rm', '-f', 'web'
]
cmd_rm_mariadb_container = [
    'docker', 'rm', '-f', 'db'
]
cmd_rmi_ansible_image = [
    'docker', 'rmi', 'ansible'
]
cmd_rmi_apache2_image = [
    'docker', 'rmi', 'apache2'
]
cmd_rmi_mariadb_image = [
    'docker', 'rmi', 'mariadb'
]
cmd_rm_macvlan_network = [
    'docker', 'network', 'rm', 'macvlan'
]
rm_wordpress_data = [
    "rm", "wordpress.tar.gz"
]

ansible_containaer_path = './docker_file/ansible/'
root_path = '../../'

subprocess.run(cmd_rm_ansible_container)
subprocess.run(cmd_rm_apache2_container)
subprocess.run(cmd_rm_mariadb_container)
subprocess.run(cmd_rmi_ansible_image)
subprocess.run(cmd_rmi_apache2_image)
subprocess.run(cmd_rmi_mariadb_image)
subprocess.run(cmd_rm_macvlan_network)
os.chdir(ansible_containaer_path)
subprocess.run(rm_wordpress_data)
os.chdir(root_path)
