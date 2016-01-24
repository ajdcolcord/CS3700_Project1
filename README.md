# CS3700_Project1

Austin Colcord and Nick Scheuring

This is the project for creating a socket connection to a server, 
sending and receiving messages, and processing messages received.

High-Level Approach:
    - Accept parameters from the command line
    - Created simple socket connection to the server with hard-coded arguments
    - Replaced the hard-coded arguments with parameters from command line
    - Implemented a parse_message function that decided what types of messages
    were being sent from the server (STATUS, BYE)
    - Created a function to solve the simple math problems
    - Created a loop to solve the math problems until BYE was received
    - Printed out the secret message
    - Verified project specifications were met
    - Implemented SSL connection options

Issues:
    - Did not see that we should include the 'cs3700spring2016' for the messages,
    so we had issues getting any messages from the server
    - SSL issues - EOF errors - was using incorrect port number during execution

Testing:
    - Run through the non-ssl version multiple times
    - Changed the inputs, and number of inputs, to the program
    - Ran the program using different parameter combinations,
    ensured to fulfill project requirements
