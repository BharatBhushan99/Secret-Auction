from replit import clear

participants = {}

print("Welcome to the secret auction program.")

keepLooping = True

while keepLooping:

  name = input("What is your name?: ")
  amount = float(input("What's your bid?: $"))

  participants[name] = amount

  is_next_participant = input("Are there any other bidders? Type 'yes' or 'no'.\n")

  if is_next_participant == 'no':
    keepLooping = False
  else:
    clear()

print(f"The winner is {max(participants)} with a bid of ${participants[max(participants)]}")
    