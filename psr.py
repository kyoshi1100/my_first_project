from random import choice

ratings = open('rating.txt', 'r')
name = input('Enter your name: ')
print(f'Hello, {name}')
score = 0

for line in ratings:
    content = line.split()
    if name == content[0]:
        score = int(content[1])

opts = input()
if opts in ['', '\n', '\r\n']:
    options_list = ['scissors', 'rock', 'paper']
else:
    options_list = opts.split(',')
print("Okay, let's start")


def relations(option):
    rules = options_list[options_list.index(option) + 1:] + options_list[:options_list.index(option)]
    return rules


while True:
    user_choice = input()
    computer_choice = choice(options_list)
    if user_choice not in options_list:
        print('Invalid input')
    loose = relations(computer_choice)[:len(relations(computer_choice))//2]
    win = relations(computer_choice)[len(relations(computer_choice))//2:]
    if user_choice == '!rating':
        print(f'Your rating: {score}')
    if user_choice == '!exit':
        print('Bye!')
        break
    if user_choice in loose:
        print(f'Well done. The computer chose {computer_choice} and failed')
        score += 100
    elif user_choice == computer_choice:
        print(f'There is a draw ({user_choice})')
        score += 50
    elif user_choice in win:
        print(f'Sorry, but the computer chose {computer_choice}')

ratings.close()
