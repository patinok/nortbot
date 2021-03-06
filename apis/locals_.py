# -*- coding: utf-8 -*-

"""
The MIT License (MIT)

Copyright (c) 2019 Nortxort

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import random


def eight_ball():
    """
    Magic eight ball.

    :return: A random answer.
    :rtype: str
    """
    answers = [
        'It is certain', 'It is decidedly so', 'without a doubt', 'Yes definitely',
        'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good',
        'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later',
        'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
        'Don\'t count on it', 'My reply is no', 'My sources say no', 'Outlook not so good',
        'Very doubtful'
    ]
    return random.choice(answers)


def flip_coin():
    """
    Flip a coin.

    :return: Heads or tails.
    :rtype: str
    """
    coin = ['heads', 'tails']
    return random.choice(coin)


def roll_dice():
    """
    Roll a 6 sided dice.

    :return: A number between 1 and 6.
    :rtype: str
    """
    numbers = ['1', '2', '3', '4', '5', '6']
    return random.choice(numbers)
