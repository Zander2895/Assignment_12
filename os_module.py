import os

def list_directory_contents(path):
    try:
        if not os.path.exists(path):
            print(f"Error: The path '{path}' does not exist.")
            return
    
        if not os.path.isdir(path):
            print(f"Error: The path '{path}' is not a directory.")
            return
        
        contents = os.listdir(path)
        
        if not contents:
            print(f"The directory '{path}' is empty.")
        else:
            print(f"Contents of the directory '{path}':")
            for item in contents:
                item_path = os.path.join(path, item)
                if os.path.isdir(item_path):
                    print(f"Directory: {item}")
                else:
                    print(f"File: {item}")
    
    except PermissionError:
        print(f"Error: You do not have permission to access '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Prompt the user for the directory path
    path = input("Enter the directory path: ")
    list_directory_contents(path)

if __name__ == "__main__":
    main()
