from random import randint
from brain_games.scripts.brain_games import welcome_user
import prompt


def main():
    print('Welcome to the Brain Games!')
    print('Answer "yes" if number even otherwise answer "no".')
    name = welcome_user()
    count = 0
    for _ in range(3):
        rand_number = randint(0, 1000)
        print('Question: {}'.format(rand_number))
        answer_user = prompt.string('Your answer:')
        if rand_number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if correct_answer == answer_user:
            print('Correct!')
            count += 1
            if count == 3:
                print('Congratulations, {}!'.format(name))
        else:
            print("{} is wrong answer ;(. Correct answer was {}"
                  .format(answer_user, correct_answer))
            break


if __name__ == '__main__':
    main()
