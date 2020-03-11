import requests
import os
import hashlib
import sys
import time
import shutil

url_malware = 'http://127.0.0.1:8000/api/check_malware/'
url_benign = 'http://127.0.0.1:8000/api/check_benign/'
ftypes = ["Malware","Benign"]
files_type = str(input("Enter the type of files (Malware or Benign) >>> "))

if(files_type not in ftypes):
    sys.exit(1)

if(files_type == "Malware"):
    url = url_malware
elif(files_type == "Benign"):
    url = url_benign
else:
    pass


#return SHA 256 of the file
def sha_256(file):
    sha256_hash = hashlib.sha256()
    with open(file,"rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def send_file_to_server(file):
    hash = sha_256(file)  
    file_name = os.path.basename(file)
    print("Filename >>> ",file_name)
    file_size = os.path.getsize(file)
    PARAMS = {'hash':hash,'file_name':file_name,'file_size':file_size} 
    print("             Sending ",file_name)
    r = requests.get(url = url, params = PARAMS) 
    return r.text
      

def getListOfFiles(files_dir_source):
    listOfFile = os.listdir(files_dir_source)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(files_dir_source, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)
                
    return allFiles        



def main():

    files_dir_source = str(input("Enter the directory in which files are stored (eg : /home/ubuntu/Files/) >>> "))
    files_dir_destination = str(input("Enter the directory in which files has to be transfered (eg : /home/ubuntu/Files/) >>> "))

    listOfFiles = getListOfFiles(files_dir_source)
    
    print("_______________________________________________________________________________________")
    for file in listOfFiles:
        if file.endswith('.exe'):
            response = send_file_to_server(file)
            if (files_type == "Benign"):
                if (response == "Duplicate") or (response == "Malware"):         
                    if (response == "Duplicate"):
                        print("\t \t {} already exists in the benign database .".format(file))
                    elif(response == "Malware"):
                        print("\t \t {} is a malware  .".format(file))
                    else:
                        pass
                    print("\t \t removing {}".format(file))

                    os.remove(file)
                elif (response == "Benign"):
                    print("\t \t Added {} to the  benign database .".format(file))
                    new_filename = files_dir_destination+str(sha_256(file)) + ".exe"
                    shutil.move(file,new_filename)
                else:
                    print("Error encountered !! ")

            else:
                if (response == "Duplicate") or (response == "Benign"):
            
                    if (response == "Duplicate"):
                        print("\t \t {} already exists in the malware database .".format(file))
                    elif(response == "Benign"):
                        print("\t \t {} is benign .").format(file)
                    else:
                        pass
                    print("\t \t removing {} ".format(file))

                    os.remove(file)
                elif (response == "Malware"):
                    print("\t \t Added {} to the  malware database .".format(file))
                    new_filename = files_dir_destination+str(sha_256(file)) + ".exe"
                    shutil.move(file,new_filename)
                else:
                    print("Error encountered !! ")
            print("_______________________________________________________________________________________")


    

    print('Completed')

       
        
if __name__ == '__main__':
    main()
