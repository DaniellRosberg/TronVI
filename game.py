import random

import socket

import threading

import os


def game():
    number = random.randint(0, 1000)
    tries = 1
    done = False
    while not done:
        guess = input('Введите число: ')
        if guess.isdigit():
            guess = int(guess)
            if guess == number:
                done = True
                print(f'Ты победил! Я загадал {guess}. Ты использовал {tries} попыток.')
            else:
                tries += 1
            if guess > number:
                print('Загаданное число меньше!')
            else:
                print('Загаданное число больше!')
        else:
            print('Это не число от 0 до 1000!')