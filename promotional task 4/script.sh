
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
