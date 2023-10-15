import random

def game(x, computerchoice):
    match x:
      case 'rock':
        if computerchoice == 'rock':
            print(f"you: {x}  computer: {computerchoice}")
            return 'Draw'
        elif computerchoice == 'scissor':
            print(f"you: {x}  computer:{computerchoice}")
            return 'You won'
        else:
            print(f"you: {x} computer: {computerchoice}")
            return 'You lost'
     case 'paper':
         if computerchoice == 'paper':
            print(f"you: {x}  computer: {computerchoice}")
            return 'Draw'
        elif computerchoice == 'rock':
            print(f"you: {x}  computer:{computerchoice}")
            return 'You won'
        else:
            print(f"you: {x} computer: {computerchoice}")
            return 'You lost'
     case 'scissor':
         if computerchoice == 'scissor':
            print(f"you: {x}  computer: {computerchoice}")
            return 'Draw'
        elif computerchoice == 'paper':
            print(f"you: {x}  computer:{computerchoice}")
            return 'You won'
        else:
            print(f"you: {x} computer: {computerchoice}")
            return 'You lost'
     case _:
           return 'replay'

choices = ['rock', 'paper', 'scissor']
result = 'replay'
while result == 'replay':
    x = input ('plase choose rock, paper, or scissor:')
    computerchoice = random.chocie(chocies)
    result = game(x. computerchoice)
    if result != 'replay':
        print(result)
        replay = input('you want to play again ? y/n')
        if (replay != 'n') and (replay != 'N'):
            result = 'replay'
    else:
        print(f'your input {x} is not valid')


