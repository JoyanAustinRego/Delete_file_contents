import os
import re

with open("master_file.txt", "r") as master_file:
    master_contents = master_file.readlines()


with open("string_file.txt", "r") as string_file:
    string_contents = string_file.readlines()


for master_element in master_contents:   
    for string_element in string_contents:
       if(re.search(string_element, master_element)):
           master_contents.remove(master_element)

         
with open("master_file.txt", "w") as master_file:
    for master_element in master_contents:
        master_file.writelines(master_element)
      
