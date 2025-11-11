n=int(input("Enter no of Salaries:"))
salary=[]
for i in range(n):
    salary_Employee=int(input(f"Enter Salary of Employee {i+1}"))
    salary.append(salary_Employee)
print(salary)
for i in range(n-1):
    min_index=i
    for j in range(i+1,n):
        if salary[j]<salary[min_index]:
            min_index=j
            salary[i],salary[j]=salary[j],salary[i]
print(salary)