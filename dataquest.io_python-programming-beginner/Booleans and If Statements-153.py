## 1. Booleans ##

cat = True
dog = False
print(type(cat))

## 2. Boolean Operators ##

first_alb = (cities[0] == "Albuquerque")
second_alb = (cities[1] == "Albuquerque")
first_last = (cities[0] == cities[len(cities)-1])

## 3. Booleans with "Greater Than" ##

first_500 = (crime_rates[0] > 500)
first_749 = (crime_rates[0] >= 749)
first_last = (crime_rates[0] >= crime_rates[len(crime_rates)-1])

## 4. Booleans with "Less Than" ##


second_500 = (crime_rates[1] < 500)
second_371 = (crime_rates[1] <= 371)
second_last = (crime_rates[1] <= crime_rates[len(crime_rates)-1])

## 5. If Statements ##

result = 0

if (cities[2]=="Anchorage"):
    result = 1

## 6. Nesting If Statements ##

both_conditions = False

if (crime_rates[0]>500 and crime_rates[1] > 300):
    both_conditions = True
    




## 7. If Statements and For Loops ##

five_hundred_list = []
for cur_element in crime_rates:
    if cur_element > 500:
        five_hundred_list.append(cur_element)

## 8. Find the Highest Crime Rate ##



highest = 0
for cur_element in crime_rates:
    if (cur_element > highest):
        highest = cur_element