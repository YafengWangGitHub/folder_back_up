# this code is to copy all the files in 'src folder(source folder) to
# dest folder(destination folder)'

import os  
import shutil # this module allow us to do many advanced things on folder  
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
dt_string = now.strftime("%d-%m-%Y/%H-%M")
# print("date and time =", dt_string)
   
src = 'C:/Users/Your source Path
str1 = 'D:/005_one_drive backup'
str2 = '/Backup at '
str3 = dt_string

newstr = "".join((str1, str2, str3))
dest =  newstr

destination = shutil.copytree(src, dest)  
   
print("Back up folder path:", dest)
