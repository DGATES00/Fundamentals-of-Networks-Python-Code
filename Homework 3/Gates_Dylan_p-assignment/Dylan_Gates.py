# Author of Assignment
#   Dylan Gates
#   Date: 2/17/18
#   Email: gates.d@husky.neu.edu
#   Task: My client program must verify the validity of messages sent by strictly checking
#   their format to confirm that it abides by the above protoco

#imported the socket library for this program
from socket import *

#IP address that we will be listening to
serverName = '129.10.59.73'

#Port number that is within the range for the server communicate with
serverPort = 12003

#Creating a client socket
clientSocket = socket(AF_INET, SOCK_STREAM)

#This initiates three way handshake so that socket could communicate to
#the server port listed in this program
clientSocket.connect((serverName,serverPort))

#Declaring the format of the HELLO message
Hello_sentence = "eece2450 HELLO 001454712"

#This will send the hello message to the server encoded in utf-8
clientSocket.send(Hello_sentence.encode())

#This while loop will complete protocol problems listed in the assignment
while True:

    #The utf-8 message is taken from server and is converted into a string
    decoded_input = clientSocket.recv(1024).decode()

    #Print out the string that was from the utf-8 message
    print('From the Server:', decoded_input)

    # If the string variable "BYE" is present in the string taken in from the server,
    # store the secret code into the variable "final message"
    if "BYE" in decoded_input:
        final_message = decoded_input[12:]
        print('The Secret flag for this NUID is', final_message)
        break;

    #The input string will be reduced to the neccesary math problem
    math_problem = (decoded_input.replace('ece2540 STATUS ',''))

    #Print out the mathematical expression needed
    print('From Server:', math_problem)

    #This decrlared variable will return the 
    #evaluated string result into an integer
    answer = eval(math_problem)

    #Prints out the result
    print(answer)

    #Converts the variable "answer" into a string; 
    #needs to be sent to the server
    str_answer = str(answer)

    #Send result to the server, but this string is encoded into the utf-8 format
    clientSocket.send(str_answer.encode())

#Once out of the while loop, close th socket connection
clientSocket.close()






