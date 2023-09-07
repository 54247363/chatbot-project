import random

R_EATING = "i dont eat because im not hungry"

def unknown():
    response = ['could you please rephrase that?',
                "...",
                'sounds about right',
                'what does that mean'][random.arrange(4)]
    return response 