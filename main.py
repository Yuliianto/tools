import requests
import sys
import os
from pyfiglet import Figlet
import re

class Bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'



class Tools:
	"""docstring for Tools"""
	options = {'-l':False,'-i':False,'-m':False,'-c':False,'-f':None,'-o':None}
	def __init__(self, arg):
		super(Tools, self).__init__()
		self.arg = arg
	
	def run():
		print("when you run the")
	



def main(_option=None):
	n = len(sys.argv)
	if n == 1:
		manualBook()
	tools = Tools
	for x in range(1,n):
		if _option[x][:_option[x].find("=")] in tools.options:
			tools.options[_option[x][:_option[x].find("=")]]=_option[x][_option[x].find("=")+1:]
		elif _option[x] in tools.options:
			tools.options[_option[x]] = True
		else:
			manualBook(_option[x]+": Command not found!!")
		# if re.search(r'\w',_option[x]).group() in tools.options:
		# 	tools.options[re.search(r'\w',_option[x]).group()] = True
	tools.run()


def manualBook(_message=None):
	custom_fig = Figlet(font='basic')
	os.system("clear")
	print("\n")
	print(Bcolors.WARNING+custom_fig.renderText('SCTOOLS')+Bcolors.ENDC)
	print(Bcolors.FAIL,_message,Bcolors.ENDC)
	print('Useage : sctools [options] [path/order_id]\n\n\n')
	print("Options : ")
	print("  -l, --fix-lcode \t\t ","memperbaiki lcode")
	print("  -i, --fix-indihome-type \t ","memperbaiki nilai indihome indicator")
	print("  -m, --fix-milestone-deposit \t ","untuk fix milestone deposit")
	print("  -c, --cek-status \t\t ","untuk cek status")
	print("  -f, --file-mass=path file \t  lokasi file untuk di masalain ")
	print("  -o, --order_id=order_id \t  order id target")
	print("\n\n\n")

def banner():
	custom_fig = Figlet(font='basic')
	os.system("clear")
	print(Bcolors.WARNING+custom_fig.renderText('SCTOOLS')+Bcolors.ENDC)

if __name__ == '__main__':
	main(sys.argv)