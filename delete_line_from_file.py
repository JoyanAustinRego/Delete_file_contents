import os
import re


master_contents_list = []
string_contents_list = []


with open("master_file.txt", "r") as master_file:
    master_contents = master_file.readlines()
    

with open("string_file.txt", "r") as string_file:
    string_contents = string_file.readlines()


for master_elements in master_contents:
    master_contents_list.append(master_elements.strip('\n'))


for string_element in string_contents:
    string_contents_list.append(string_element.strip('\n'))

 
for master_element in master_contents_list:   
    for string_element in string_contents_list:
       if(re.search(string_element, master_element)):
           master_contents_list.remove(master_element)

         
with open("master_file.txt", "w") as master_file:
    for master_element in master_contents_list:
        master_file.writelines(master_element+"\n")
      

