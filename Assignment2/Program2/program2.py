class Clerk:
    def __init__(self, id: int, name: str, role: str, salary: float):
        self.clrk_id: int = id
        self.clrk_name: str = name
        self.clrk_role: str = role
        self.clrk_salary: float = salary
    
    def increment_salary(self, percentage: int):
        increase = percentage / 100.0 * self.clrk_salary
        self.clrk_salary += increase
    

class Organization:
    def __init__(self, name: str):
        self.org_name: str = name
        self.clerks: "list[Clerk]" = []
        self.__id = 1
    
    def calculate_salary(self, role: str, percentage: int) -> "list[Clerk]":
        clerks: "list[Clerk]" = []
        for i in range(len(self.clerks)):
            if(self.clerks[i].clrk_role == role):
                self.clerks[i].increment_salary(percentage)
            clerks.append(self.clerks[i])
        
        return clerks
    
    def addClerk(self, name: str, role: str, salary: float):
        clerk = Clerk(self.__id, name, role, salary)
        self.clerks.append(clerk)
        self.__id += 1


if(__name__ == "__main__"):
    org = Organization("Sandy Shores")

    # Get the clerk inputs from file
    try:
        with open("input.txt", "r") as file:
            for row in file:
                temp = row.split(" ")
                name: str = temp[0]
                role: str = temp[1]
                salary: float = float(temp[2])
                org.addClerk(name, role, salary)
    except FileNotFoundError:
        print("File not found. Be sure to name the input file 'input.txt'")
        exit()
    
    # Get role and percentage by which to increase salary
    role: str = input("Input role for whom salary should be increased: ")
    percentage: int = int(input("Input percentage by which salary should be increased: "))

    # Get clerks with increased salary
    new_salaries = org.calculate_salary(role, percentage)

    # Write the clerks with increased salary to output file
    with open("output.txt", "w") as file:
        file.write("Role to increse salary: " + role + "\n")
        file.write("Percentage to increase salary by: " + str(percentage) + "\n\n")

        for clerk in new_salaries:
            file.write(f"{clerk.clrk_name} {clerk.clrk_role} {str(clerk.clrk_salary)}\n")
