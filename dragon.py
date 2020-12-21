import random
import time

def dictionary(language, codMsg):
    if language == 'en':
        switcher = {
            'm1':'''You are in a land full of dragons. In front of you, you see two caves.
    In one of the caves, the dragon is friendly and will share the treasure with you.
    The other dragon is greedy and hungry and will eat you on sight.''',
            'm2':'Wich cave will you go into? (1 or 2)',
            'm3':'You approach the cave...',
            'm4':'It is dark ans spooky...',
            'm5':'A large dragon jumps out in front of you! He opens his jaws and...',
            'm6':'Gives you his treasure!',
            'm7':'Gobbles you down in one bite!',
            'm8':'Do you want to play again? (yes or no)',
            'm9':'',
            'm10':''
            }
    elif language == 'pt':
        switcher = {
            'm1':'''Você está em uma terra cheia de dragões. À sua frente, você vê duas cavernas.
     Em uma das cavernas, o dragão é amigável e compartilhará o tesouro com você.
     O outro dragão é ganancioso e faminto e irá comê-lo à primeira vista.''',
            'm2':'Em que caverna você irá entrar? (1 ou 2)',
            'm3':'Você se aproxima da caverna...',
            'm4':'Está escuro e assustador...',
            'm5':'Um grande dragão pula na sua frente! Ele abre suas mandíbulas e ...',
            'm6':'Dá a você seu tesouro!',
            'm7':'Devora você com uma só mordida!',
            'm8':'Você quer jogar de novo? (sim ou não)',
            'm9':'',
            'm10':''
            }
    else:
        print('Language not available.')
    return switcher[codMsg]

def displayIntro(language):
    print(dictionary(language, 'm1'))
    print()

def chooseCave(language):
    cave = ''
    while cave != '1' and cave != '2':
        print(dictionary(language, 'm2'))
        cave = input()

    return cave

def checkCave(language, chosenCave):
    print(dictionary(language, 'm3'))
    time.sleep(2)
    print(dictionary(language, 'm4'))
    time.sleep(2)
    print(dictionary(language, 'm5'))
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)

    if chosenCave == str(friendlyCave):
        print(dictionary(language, 'm6'))
    else:
        print(dictionary(language, 'm7'))

def stillPlaying(userAnswer):
    if userAnswer.lower() in ('yes','y','sim','s'):
        play = True
    else:
        play = False
    return play

chosenLang = ''
while chosenLang != 'pt' and chosenLang != 'en':

    print('Escolha um idioma. (PT/EN) \nChoose a language. (PT/EN)')
    chosenLang = str(input()).lower()

playAgain = True
while playAgain:
    displayIntro(chosenLang)
    caveNumber = chooseCave(chosenLang)
    checkCave(chosenLang, caveNumber)

    print(dictionary(chosenLang, 'm8'))
    playAgain = stillPlaying(str(input()))
    
