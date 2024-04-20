import zipfile
import time

folderpath = input("path to the file: ")
zipf = zipfile.ZipFile(folderpath)
global result
result = 0 
global tried
tried = 0 
global c 
c = 0

if not zipf : 
    print("the zipped file/folder is not password protected! You can successfully open it")
else:
    wordListFile = open("wordlist.txt","r",error = "ignore")
    body = wordListFile.read().lower()
    words = body.split("/n")

for i in range(len(words)):
        word = words[i]
        try:
                            with zipfile.ZipFile(folderpath,'r') as zf:
                                zf.extractall(pwd=password)
                                print("Success! The password is: "+ guess)
                                endtime = time.time()            
                                result = 1                       
                                break                       
        except:
                pass
                if result == 1:
                        break                           #If the password is found break from j for loop
                if result == 1:
                    break                               #If the password is found break from k for loop
                if result == 1:
                   break     
        if(result == 0):
           print("Sorry, password not found. A total of "+str(c)+"+ possible combinations tried in "+str(duration)+" seconds. Password is not of 4 characters.")
        else:
            duration = endtime - starttime
            print('Congratulations!!! Password found after trying '+str(c)+' combinations in '+str(duration)+' seconds')
