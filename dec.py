import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

def decrypt(key, filename):
    chunksize = 64*1024
    outputFile = filename[0:len(filename)-7]
    
    with open(filename, 'rb') as infile:
        filesize = long(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)
            


def getKey(password):
    hasher = SHA256.new(password)
    return hasher.digest()
    
                
def allfiles():
        allFiles = []
        for root, subfiles, files in os.walk(os.getcwd() + "\\dir\\"):
                for names in files:
                        allFiles.append(os.path.join(root, names))
        return allFiles

encFiles = allfiles()

def Main():
    password = raw_input("Password: ")
    for file in encFiles:
        try:
            decrypt(getKey(password), file)
            print "\n" + "Decrypted: " + file
        except ValueError:
            print "\n" + file + "   doesn't need decrypted or can't be decrypted"
        

if __name__ == '__main__':
    Main()