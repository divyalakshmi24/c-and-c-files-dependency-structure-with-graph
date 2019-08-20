import re
import csv
import os

dictoffile = {}

def parse(path):
    
#    dictoffile = {}
    for files in os.listdir(path):
        os.chdir(path)
        if files.endswith(".cpp"):
            print(" \n parsing the program file... {}".format(files))
            outfile = open (files,'r')
            dependency_list = list()
            dictoffile[files] = dependency_list
            for item in outfile.readlines():
#        
                if re.search(r'[#]include\s*.(\w*)',item):
                            result1 = re.findall(r'[#]include\s*.(\w*)',item)
                            dependency_list.extend(result1)
#                            
        else:
            p = (os.path.join(path, files))
            if os.path.isdir(p):
                print(" \n current working directory is : \n\n",p)
                parse(p)
            else:
                continue
            
    print("\n\n file name: list of dependencies are :\n\n",dictoffile)
            

# writing current dependencies to file
                
with open('C:/Users/ravisand/Desktop/Iproject/dependencies.txt', 'a',newline='') as target:
  writer = csv.writer(target,dialect ='excel', delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
  for key, value in dictoffile.items():
       writer.writerow([key, value])

