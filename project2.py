import os
import pandas as pd
from classes import Person, Student, Employee
from enums import Menu
import warnings

def saveNewEntry(users, users_index, personType):
    id = input("Please enter your ID: ").strip()
    if not id.isdigit():
        print("\nInvalid ID. Please enter a numeric ID.")
        return 0
    if int(id) in users_index:
        print(f"\nError: ID already exists: {id}\n")
        return 0
    id = int(id)
    name = input("Please enter your name: ").strip().title()
    if not name:
        print("\nBlank name. Please enter a valid name.")
        return 0
    age = input("Please enter your age: ").strip()
    if not age.isdigit() or int(age) <= 0 or int(age) >= 130:
        print("\nInvalid age. Please enter a numeric age between 1 and 129.")
        return 0
    age = int(age)
    input_person_type = input(f"\nEnter the person type:\n{getPersonType(personType)}").strip()
    personDetails = [id, name, age]
    if not input_person_type.isdigit() or not int(input_person_type) in range(1, len(personType)):
        print(f"\nInvalid person type. Please enter number from 1 to {len(personType)}")
        return 0
    person = personType[int(input_person_type)-1](*personDetails)
    person.setExtraDetails()
    person_index = len(users_index)
    users[person_index] = person
    users_index[id] = person_index
    print(f"\n{person.printMySelf()}\nEntry saved successfully in dictionary!\n")
    return age

def getPersonType(personType):
    person_type = ""
    for i, pType in enumerate(personType, start=1):
        person_type += (f"{i}. {pType.__name__}\n")
    return person_type

def isNumber(value):
    try:
        int(value)
        return True
    except ValueError:
        print(f"Invalid input: {value}. Setting value to 0.")
        return False
    
def searchById(users, users_index):
    id = input(f"Enter the id of the entry to print: ").strip()
    if not id.isdigit():
        print(f"Invalid ID. Please enter a number!")
        return
    id = int(id)
    index = users_index.get(id, None)
    if index == None:
        print(f"ID {id} not found in the list.")   
        return
    person = users.get(index, None)
    print(f"\n{person.printMySelf()}")
            

def printAgeAvg(age_sum, users):
    print(f"\nAverage age is: {age_sum / len(users):.2f}\n")
    
def printAllNames(users):
    for index, person in enumerate(users.items()):
        print(f"{index}: {person[1].getName()}")

def printAllIds(users, users_index):
    if users:
        for index, value in enumerate(users_index.items()):
            print(f"{value[0]}")
    else:
        print("No entries in list!")

def printAllEntries(users):
    if users:
        print("\nAll entries in the list:")
        for index, person in enumerate(users.items()):
            print(f"{index}. {person[1].printMySelf()}")
    else:
        print("No entries in list!")

def printEntryByIndex(users):
    index = input(f"Enter the index to search: (0-{len(users)-1}): ")
    if not index.isdigit():
        print("Invalid index. Please enter a number.")
        return
    person = users.get(int(index), None)
    if person != None:
        print(f"{index}. {person.printMySelf()}")
    else:
        print(f"Index {index} not found!")

def saveAllData(users):
    default_value = "persons.txt"
    file_name = input(f"Enter the output file name (default: {default_value}): ") or default_value
    persons_csv = []
    for person in users.values():
        person_details = person.getPersonDetails()
        persons_csv.append(person_details)
    pd.DataFrame(persons_csv).to_csv(f"{file_name}", index=False)

def importFromFile(users, users_index, personType):
    # print(list(personType.__name__ for personType in personType))
    default_value = "persons.txt"
    file_name = input(f"Enter the input file name (default: {default_value}): ") or default_value
    if not os.path.exists(file_name):
        print(f"File {file_name} does not exist!")
        return
    try:
        df = pd.read_csv(file_name)
        age_sum = 0
        for index, row in df.iterrows():
            if row['id'] in users_index:
                print(f"ID {row['id']} already exists. Skipping entry.")
                continue
            # person_type = row['person_type']
            person_type = personType[[pType.__name__ for pType in personType].index(row['person_type'])]
            extraDetails = {'company': row['company'],
                            'position': row['position'],
                            'salary': int(row['salary']) if pd.notna(row['salary']) else 0,
                            'field_of_study': row['field_of_study'],
                            'score_avg': int(row['score_avg']) if pd.notna(row['score_avg']) else 0}
            person = person_type(row['id'], row['name'], row['age'])
            person.setExtraDetailsFromFile(extraDetails)                    
            users[len(users)] = person
            users_index[row['id']] = len(users) - 1
            age_sum += person.getAge()
        print("Data imported successfully!")
        return age_sum
    except Exception as e:
        print(f"Error importing data: {e}")
    
def exitProgram():
    while True:
        try:
            exit_input = input("\nAre you sure (y/n)? ")
            if exit_input == "y":
                print("Exiting the program. Goodbye!\n")
                return True
            if exit_input == "n":
                os.system('cls')
                print("Returning to the main menu.\n")
                return False
            else:
                continue    
        except KeyboardInterrupt:
            continue

def checkUsers(users):
    if not users:
        print("No entries in list!")
        return False
    return True

def menu():
    os.system('cls')
    for value in Menu.__members__.values():
        print(f"{value.value}. {value.name.replace('_', ' ').title()}")
    choice = input(f"Please enter your choice: ")
    return choice
    
def main():
    users = {}
    users_index = {}
    personType = [Person, Student, Employee]
    age_sum = 0
    exit_program = False
    while not exit_program:
        try:
            choice = menu()
            if choice == Menu.SAVE_NEW_ENTRY.value:
                age = saveNewEntry(users, users_index, personType)
                age_sum += age
            elif choice == Menu.SEARCH_BY_ID.value:
                if checkUsers(users):
                    searchById(users, users_index) 
            elif choice == Menu.PRINT_AGES_AVERAGE.value:
                if checkUsers(users):
                    printAgeAvg(age_sum, users)
            elif choice == Menu.PRINT_ALL_NAMES.value:
                if checkUsers(users):
                    printAllNames(users)
            elif choice == Menu.PRINT_ALL_IDS.value:
                if checkUsers(users):
                    printAllIds(users, users_index)
            elif choice == Menu.PRINT_ALL_ENTRIES.value:
                if checkUsers(users):
                    printAllEntries(users)
            elif choice == Menu.PRINT_ENTRY_BY_INDEX.value:
                if checkUsers(users):
                    printEntryByIndex(users)
            elif choice == Menu.SAVE_DATA_TO_FILE.value:
                if checkUsers(users):
                    saveAllData(users)
            elif choice == Menu.IMPORT_DATA_FROM_FILE.value:
                age_sum = importFromFile(users, users_index, personType)
            elif choice == Menu.EXIT.value:
                exit_program = exitProgram()
            else:
                warnings.simplefilter('always')
                warnings.warn(message="\nInvalid choice. Please enter a number between 0 and 9", category=UserWarning, stacklevel=3)
        except KeyboardInterrupt:
            exit_program = exitProgram()

        if not exit_program:
            os.system('pause')

if __name__ == '__main__':
    main()
