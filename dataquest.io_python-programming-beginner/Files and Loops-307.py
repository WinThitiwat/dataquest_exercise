## 1. Opening Files ##

f = open("crime_rates.csv", "r")

## 2. Reading In Files ##

f = open("crime_rates.csv", "r")
data = f.read()

print(data)

## 3. Splitting ##

# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows)

## 5. Practice - Loops ##

ten_rows = rows[0:10]
for each_row in ten_rows:
    print(each_row)


## 6. List of Lists ##

three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])

## 7. Practice - Splitting Elements in a List ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
final_data = []
for each_row in rows:
    temp = each_row.split(',')
    final_data.append(temp)
    
print(final_data)

## 8. Accessing Elements in a List of Lists: The Manual Way ##

print(five_elements)
cities_list = []
for each in five_elements:
    cities_list.append(each[0])
    

## 9. Looping Through a List of Lists ##

crime_rates = []
cities_list = []
for row in final_data:
    cities_list.append(row[0])
    # row is a list variable, not a string.
    crime_rate = row[1]
    # crime_rate is a string, the crime rate of the city.
    crime_rates.append(crime_rate)

## 10. Challenge ##

f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
int_crime_rates  = []
for each in rows:
    temp = each.split(',')
    int_crime_rates.append(int(temp[1]))

