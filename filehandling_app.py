class Student():
    def __init__(self, name, surname, grade, letter, id):
        self.name = name
        self.surname = surname
        self.grade = grade
        self.letter = letter
        self.id = id
    
    def writeFile(self):
        filename = self.id + ".txt"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"ID: {self.id}\nName: {self.name}\nSurname: {self.surname}\nGrade: {self.grade}\nLetter: {self.letter}")
        print("==> Record successfully created! <==\n")

class Process():
    def __init__(self):
        self.choice = None
    
    def displayMenu(self):
        menu = {
            "1" : "Enter new record",
            "2" : "Read a record",
            "3" : "Exit"
        }
        options = menu.keys()
        print(" MAIN MENU ".center(100, "="))
        print("What'd you like to do?\n")
        for entry in options:
            print(entry + "- " + menu[entry])
        
        self.checkSelection()
    
    def checkSelection(self):        
        try:
            self.choice = input("Your choice: ")
            if not ((self.choice == "1") or (self.choice == "2") or (self.choice == "3")):
                raise Exception("Please provide a valid choice (1, 2 or 3): ")
        except Exception as e:
            print(e)
            self.checkSelection()
        else:
            self.makeChoice(self.choice)    
    
    def makeChoice(self, selection):
        if selection == "1":
            self.newRecord()
        elif selection == "2":
            self.readRecord()
        elif selection == "3":
            print("Exitting...")
            import sys
            sys.exit()
    
    def determineLetter(self, point):
        if (point >= 0) and (point < 45):
            return "F"
        elif (point >= 45) and (point < 60):
            return "D"
        elif (point >= 60) and (point < 70):
            return "C"
        elif (point >= 70) and (point < 80):
            return "B"
        elif (point >= 80) and (point <= 100):
            return "A"
    
    def newRecord(self):
        while True:             # Taking user input as StdID and checking if valid
            try:
                id_int = int(input("Enter student ID: "))
                id_str = str(id_int)
                id_length = 6
                if not len(id_str) == id_length:
                    raise Exception("ID length must be 6 characters!")
            except ValueError:
                print("ID must be numerical!")
            except Exception as e:
                print(e)
            else:
                break
        
        while True:             # Taking user input as name and checking if valid
            try:
                import re
                name = input("Enter student name: ")
                if re.search("""['"@_!#$%^&*()<>?/\|}{~:]""", name):
                    raise Exception("The name cannot contain any special characters!")
                elif len(name) > 20:
                    raise Exception("Length of the name cannot be more than 20 characters!")
                elif re.search("[0-9]", name):
                    raise Exception("The name cannot contain any numerical characters!")
            except Exception as e:
                print(e)
            else:
                break
        
        while True:             # Taking user input as surname and checking if valid
            try:
                import re
                surname = input("Enter student surname: ")
                if re.search("""['"@_!#$%^&*()<>?/\|}{~:]""", surname):
                    raise Exception("The surname cannot contain any special characters!")
                elif len(surname) > 20:
                    raise Exception("Length of the surname cannot be more than 20 characters!")
                elif re.search("[0-9]", surname):
                    raise Exception("The surname cannot contain any numerical characters!")
            except Exception as e:
                print(e)
            else:
                break    
        
        while True:             # Taking user input as grade and checking if valid
            try:
                grade = int(input("Enter student grade: "))
                if not ((grade >= 0) and (grade <= 100)):
                    raise Exception("Invalid input! The grade value must be between 0 - 100!")
            except ValueError:
                print("The grade value must be numerical!")
            except Exception as e:
                print(e)
            else:
                letter = self.determineLetter(grade)
                break
        
        try:
            locals()[id_str] = Student(name, surname, grade, letter, id_str)     # Creating object
            locals()[id_str].writeFile()
            self.backtoMenu()
        except Exception:
            print("An error occured! Program terminating...")
            import sys
            sys.exit()
    
    def readRecord(self):
        while True:             # Taking user input as StdID and checking if valid
            try:
                id_int = int(input("Enter student ID: "))
                id_str = str(id_int)
                id_length = 6
                if not len(id_str) == id_length:
                    raise Exception("ID length must be 6 characters!")
            except ValueError:
                print("ID must be numerical!")
            except Exception as e:
                print(e)
            else:
                break
        print(" RECORD ".center(100, "="))
        filename = id_str + ".txt"
        
        try:
            with open(filename, "r", encoding = "utf-8") as file:
                print(file.read())
        except Exception:
            print("No records found!")
        finally:
            self.backtoMenu()
    
    def backtoMenu(self):
        select = input("\nDo you want to return to main menu? (y/n): ")
        if select == "y" or select == "Y":
            self.displayMenu()
        elif select == "n" or select == "N":
            import sys
            print("Exitting...")
            sys.exit()
        else:
            print("Invalid selection! Please make a valid choice, y or n !")
            self.backtoMenu()

q = Process()

q.displayMenu()