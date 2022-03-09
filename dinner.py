import random

def whatToEat():
    possible_responses = [
    'Bacon!',
    'Hamburgare!',
    'Pizza!',
    'Det som är på extrapris på Maxi.',
    'Dillkött.',
    'Pommes med bea.'
    ]

    return f'{random.choice(possible_responses)} Det är vad du borde äta till middag.'