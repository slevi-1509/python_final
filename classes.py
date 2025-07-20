class Person:
    def __init__(self, id, name, age):  # Constructor to initialize name and age
        self._id = id
        self._name = name
        self._age = age
        self._person_type = "Person"

    def getId(self):
        return self._id
    
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age
    
    def getPersonType(self):
        return self._person_type

    def setExtraDetails(self):
        pass

    def setExtraDetailsFromFile(self, extraDetails = None):
        pass

    def getPersonDetails(self):
        return {
            "person_type": self.getPersonType(),
            "id": self.getId(),
            "name": self.getName(),
            "age": self.getAge()
        }
    
    def getPersonString(self):
        return(f"\033[0;97mID: {self.getId()}\n   Name: {self.getName()}\n   Age: {self.getAge()}\n   Type: {self.getPersonType()}\033[0;97m\n")

    def printMySelf(self):
        return self.getPersonString()


class Student(Person):
    def __init__(self, id, name, age): #, field_of_study, score_avg):
        super().__init__(id, name, age)  # Call the parent constructor
        self._person_type = "Student"
        self.field_of_study = ""
        self.score_avg = 0

    def getFieldOfStudy(self):
        return self.field_of_study
    
    def getScoreAvg(self):
        return self.score_avg

    def setExtraDetails(self):
        self.field_of_study = input("Enter field of study: ").strip().title()
        self.score_avg = input("Enter score average: ").strip()
        self.score_avg = int(self.score_avg) if self.score_avg.isdigit() else 0

    def setExtraDetailsFromFile(self, extraDetails):
        self.field_of_study = extraDetails["field_of_study"]
        self.score_avg = extraDetails["score_avg"]
        
    def getPersonDetails(self):
        return {
            "person_type": self.getPersonType(),
            "id": self.getId(),
            "name": self.getName(),
            "age": self.getAge(),
            "field_of_study": self.getFieldOfStudy(),
            "score_avg": self.getScoreAvg()
        }
    
    def printStudent(self):
        return(f"{self.getPersonString()}\033[0;91m   Field of Study: {self.getFieldOfStudy()}\n   Score Average: {self.getScoreAvg()}\033[0;97m\n")

    def printMySelf(self):
        return(self.printStudent())


class Employee(Person):
    def __init__(self, id, name, age, s = None):
        super().__init__(id, name, age)  # Call the parent constructor
        self._person_type = "Employee"

    def getCompany(self):
        return self.company
    
    def getPosition(self):
        return self.position
    
    def getSalary(self):
        return self.salary

    def setExtraDetails(self):
        self.company = input("Enter the company name: ").strip().title()
        self.position = input("Enter your position: ").strip().title()
        self.salary = input("Enter your salary: ").strip()
        self.salary = int(self.salary) if self.salary.isdigit() else 0

    def setExtraDetailsFromFile(self, extraDetails):
        self.company = extraDetails["company"]
        self.position = extraDetails["position"]
        self.salary = extraDetails["salary"]

    def getPersonDetails(self):
        return {
            "person_type": self.getPersonType(),
            "id": self.getId(),
            "name": self.getName(),
            "age": self.getAge(),
            "company": self.getCompany(),
            "position": self.getPosition(),
            "salary": self.getSalary()
        }
    
    def printEmployee(self):
        return(f"{self.getPersonString()}\033[0;96m   Company: {self.getCompany()}\n   Position: {self.getPosition()}\n   Salary: {self.getSalary()}\033[0;97m\n")

    def printMySelf(self):
        return(self.printEmployee())

if __name__ == "__main__":
    test_name = "test_name"
    test_age = 150
    person = Person (1, test_name, test_age)
    if person.getName() != test_name:
        print("Error: Name should be " + test_name + ", but got " + person.getName())
    if person.getAge() != test_age:
        print("Error: Age should be " + str(test_age) + ", but got " + str(person.getAge()))
