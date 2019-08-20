import Icodeparser as cd
import filter_lib as fb
import dictunique as du






    
#C:\\Users\\ravisand\\Desktop\\Iproject\\Parsing_code

codepath = input ("enter the path to parse :")
cd.parse (codepath)
fb.dependency()
du.dictunique()
