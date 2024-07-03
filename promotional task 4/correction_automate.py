import os
import subprocess

# Function to run a shell command
def run_command(command):
    try:
        sp = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = sp.communicate()
        if sp.returncode != 0:
            print(f"Error: {stderr}")
        else:
            print(f"Output: {stdout}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to create groups
def create_groups(groups):
    for group in groups:
        run_command(f"groupadd {group}")

# Function to create users and assign them to groups
def create_users(users):
    for user, group in users.items():
        run_command(f"useradd -m -g {group} {user}")

# Function to create directories and set ownership
def create_directories(directories):
    for directory, ownership in directories.items():
        os.makedirs(directory, exist_ok=True)
        run_command(f"chown root:{ownership} {directory}")

def main():
    # Define groups, users, and directories
    groups = ["System_Administrator", "Legal", "Human_Resource_Manager", "Sales_Manager", "Business_Strategist", "CEO", "IT_intern", "Finance_Manager"]
    users = {
        "Andrew": "System_Administrator",
        "Julius": "Legal",
        "Chizi": "Human_Resource_Manager",
        "Jeniffer": "Sales_Manager",
        "Adeola": "Business_Strategist",
        "Bach": "CEO",
        "Gozie": "IT_intern",
        "Ogochukwu": "Finance_Manager"
    }
    directories = {
        "/Company/Finance_Budgets": "root",
        "/Company/Contract_Documents": "Legal",
        "/Company/Business_Projections": "Business_Strategist",
        "/Company/Business_Models": "Sales_Manager",
        "/Company/Employee_Data": "Human_Resource_Manager",
        "/Company/Company_Vision_and_Mission_Statement": "root",
        "/Company/Server_Configuration_Script": "System_Administrator"
    }

    # Create groups
    create_groups(groups)

    # Create users and assign to groups
    create_users(users)

    # Create directories and set ownership
    create_directories(directories)

if __name__ == "__main__":
    main()
