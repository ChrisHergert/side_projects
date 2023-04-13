from pprint import pprint
from socket import *
import configparser, os, random, select, sqlite3, sys, time

def printsend(connfd, msg):
    connfd.send(msg)
    print(msg)

# System settings
os.system("cls")
file_path=os.getcwd()

# Configure parser
parser = configparser.ConfigParser()
parser.read(f"{file_path}/config.ini")

if __name__=="__main__":
    #Initialize variables
    connections = []

    # Console logging
    print(f"Made it to {file_path}")
    print(parser["DEFAULT"]["server_port"])

    # Socket setup
    s = socket(AF_INET, SOCK_STREAM) #Create a socket
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)   #Set socket options --> SOL_SOCKET level, so that the action is protocol-agnostic
    s.bind(("",parser.getint("DEFAULT", "server_port")))    #Bind the socket to a port from the configs
    s.listen(parser.getint("DEFAULT", "server_accepted_connections"))

    # Initiate server loop.
    for i in range(parser.getint("DEFAULT", 'loops')):

        # If there are no connected users, wait until someone connects
        if not connections: 
            print("Waiting for connections")
            cl_x, addr_x = s.accept()
            connections.append({cl_x:random.randint(1,5000)})
            printsend(cl_x, "User connected")
        else:
            pass

    s.close()
#'''