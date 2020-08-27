from random import randint
from brain_games.scripts.brain_games import welcome_user
import prompt


def main():
    print('Welcome to the Brain Games!\nAnswer "yes" if number even otherwise answer "no".')
    welcome_user()
    
    rand_number = randint(0, 1000)
    print('Question: {}'.format(rand_number))
    answer_user = prompt.string('Your answer:')
    if rand_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    if correct_answer == answer_user:
        print('Correct!')
    #print("'yes' is wrong answer ;(. Correct answer was 'no'")

if __name__ == '__main__':
    main()