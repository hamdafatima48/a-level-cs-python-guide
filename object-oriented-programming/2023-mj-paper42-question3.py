'''
Cambridge International AS & A Level Computer Science 9618
Paper 42 Practical - May/June 2023
Question: 3

Short description:
This question was about using OOP to store employee pay details.
It required an Employee class, then a Manager subclass that inherits from Employee.
The program reads employee data and hours worked from files, then calculates and outputs total pay.
'''


class Employee:
    def __init__(self, pay, num, title):
        self.__HourlyPay = pay               # PRIVATE HourlyPay: REAL
        self.__EmployeeNumber = num          # PRIVATE EmployeeNumber: STRING
        self.__JobTitle = title              # PRIVATE JobTitle: STRING
        self.__PayYear2022 = [0.0]*52        # PRIVATE PayYear2022: ARRAY[0:52] OF REAL

    def GetEmployeeNumber(self):
        return self.__EmployeeNumber

    def SetPay(self, weekNum, hours):
        Pay = self.__HourlyPay * hours
        self.__PayYear2022[weekNum-1] = Pay  # arrays last index will be 51

    def GetTotalPay(self):
        ans = 0
        for i in range(8):
            ans = ans + self.__PayYear2022[i]
        return ans


class Manager(Employee):
    def __init__(self, bonus, pay, num, title):
        Employee.__init__(self, pay, num, title)
        self.__BonusValue = float(bonus)    # PRIVATE BonusValue: REAL

    def SetPay(self, week, hours):
        hours = hours * (1 + self.__BonusValue/100)
        Employee.SetPay(self, week, hours)


def EnterHours():
    f = open('HoursWeek1.txt', 'r')
    for i in range(8):
        EmployeeID = f.readline().strip()
        hours = f.readline().strip()
        for z in range(8):
            temp = EmployeeArray[z].GetEmployeeNumber()
            if EmployeeID == temp:
                EmployeeArray[z].SetPay(1, float(hours))
    f.close()


# ********MAIN********

Employee1 = Employee(0.0, "", "")
EmployeeArray = [Employee1]*8
# I made one blank Employee first so I could create an array with 8 spaces.
# This is just used to initialise the array before reading the real data from the file.

try:
  file = open("Employees.txt", "r")

  for i in range(8):
    # Each employee starts with hourly pay and employee number.
    line1 = float(file.readline().strip())
    line2 = file.readline().strip()

    # The third line can either be a bonus value or a job title.
    # This is the unusual part of the question.
    BonusTitle = file.readline().strip()

    try:
        # If BonusTitle can be converted to a float,
        # then this record is for a Manager because managers have a bonus.
        Bonus = float(BonusTitle)

        # For a manager, the next line is the job title.
        line4 = file.readline().strip()

        # So here I create a Manager object instead of a normal Employee object.
        EmployeeArray[i] = Manager(BonusTitle, line1, line2, line4)

    except:
        # If BonusTitle is not a number, then it is actually the job title.
        # So this employee is not a manager.
        EmployeeArray[i] = Employee(line1, line2, BonusTitle)

file.close()

except IOError:
  print('error')

# This reads the hours worked from HoursWeek1.txt
# and uses the employee number to match the hours to the correct employee.

EnterHours()

# After the pay has been set, we print each employee's number and total pay.

for i in range(8):
  c = EmployeeArray[i].GetTotalPay()
  print(EmployeeArray[i].GetEmployeeNumber())
  print(c)
