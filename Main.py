n = int(input("Enter no. of Employees: "))
salary_from_user = []
# Input salaries
for x in range(n):
    salary = int(input(f"Enter salary for Employee {x+1}: "))
    salary_from_user.append(salary)
# Show unsorted salaries
print("Unsorted array is:", salary_from_user)
# Choose sorting option
option = int(input("Select option for sorting \n1 - Selection Sort \n2 - Bubble Sort\n"))
if option == 1:
# ----------------------------Selection Sort---------------------------
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if salary_from_user[j] < salary_from_user[min_index]:
                min_index = j
                salary_from_user[i], salary_from_user[min_index] = salary_from_user[min_index],salary_from_user[i]
print("Sorted array using Selection Sort:", salary_from_user)