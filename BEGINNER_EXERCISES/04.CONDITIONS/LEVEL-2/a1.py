month = 'February'

month_31_days = ('January', 'March', 'May', 'July',
                 'August', 'October', 'December')
month_30_days = ('April', 'Jun', 'September', 'November')

if month in month_31_days:
    print(f"{month} has 31 days")
elif month in month_30_days:
    print(f"{month} has 30 days")
else:
    print(f"{month} has 28 days")
