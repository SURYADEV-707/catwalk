import sys
import os
import subprocess
import re
import shutil
from termcolor import colored
banner="""

█▀▀ ▄▀█ ▀█▀ █░█░█ ▄▀█ █░░ █▄▀
█▄▄ █▀█ ░█░ ▀▄▀▄▀ █▀█ █▄▄ █░█

"""
arg=len(sys.argv)
flag_found=False
empty=open(os.devnull,"w")
temp_file_name=".temp"
FNEW=open(temp_file_name,"w")
if (arg>2 or arg<2):
    print(colored("please speficy the file to work on !!","red"))
else:
    files=os.listdir(os.getcwd())
    if sys.argv[1] not in files:
        print(f"{sys.argv[1]} file not found !!")
    else:
        subprocess.call(['binwalk', '-e' ,'-M', sys.argv[1]],stdout=FNEW)
        d=subprocess.check_output(['grep','name:',temp_file_name])
        tg=d.decode()
        print(colored(banner,"cyan"))
        print(colored("possible artifact found :","green"))
        print("==========================")
        r=re.findall("name:.*",tg)
        for k in r:
            if ".txt" in k:
                print(colored(k,"green"))
            else :
                print(k)
        print("==========================")
        print()
        directory="_"+sys.argv[1]+".extracted"
        os.remove(temp_file_name)
        shutil.rmtree(directory)
        sys.exit()
        
    


