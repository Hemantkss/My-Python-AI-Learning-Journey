"""
File Handling
"""

# p = open(r"class8.py")
# print(p.read())

# a = open("hemant.txt", "w")
# a.write("Hello Hemant\n")
# a.write("Hello Hemant\n")
# a.close()

# a = open("hemant.txt", "x")


from pathlib import Path
def readFilesAndFolder():
    path = Path("")
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {item}")


# Craete File
def create_file():
    try:
        readFilesAndFolder()
        name = input("Enter File Name: ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                date = input("Enter Date: ")
                fs.write(date)
            print(f"File Created: {p}") 
        else:
            print(f"File Already Exist: {p}")       
        
    except Exception as err:
        print(f"File Already Exist: {err}")
        
# Read File
def read_file():
    try:
        readFilesAndFolder()
        name = input("Enter File Name: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r") as fs:
                data = fs.read()
                print(data)
            print(f"File Read: {p}")
        else:
            print(f"File Not Found: {p}")
    except Exception as err:
        print(f"File Not Found: {err}")
   
# Update File
def update_file():
    try:
        readFilesAndFolder()
        name = input("Enter File Name: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of file")
            print("Press 2 for changing the content of file")
            print("Press 3 for appending the content of file")
            check = int(input("Enter Your Choice: "))
            if(check == 1):
                new_name = input("Enter New File Name: ")
                p.rename(new_name)
                print(f"File Renamed: {new_name}")
            elif(check == 2):
                with open(p, "w") as fs:
                    data = input("Enter Data: ")
                    fs.write(data)
                print(f"File Updated: {p}")
            elif(check == 3):
                with open(p, "a") as fs:
                    data = input("Enter Data: ")
                    fs.write(data)
                print(f"File Updated: {p}")
            else:
                print("Invalid Choice")
        elif p.exists() and p.is_dir():
            print("You can not update directory")
        elif p.exists() and not p.is_file():
            print("You can not update directory")
        elif not p.exists():
            print("File Not Found")
    except Exception as err:
        print(f"File Not Found: {err}")
   
# Delete File
def delete_file():
    try:
        readFilesAndFolder()
        name = input("Enter File Name: ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print(f"File Deleted: {p}")
        elif p.exists() and p.is_dir():
            p.rmdir()
            print(f"Directory Deleted: {p}")
        elif not p.exists():
            print("File Not Found")
    except Exception as err:
        print(f"File Not Found: {err}")
        
              
    
print("Press 1 for Create file")
print("Press 2 for Read file")
print("Press 3 for update file")
print("Press 4 for Delete file")

check = int(input("Enter Your Choice: "))
if(check == 1):
    create_file()
if(check == 2):
    read_file()
if(check == 3):
    update_file()
if(check == 4):
    delete_file()

    
    


