n=int(input("Enter number of customers Ids to stored :"))
customer_ids=[]
for i in range(0,n):
    elements=int(input(f"Enter {i+1} :"))
    customer_ids.append(elements)
print("Customer ids are :",customer_ids)
print("In which way you want to elements to found \n1. Linear search \n2. Binary search")
choice=int(input("Enter choice between 1 and 2 : "))
if(choice ==1):
    target=int(input("Enter customer id to find :"))
    for i in range(0,n):
        if customer_ids[i]==target:
            print("Id found ")
            break
        else:
            print("not found")
            break

elif choice==2:
    temp=0 
    for i in range (n):
        for j in range (i+1,n):
            if(customer_ids[i]>customer_ids[j]):
                temp=customer_ids[i]
                customer_ids[i]=customer_ids[j]
                customer_ids[j]=temp
    print(customer_ids)
    target=int(input("Enter customer id to search : "))
    li=0
    hi=n-1
    while(li<=hi):
        mid=(li+hi)//2
        if(customer_ids[mid]==target):
            print("Id found at index ",mid)
            break
        elif (target >customer_ids[mid]):
            li=mid+1
        else:
            hi=mid-1
    