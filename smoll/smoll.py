# coding: utf8
import time
from termcolor import colored, cprint
import colorama



# number
# previous_time
# current_time

f_num = open("number.txt", "r")
pre_number = int(f_num.read())
f_num.close()

f_pre_data = open("data.txt", "r")
pre_data = int(f_pre_data.read(10))
f_pre_data.close()

# pre_number pre_data

cur_data = time.time()

refuse = int(cur_data) - int(pre_data)

cur_number = refuse / 480

result = pre_number + int(cur_number)

if result >= 160:
	result = 160
print(result)

f_cur_data = open("data.txt", "w")
f_cur_data.write(str(cur_data))
f_cur_data.close()

f_cur_number = open("number.txt", "w")
f_cur_number.write(str(result))
f_cur_number.close()



i = input()