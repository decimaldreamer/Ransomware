from Crypto.Util import randpool
from Crypto.Hash import SHA256
from Crypto.Hash import SHA512
import random
import socket
import sys

print(""""

        SqLastic Software
               
               
               

""")
host = '127.0.0.1'
port = 443
DIRR = input("                ÞÝFREYÝ GÝRÝN: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(1)

    
def sha512_random_line(line):
    hasher = SHA512.new(line)
    return hasher.digest()    
    
def random_line(afile):
    lines = open(DIRR).read().splitlines()
    myline = random.choice(lines)
    return myline

def getKey(password):
    hasher = SHA256.new(password)
    return hasher.digest()
    
def get_connection_keys():
    with open('connection_keys.txt') as txt:
        content = txt.readlines()
        return content
    

def generate_random_alpha_string():
    return ''.join(random.choice('0123456789ABCDEF') for i in range(16))
    
print("            Zaten o portta çalýþýyor." % port)

def main(): 
    while 1:
        clientsock, clientaddr = s.accept()
        data = clientsock.recv(100000)
        data = data.decode("utf-8")
        data = str(data)
        clientAddr = str(clientsock.getpeername())
        set_keys = get_connection_keys()
        falseKey = False
        print("Alýnan: ", set_keys)
        print("Gönderilen: ", data)
        if data not in set_keys:
            print(clientAddr + " baðlantý yanlýþ. " + data)
            print("Terminating connection. ")
            terminate = bytes("FalseKey")
            clientsock.send(terminate)
            clientsock.close()
            falseKey = True
        if data in set_keys and falseKey == False:    
            Password = random_line(DIRR)
            with open("clients.txt", "a") as text_file:
                print("Wrote    " + str(clientAddr)+ " : " + str(Password) + " : " + str(data) + "\n")
                print("Key:"+ Password)
                text_file.write("\n" + clientAddr + ":" + Password + ":" + data + "\n")
                text_file.close() 
            print("got connection from ", clientsock.getpeername())
            clientsock.send(bytes(Password, 'utf-8'))
# clientsock.send(encryptDirr)
            print('Sent KEY: ' , Password , ' to: ' , clientaddr)
            clientsock.close()
            print("Client socket closed. ")
            
main()