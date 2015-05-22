import os
import os.path
os.chdir('d:')
for i in range(1,101):
    myvar = 'folder'+str(i)
    myval = 'text' + str(i)
    os.mkdir(myvar)
    complete_name = os.path.join('d:'+myvar,myval+".txt")
    file1=open(complete_name,"w")
                                 
    
    
    
