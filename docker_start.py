#!user/bin/python

import os
import subprocess
import time
import env

env_object = env.MyEnv()

cmd_get_wordpress_latest = [
    "wget", "https://wordpress.org/latest.tar.gz"
]

cmd_mv_wordpress_latest = [
    "mv", "latest.tar.gz", "./docker_file/ansible/"
]

cmd_create_macvlan = [
    "docker", "network", "create", "-d", "macvlan",
    "--subnet={0}".format(env_object.my_env["subnet"]),
    "--gateway={0}".format(env_object.my_env["gateway"]),
    "-o", "parent={0}".format(env_object.my_env["phsical_nic"]),
    "macvlan"
]
tar_ansible_file = [
    "tar", "-zcvf", "./docker_file/ansible/latest-ja.tar.gz",
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

inventory_path = './wordpress/inventory'
db_defaults_path = './wordpress/roles/mysql/defaults/main.yml'
ansible_containaer_path = './docker_file/ansible/'
web_container_path = './docker_file/web/'
db_container_path = './docker_file/db/'
root_path = '../../'

inventory = {
    "[web]" : env_object.my_env["web_addr"],
    "[db]" : env_object.my_env["db_addr"]
}
defaults = {
    "mysql_password" : env_object.my_env["db_password"],
}

with open(inventory_path, mode="w") as f:
    f.write(f'[web]\n{inventory["[web]"]}\n')
    f.write(f'[db]\n{inventory["[db]"]}\n')
with open(db_defaults_path, mode="w") as f:
    f.write('---\n')
    f.write(f'mysql_password: {defaults["mysql_password"]}\n')

subprocess.run(cmd_get_wordpress_latest)
subprocess.run(cmd_mv_wordpress_latest)
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
