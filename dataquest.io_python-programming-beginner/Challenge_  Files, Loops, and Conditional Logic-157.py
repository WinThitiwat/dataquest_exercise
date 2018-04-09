## 3. Read the File Into a String ##

names = open("dq_unisex_names.csv", "r").read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()

names_list = names.split('\n')
first_five = names_list[0:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = []

for cur_element in names_list:
    comma_list = cur_element.split(',')
    nested_list.append(comma_list)

print(nested_list[0:5])

## 6. Convert Numerical Values ##


numerical_list = []
for cur_element in nested_list:
    first_idx = cur_element[0]
    second_idx = float(cur_element[1])
    two_elements = [first_idx, second_idx]
    numerical_list.append(two_elements)
print(numerical_list[0:5])

## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]

thousand_or_greater = []
for cur_element in numerical_list:
    if(cur_element[1] >= 1000):
        thousand_or_greater.append(cur_element[0])
print(thousand_or_greater[0:10])