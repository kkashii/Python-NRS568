# Challenge 3.3
#
# Using the Atmospheric Carbon Dioxide Dry Air Mole Fractions from quasi-continuous daily measurements at Mauna Loa,
# Hawaii dataset, obtained from here (https://github.com/datasets/co2-ppm-daily/tree/master/data).
#
# Using Python (csv) calculate the following:
#
# Annual average for each year in the dataset.
# Minimum, maximum and average for the entire dataset.
# Seasonal average if Spring (March, April, May), Summer (June, July, August), Autumn (September, October, November) and Winter (December, January, February).
# Calculate the anomaly for each value in the dataset relative to the mean for the entire timeseries.


import csv


# # # Annual average

year_list = []

# Im first creating an inventory of years

with open("E:\KMK_Python\co2-ppm-daily-master\data\co2-ppm-daily.csv") as co2_csv:
    csv_reader = csv.reader(co2_csv, delimiter=",")
    headerline = co2_csv.next()
    year_sum = 0
    total_sum = 0
#
# # I'm pulling the csv file I want to use and defining its format as well as skipping the first line of headers
# # I need to define sum of the values of a single year and the total sum, both set at zero
# # Next, I am identifying the format of the CSV file and how python can identify the year, month, and day
# # I am then looping the years and appending that list so that the year value will only appear once
#
    for row in csv_reader:
        year, month, day = row[0].split("-")
        if year not in year_list:
            year_list.append(year)
#
# # Next I am defining what the total sum of values in row 2 is as well as the totals for each year
# # By defining the variables I can more easily write the final equation
#
    for row in co2_csv:
        total_sum = sum(row[1])
        if year == year:
            year_sum = sum(row[1])

    annual_average = year_sum / total_sum

print annual_avg(year_list)

# Solutions Method for Annual Average
#
year_value_dict = {}

for year in year_list:
    temp_year_list = []
    with open("co2-ppm-daily.csv") as co2:
        csv_reader = csv.reader(co2, delimiter=',')
        headerline = co2.next()

        for row in csv_reader:
            year_co2, month_co2, day = row[0].split("-")
            if year_co2 == year:
                temp_year_list.append(float(row[1]))

    year_value_dict[year] = str(sum(temp_year_list) / len(temp_year_list))

print year_value_dict

# # # Min, Max, Avg

# I am identifying the values and the line count. Then I am looping the values in row 1 to calculate the stats

values = []
line_count = 0

with open("E:\KMK_Python\co2-ppm-daily-master\data\co2-ppm-daily.csv") as co2_csv:
    csv_reader = csv.reader(co2_csv, delimiter=",")
    headerline = co2_csv.next()
    line_count = line_count + 1

for values in row[1]:

print "Minimum = " + str(min(values)
print "Maximum = " + str(max(values)
print "Average = " + str(sum(values) / len(line_count))


# # # Seasons
#
spring = []
summer = []
fall = []
winter = []
with open ("E:\KMK_Python\co2-ppm-daily-master\data\co2-ppm-daily.csv") as co2_csv:
    csv_reader = csv.reader(co2_csv, delimiter=",")
    headerline = co2_csv.next()

    for row in csv_reader:
        year, month, day = row[0].split("-")
        if month == "03" or month == "04" or month == "05":
            spring.append(float(row[1]))
        if month == "06" or month == "07" or month == "08":
            summer.append(float(row[1]))
        if month == "09" or month == "10" or month == "11":
            fall.append(float(row[1]))
        if month == "12" or month == "01" or month == "02":
            winter.append(float(row[1]))

print "Spring = " + str(sum(spring) / len(spring))
print "Summer = " + str(sum(summer) / len(summer))
print "Fall = " + str(sum(fall) / len(fall))
print "Winter = " + str(sum(winter) / len(winter))


# # # Anomaly


with open ("E:\KMK_Python\co2-ppm-daily-master\data\co2-ppm-daily.csv") as co2_csv:
    csv_reader = csv.reader(co2_csv, delimiter=",")
    headerline = co2_csv.next()

    for row in csv_reader:
        anomaly = int(float(row[1])) - int(float(str(sum(row[1])/(len(row[1])))))

print anomaly
