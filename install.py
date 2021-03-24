import os
import time

print('''
CODED BY BLACK CODERS
''')
	

def func():
	while True:
		choice = input('''

	1. Install Required Library
	2. SHELLPHISH
	3. CAMPHISH
	4. SAYCHEESE
	5. EXIT

	''')
		if choice == 1:
			os.system('apt-get update')
			os.system('apt-get install php')
			os.system('apt-get install curl')
			os.system('apt-get install wget')
			os.system('apt-get install openssh')
			print('ALL REQUIRED LIBRARIES ARE INSTALLED SUCCESSFULLY')

		if choice == 2:
			os.system('git clone https://github.com/suljot/shellphish.git')
			print('You have Successfully installed Shellphish')

		if choice == 3:
			os.system('git clone https://github.com/techchipnet/CamPhish.git')
			print('You have Successfully installed Camphish')

		if choice == 4:
			os.system('git clone https://github.com/hangetzzu/saycheese.git')
			print('You have Successfully installed Saycheese')

		else:
			print('Thanks for Using')
			break

func()
