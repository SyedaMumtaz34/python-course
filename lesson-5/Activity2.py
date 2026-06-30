Actual_cost=int(input("Enter Your Actual cost "))
Selling_cost=int(input("Enter Your Selling Cost "))
if Selling_cost>Actual_cost:
    Amount=(Selling_cost-Actual_cost)
    print("Total profit is ",Amount)
else:
    print("No Profit")
