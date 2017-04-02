
import random


class Element:
    
    def __init__(self, name, win, lose):
        self.name = name
        self.win = win
        self.lose = lose

    def compare(self, other):
        if isinstance(other, type(self)):
            pass
        if self.name == other.name:
            print('dead-head')
        elif self.name in other.win:
            print('You won')
        else:
            print('You lost')

rock = Element('rock', ['scizors'], ['paper'])
paper = Element('paper', ['rock'], ['scizors'])
scizors = Element('scizors', ['paper'], ['rock'])

element_list = [paper, rock, scizors]
rand_choice = random.choice(element_list)
print(rand_choice.name)
user = input('Choose an element (rock, paper, scizors): ')

try:
    dict_element = {'paper': paper, 'rock':rock, 'scizors': scizors}[user]
    rand_choice.compare(dict_element)
except KeyError:
    print('Choose element from list: )')


class Score:
    '''Write score to file with date and hour of play'''
    
        
    
