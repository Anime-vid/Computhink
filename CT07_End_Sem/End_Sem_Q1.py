# Big_sale = 0
# Day_Big_Sale = 0
# Small_Sale = 9999999999999999999
# Day_Small_Sale = 0
daily_sales = [1205, 986, 1354, 10535, 15741, 11200, 800, 13056, 952, 1100, 1025, 8574, 14014, 9987, 1238, 1458, 7803, 900, 13674, 14539, 13241, 10886, 7541, 8743, 1482, 11523, 977, 12181, 8903, 1008, 1530]
Day_Big_Sale = 0
Small_Sale = min(daily_sales)
Day_Small_Sale = 0
Avg_total = 0
Big_sale = max(daily_sales)

# for i in range(len(daily_sales)):
#     if daily_sales[i] > Big_sale:
#         Big_sale = daily_sales[i]
#         Day_Big_Sale = i + 1
# for i in range(len(daily_sales)):
#     if daily_sales[i] < Small_Sale:
#         Small_Sale = daily_sales[i]
#         Day_Small_Sale = i + 1
for i in range(len(daily_sales)):
    if daily_sales[i] == Big_sale:
        Day_Big_Sale = i + 1
for i in range(len(daily_sales)):
    if daily_sales[i] == Small_Sale:
        Day_Small_Sale = i + 1
for i in range(len(daily_sales)):
    Avg_total = Avg_total + daily_sales[i]
print(str(Day_Big_Sale) + " August has highest sales of $" + str(Big_sale))
print(str(Day_Small_Sale) + " August has highest sales of $" + str(Small_Sale))
print("Average daily sales for August is " + str(round(Avg_total / len(daily_sales),2)))



