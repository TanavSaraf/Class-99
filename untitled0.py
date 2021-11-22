import os
import shutil
path=input("Enter a directory name to sort it")

listOfFiles=os.listdir(path)
for i in listOfFiles :
    name,ext=os.path.splitext(i)
    if(os.path.exists(path+"/"+ext[1:])):
        shutil.move(path+"/"+i,path+"/"+ext[1:]+"/"+i)
    elif (ext=="") :
        continue
    else :
        os.mkdir(path+"/"+ext[1:])
        shutil.move(path+"/"+i,path+"/"+ext[1:]+"/"+i)
        
    
    
    