import subprocess
import pyperclip
import random



file = open('draculaflow/bars.txt')
bars = file.readlines()

bar = random.choice(bars)

pyperclip.copy(bar)
pyperclip.paste()
