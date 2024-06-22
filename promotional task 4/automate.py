import os
import subprocess

command = ["vagrant", "init", "ubuntu/focal64"]
command2 = ["vagrant", "up", "automation"]

shell_script_content = """
sudo -i
sudo apt-get update

groupadd System_Administrator
groupadd Legal
groupadd Human_Resource_Manager
groupadd Sales_Manager
groupadd Business_Strategist
groupadd CEO
groupadd IT_intern
groupadd Finance_Manager

useradd -m -g System_Administrator Andrew
useradd -m -g Legal Julius
useradd -m -g Human_Resource_Manager Chizi
useradd -m -g Sales_Manager Jeniffer
useradd -m -g Business_Strategist Adeola
useradd -m -g CEO Bach
useradd -m -g IT_intern Gozie
useradd -m -g Finance_Manager Ogochukwu

mkdir -p /Company/Finance_Budgets
mkdir -p /Company/Contract_Documents
mkdir -p /Company/Business_Projections
mkdir -p /Company/Business_Models
mkdir -p /Company/Employee_Data
mkdir -p /Company/Company_Vision_and_Mission_Statement
mkdir -p /Company/Server_Configuration_Script

chown root:System_Administrator /Company/Server_Configuration_Script
chown root:Legal /Company/Contract_Documents
chown root:Human_Resource_Manager /Company/Employee_Data
chown root:Sales_Manager /Company/Business_Models
chown root:Business_Strategist /Company/Business_Projections
"""

vagrantfile_content = """
Vagrant.configure("2") do |config|
  config.vm.define "automation" do |automation|
    automation.vm.box = "ubuntu/focal64"
    automation.vm.hostname = "automation"
    automation.vm.network "private_network", ip: "192.168.33.10"
    automation.vm.provider "virtualbox" do |vb|
      vb.memory = "1024"
    end
    automation.vm.provision "shell", path: "script.sh"
  end
end
"""

# a sub process  funtion to execute the our commands
def run_subprocess(command):
    try:
        sp = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = sp.communicate()
        if sp.returncode != 0:
            print(f"Error: {stderr}")
        else:
            print(f"Output: {stdout}")
    except Exception as e:
        print(f"An error occurred: {e}")

# initialize vagrant function
def initialize_vagrant():
    run_subprocess(command)

def create_shell_script_to_create_users_and_assign_to_departments():
    with open('script.sh', 'w') as file:
        file.write(shell_script_content)
    os.chmod("script.sh", 0o755)

def add_vagrant_configuration_to_use_shell_script_to_create_users_and_assign_to_departments():
    with open('Vagrantfile', 'w') as file:
        file.write(vagrantfile_content)

def get_vagrant_to_execute_run():
    run_subprocess(command2)


def main():
     initialize_vagrant()
     create_shell_script_to_create_users_and_assign_to_departments()
     add_vagrant_configuration_to_use_shell_script_to_create_users_and_assign_to_departments()
     get_vagrant_to_execute_run()


main()



