import random

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissors']

while True:
    user_input = input(
        'enter your choice: rock/paper/scissors or quit q:').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    computer_choice = options[random_number]
    print(f'Computer picked {computer_choice}.')

    if (user_input == 'rock' and computer_choice == 'scissors') or (user_input == 'paper' and computer_choice == 'rock') or (user_input == 'scissors' and computer_choice == 'paper'):
        print('You win!')
        user_wins = user_wins + 1

    elif user_input == computer_choice:
        print('Its a draw!')

    else:
        print('Computer wins!')
        computer_wins = computer_wins + 1

print(f'You won {user_wins} times!')
print(f'The computer won {computer_wins} times!')
print('Goodbye!')
