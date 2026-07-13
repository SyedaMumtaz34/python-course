def Total_celc(bill_amount,tip_perc):
    Total=bill_amount*(1+0.01*tip_perc )
    Total=round(Total,2)
    print("please pay ",Total )
Total_celc(150,20)