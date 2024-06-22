import random

messages = [
    'it is certain',
    'it is decidedly so',
    'without a doubt',
    'yes - definitely',
    'you may rely on it',
    'as I see it, yes',
]

print(messages[random.randint(0, len(messages) - 1)])
