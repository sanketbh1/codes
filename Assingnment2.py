n=int(input("Enter no of customer ids to stored "))
customer_id=[]
for i in range (0,n):
    elements=int(input(f"Enter element {i+1} "))
    customer_id.append(elements)
print(customer_id)
print("to perform selection sort \n1.Selection sort \n2.bubble sort")
choice=int(input("Enter choice 1 and 2"))
if(choice ==1):
   def Selection(customer_id):
       n=len(customer_id)
       for i in range(n-1):
           mini=i
           for j in range(i+1,n):
               if customer_id[j] < customer_id[mini]:
                mini=j
                customer_id[i],customer_id[mini]=customer_id[mini],customer_id[i]
print(customer_id)
       

                    