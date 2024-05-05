#!/bin/python3

"""
Copyright (c) 2024 wordbuster developer (https://www.linkedin.com/in/saidbek-rahimbekov/)
See the file 'LICENSE' for copying permission
"""

import sys
import time
from os import stat
from itertools import product
from datetime import datetime


version = "1.0.0"
input_chars = ""
start, finish = 1, 4
permutations_list = []
arguments = []
for i in range(len(sys.argv)):
	arguments.append(sys.argv[i])

## time function
def show_time():
	current_datetime = datetime.now()
	formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
	return current_datetime, formatted_datetime
a, b = show_time()
	
## just name or no arguments passed
def headline():
	_, formatted_datetime = show_time()
	print("Wordbuster", version, " - ", formatted_datetime)
	print("Copyright (c) 2024 by Saidbek Rahimbekov")
	print("LinkedIn: https://www.linkedin.com/in/saidbek-rahimbekov/ \n")
	print("Usage: python3 wordbuster [options]")

## --help option		
def help_opt():
	print(f"Wordbuster v({version}) starting in help mode\n")
	time.sleep(2)
	headline()
	print("\n\t-V, --Version \t\tPrint version")
	print("\t-h, --help  \t\tPrint short summary usage")
	print("\t-r, --range  \t\tSet minimum and maximum length of word")
	print("\t-l, --length  \t\tShortcut for --range X X")
	print("\t-p, --pass  \t\tGive characters you want to include only")
	print("\t-o, --outfile  \t\tOutputs to file")
	print("\t-v, --verbose  \t\tShows every step")
	print("\nNote: options with * are mandatory.")
	
def examples():
	print("\n")
	print("\tpython3 wordbuster.py -r 1 3 --pass abcd -o passwords.txt")
	print("\tpython3 wordbuster.py -l 2 --upper --num -o wordlist.txt")
	print("\tpython3 wordbuster.py -r 5 10 --all -o")

## full manual text
def man_opt():
	manual_file = open("manual.txt", "r+")
	print(manual_file.read())
	manual_file.close()

## shows history
def history_opt():
	history_file = open("wordbuster_history.txt", "r+")
	print(history_file.read())
	history_file.close()

## do you want to continue
def continue_question(txt_part=""):
	txt = "[+] Do you want to continue" + txt_part + ", or exit (c, e)? "
	user_input = input(txt)
	if user_input=="c" or user_input=="continue":
		return True
	else:
		return False

## find the index of option
def find_option_index(check_list, short_option, long_option):
	ind = -1
	if short_option in check_list:
		ind = check_list.index(short_option)
	elif long_option in check_list:
		ind = check_list.index(long_option)
	return ind

## index finder
def index_finder(given_list, element):
	for elm in given_list:
		if element == elm:
			return given_list.index(element)
	return -1

## define characters that can be included in word
def chars_set(name):
	upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lower_letters = "abcdefghijklmnopqrstuvwxyz"
	digits = "0123456789"
	all = upper_letters + lower_letters + digits
	
	if name=="--upper":
		return upper_letters
	elif name=="--lower":
		return lower_letters
	elif name=="--num":
		return digits
	elif name=="--all":
		return all

## remove duplicates in a given string
def remove_duplicates(txt):
	newtxt=""
	for char in txt:
		if char not in newtxt:
			newtxt=newtxt+char
	return newtxt

def generate_permutations_with_repetition(chars, length):
	perms = [''.join(p) for p in product(chars, repeat=length)]
	return perms

## calculate lines of wordlist
def calc_comb(start, finish, size):
	res = 1
	n = 0
	for i in range(start, finish+1):
		n+=i
	for i in range(n):
		res*=size
	return res

## history action and writing
history_f = open("wordbuster_history.txt", "a")
_, curr_time = show_time()
txt = "=" * 20 + "\nWordbuster " + version + " - " + curr_time + "\n[+] " + " ".join(arguments) + "\n"
history_f.write(txt)


