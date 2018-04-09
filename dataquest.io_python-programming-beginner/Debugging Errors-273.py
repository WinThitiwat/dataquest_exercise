## 2. Syntax Errors ##

def first_elts(input_lst):
    elts = []
    for each in input_lst:
        elts.append(each)
    return elts

animals = [["dog","cat","rabbit"],["turtle","snake"],["sloth","penguin","bird"]]
first_animal = first_elts(animals)
print(first_animal)

## 4. TypeError and ValueError ##

forty_two = 42
forty_two + "42"

int("guardians")

## 5. IndexError and AttributeError ##

lives = [1,2,3]
lives[4]

f = open("story.txt")
f.split(" ")