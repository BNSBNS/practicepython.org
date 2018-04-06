player1_input = input("Player 1! Select one: Rock, Scissor or Paper: " ).lower()
player2_input = input("Player 2! Select one: Rock, Scissor or Paper: " ).lower()

a = "rock"
b = "scissor" 
c = "paper"

if player1_input == a and player2_input == b:
print("Player 1, you win !")
if player1_input == a and player2_input == c:
print("Player 1, you win !")
elif player1_input == a and player2_input == a:
print("DRAAAAAAAAAAAAAAAAW")
elif player1_input == b and player2_input == c:
print("Player 2, you win !")
elif player1_input == b and player2_input == a:
print("Player 2, you win !")
elif player1_input == b and player2_input == b:
print("DRAAAAAAAAAAAAAW")
elif player1_input == c and player2_input == b:
print("Player 2, you win !")
elif player1_input == c and player2_input == a:
print("Player 1, you win ! ")
elif player1_input == c and player2_input == c:
print("DRAWWWWWWWWWWWWWWWW")

else:
print("INVALID !!")
