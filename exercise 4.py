user_input = int(input("give a number: "))

List_range = list(range(1, user_input+1))

divisor = []

for number in List_range:
    if user_input % number == 0:
        divisor.append(number)

print(divisor)

#write it as english as possible