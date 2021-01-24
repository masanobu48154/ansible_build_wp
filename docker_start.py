#!user/bin/python

import os
import subprocess
import time
import env

env_object = env.MyEnv()

cmd_create_macvlan = [
    "docker", "network", "create", "-d", "macvlan",
    "--subnet={0}".format(env_object.my_env["subnet"]),
    "--gateway={0}".format(env_object.my_env["gateway"]),
    "-o", "parent={0}".format(env_object.my_env["phsical_nic"]),
    "macvlan"
]
tar_ansible_file = [
    "tar", "-zcvf", "./docker_file/ansible/wordpress.tar.gz",
    "wordpress/"
]
cmd_build_ansible_container = [
    "docker", "build", "-t", "ansible", "."
]
cmd_build_web_container = [
    "docker", "build", "-t", "apache2", "."
]
cmd_build_db_container = [
    "docker", "build", "-t", "mariadb", "."
]
cmd_run_snsible_container = [
    "docker", "run", "-it", "-d", "--name", "ans", "--network", "macvlan",
    "--ip", env_object.my_env["ansible_addr"], "ansible"
]
cmd_run_web_container = [
    "docker", "run", "-it", "-d", "--name", "web", "--network", "macvlan",
    "--ip", env_object.my_env["web_addr"], "apache2"
]
cmd_run_db_container = [
    "docker", "run", "-it", "-d", "--name", "db", "--network", "macvlan",
    "--ip", env_object.my_env["db_addr"], "mariadb"
]

ansible_containaer_path = './docker_file/ansible/'
web_container_path = './docker_file/web/'
db_container_path = './docker_file/db/'
root_path = '../../'

subprocess.run(cmd_create_macvlan)
subprocess.run(tar_ansible_file)

os.chdir(ansible_containaer_path)
subprocess.run(cmd_build_ansible_container)
os.chdir(root_path)
os.chdir(web_container_path)
subprocess.run(cmd_build_web_container)
os.chdir(root_path)
os.chdir(db_container_path)
subprocess.run(cmd_build_db_container)
subprocess.run(cmd_run_snsible_container)
subprocess.run(cmd_run_web_container)
subprocess.run(cmd_run_db_container)
