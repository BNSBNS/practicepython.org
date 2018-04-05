a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

num = int(input("Choose a number: "))

new_a = []

for new_num in a:
    if new_num < num:
        new_a.append(new_num)

print(new_a)

#%d will format a number for display.
#%s will insert the presentation string representation of the object (i.e. str(o))
#%r will insert the canonical string representation of the object (i.e. repr(o))
#If you are formatting an integer, then these are equivalent. For most objects this is not the case.

