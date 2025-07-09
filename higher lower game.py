import random

import game_art
import game_database

def display_data(account):
    name=account['name']
    follow_count=account['follow_count']
    description=account['description']
    country=account['country']
    return f'{name},a {description} from {country}'

score=0
looping=True
while looping:
    print(game_art.higher_lower)

    account_1=random.choice(game_database.data)
    account_2=random.choice(game_database.data)

    print(f'compare 1:{display_data(account_1)}')
    print(game_art.vs)
    print(f'compare 2:{display_data(account_2)}')

    game_answer=int(input(f"chose one person who has more followers.If {account_1['name']} press 1 or {account_2['name']} press 2"))

    if account_1['follow_count']>account_2['follow_count']:
        if game_answer == 1:
            print(f'correct{ account_1["name"]} has more folow count')
            score += 1
        else:
            print(f'wrong { account_2["name"]} has more follow count')
    elif account_2['follow_count']>account_1['follow_count']:
        if game_answer == 2:
            print(f'correct{ account_2["name"]} has more folow count')
            score += 1
        else:
            print(f'wrong { account_1["name"]} has more follow count')
    else:
        print("invalid input")
    print(f'you score is:{ score}')
    retry=input(f"wanna continue press 'y' else press 'n' to exit")
    if retry =='y':
        print('\n' * 100)
        looping=True
    else:
        print(f'Thanks for playing .you final score is:{score}')
        looping=False