if len(sys.argv)==1:
	headline()
	print("\nUse --help or -h to list all available options.")
	txt = "[+] SUCCESS " + b + "\n\n\n"
	history_f.write(txt)
	history_f.close()
	exit(0)

if "--version" in arguments or "-V" in arguments:
	print(f"Version: {version}")
	txt = "[+] SUCCESS " + b + "\n\n\n"
	history_f.write(txt)
	history_f.close()
	exit(0)

if "--help" in arguments or "-h" in arguments:
	help_opt()
	examples()
	txt = "[+] SUCCESS " + b + "\n\n\n"
	history_f.write(txt)
	history_f.close()
	exit(0)

if "--manual" in arguments or "-m" in arguments:
	man_opt()
	txt = "[+] SUCCESS " + b + "\n\n\n"
	history_f.write(txt)
	history_f.close()
	exit(0)

if "--history" in arguments or "-H" in arguments:
	history_opt()
	txt = "[+] SUCCESS " + b + "\n\n\n"
	history_f.write(txt)
	history_f.close()
	exit(0)

## specifies characters that will be included
opt_ind = find_option_index(arguments, "-p", "--pass")
if opt_ind>0:
	input_chars = arguments[opt_ind+1]
else:
	options = ["--upper", "--lower", "--num", "--all"]
	for name in options:
		if index_finder(arguments, name)>1:
			input_chars += chars_set(name)
if input_chars == "":
	input_chars = chars_set("--lower")

## set minimum and maximum length of word
opt_ind = find_option_index(arguments, "-r", "--range")
if opt_ind>0:
	start, finish=int(arguments[opt_ind+1]), int(arguments[opt_ind+2])
else:
	opt_ind = find_option_index(arguments, "-l", "--length")
	if opt_ind > 0:
		start, finish = opt_ind, opt_ind
	else:
		err = "[-] Mandatory option is required: -r, --range or -l, --length"
		print(err)
		if continue_question(" to give arguments"):
			start, finish = map(int, input("Input starting and ending range (ex: 2 6): ").split())
		else:
			txt = f"\n{err}\n[-] ERROR " + b + "\n\n\n"
			history_f.write(txt)
			history_f.close()
			exit(0)

input_chars = remove_duplicates(input_chars)
lines = calc_comb(start, finish, len(input_chars))
print("[+] Wordbuster will now generate the following number of lines:", lines)
time.sleep(5)

for i in range(start, finish+1):
	perms = generate_permutations_with_repetition(input_chars, i)
	permutations_list.extend(perms)
	print("[+] Done Length:", i)

opt_ind = find_option_index(arguments, "-o", "--outfile")
if opt_ind + 1 == len(arguments):
	formatted_datetime = a.strftime("%Y-%m-%d-%H-%M-%S")
	filename = "wordlist-" + formatted_datetime + ".txt"
else:
	filename = arguments[opt_ind+1]

print("[+] Wordlist is created.")
continue_question(" writing wordlist to " + filename)

file = open(filename, "w")
for perm in permutations_list:
	file.write(perm + "\n")
print("[+] Closing file")
file.close()

file_size = stat(filename).st_size
file_pb = file_size // 1024**5
file_tb = (file_size - (file_pb * 1024**5)) // 1024**4
file_gb = (file_size - (file_tb * 1024**4)) // 1024**3
file_mb = (file_size - (file_tb * 1024**4) - (file_gb * 1024**3)) // 1024**2
file_kb = (file_size - (file_tb * 1024**4) - (file_gb * 1024**3) - (file_mb * 1024**2)) // 1024
file_b  = file_size - (file_tb * 1024**4) - (file_gb * 1024**3) - (file_mb * 1024**2) - (file_kb * 1024)
print("[+] Wordbuster generated the following amount of data:")
print(f"{file_tb} TB {file_gb} GB {file_mb} MB {file_kb} KB {file_b} B  =  {file_size} B")

txt = "[+] SUCCESS " + b + "\n\n\n"
history_f.write(txt)
history_f.close()

print("[+] Exitting... ")
sys.exit()
