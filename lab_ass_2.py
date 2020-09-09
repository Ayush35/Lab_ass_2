month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
days = ['31 days','28/29 days','31 days','30 days', '31 days','30 days','31 days','31 days','30 days','31 days','30 days','31 days']
print(month)
data=input("Enter the Name of Month:  ")        #input Month

print("No. of days : {} ".format( days[month.index(data)] ))   #value printed from days on same index as in list month