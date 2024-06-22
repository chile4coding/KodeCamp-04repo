import os

company_directories = [
    'Finance_Budgets', 
    'Contract_Documents', 
    'Business_Projections', 
    'Business_Models', 
    'Employee_Data', 
    'Company_Vision_and_Mission_Statement', 
    'Server_Configuration_Script'
]

def create_directory_and_file():
    # Take directory name as input from the user
    directory_name = input("Enter the name of the directory you want to create: ")

    # Take file name as input from the user
    file_name = input("Enter the name of the file you want to create: ")

    # Check if the directory is in the company_directories list
    if directory_name in company_directories:
        # Create the directory if it doesn't exist
        try:
            os.makedirs(directory_name, exist_ok=True)
            print(f"Directory '{directory_name}' created successfully!")
        except Exception as e:
            print(f"Error creating directory '{directory_name}': {e}")
            return
        
        # Create the file in the directory
        file_path = os.path.join(directory_name, file_name)
        try:
            with open(file_path, 'w') as f:
                print(f"File '{file_name}' created successfully in '{directory_name}'.")
        except Exception as e:
            print(f"Error creating file '{file_name}' in directory '{directory_name}': {e}")
    else:
        print(f"Directory '{directory_name}' is not in the company directories list. File not created.")

# Run the function
create_directory_and_file()
