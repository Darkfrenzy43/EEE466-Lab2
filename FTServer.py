
from enum import Enum;

import os
import sys
from EEE466Baseline.TCPFileTransfer import TCPFileTransfer as CommunicationInterface

# DO NOT import socket

""" 
    Notes:
    
        1. Ensuring we get proper input from the user is pretty simple. If the number of elements that we parse
        is more than 2 (meaning we get something more than "command,file_name"), then obviously that is bad input.
        Furthermore, once the command is parsed, first we check the command portion if it s valid command. Then 
        we check the file_name if it is a valid file path (using os.path.exists()). If any of these are violated,
        then we stop processing the given command and continue execution according to the lab instructions.
        
        2. We'll be allowing white spaces in between the command elements. This means that "command,file_name" is valid,
        in addition to "  command   ,   file_name ". 
        
        3. Side note: I'm getting a lot of "pycharm suggests you turn a class method that doesn't use <self> in the
        method body into static" suggestions. We could, however I'm choosing not to in order to not introduce
        another factor of static class methods into the code. It wouldn't exactly hurt having these methods in
        question still remain as class methods. 

"""

# Making an enum class that tracks errors
class ServerErrors(Enum):
    UNRECOG_COMM = 0;
    NONEXIST_PATH = 1;


class FTServer(object):
    """
    This class creates a server object to send and receive files with a client. It can use different interfaces that
    allow for commands and files to be sent using different transport protocols.
    """

    def __init__(self):
        self.comm_inf = CommunicationInterface()

        # Hard code server port for now
        self.server_source_port = 9000;

    def run(self):
        """

        Currently laying out what I want to do with program.

        :return: The program exit code.
        """

        # Upon initialization, open port 9000 on server and wait for connections from clients.
        self.comm_inf.initialize_server(self.server_source_port);
        self.comm_inf.establish_server_connection();

        # Server main loop:
        while True:

            # Wait to receive a command from the client
            print("\nSERVER: Waiting to receive command from client... ", end = "");
            client_command = self.comm_inf.receive_command();
            print(" command received.");

            # Parse command into an array of strings.
            parsed_command = self.parse_command(client_command);

            # Check if there was parsed_command empty - if so, means that
            # client sent too many arguments. Re-prompt client.
            if len(parsed_command) == 0:

                # Send to client here a reply notifying error and to retry.
                print(f"SERVER SIDE ERROR: Too many arguments received. Try again.")
                self.comm_inf.send_command("TOO MANY ARGS");
                continue;


            # Decode the array and handle decoding errors accordingly (refer Notes 1).
            # If error, notify client and restart main server loop.
            result = self.decode_and_execute(parsed_command);
            if result == ServerErrors.UNRECOG_COMM:
                print("SERVER SIDE ERROR: The inputted command is unrecognized. Try again.");
                self.comm_inf.send_command("UNRECOG COMM");
                continue;

            elif result == ServerErrors.NONEXIST_PATH:
                print("SERVER SIDE ERROR: The inputted file path does not exist. Try again.");
                self.comm_inf.send_command("NONEXIST PATH");
                continue;


    # EXAMPLE METHOD
    def parse_command(self, in_command):
        """ Function receives in a raw client command. Parses it, and returns
        the parsed words in an array if it does not violate conditions (2 elements or less).

        If parsed more than 2 elements, returns nothing to indicate error.

        Args:
            <in_command : string> : The raw string that contains the command sent by the client.
        """

        # Remove all whitespaces (refer to Notes 2), and parse command
        parsed_command = in_command.replace(" ", "").split(',');

        # If more than 2 elements in parsed_command, return empty list indicating error (refer to Notes 1).
        # Otherwise, return the parsed commands
        if len(parsed_command) > 2:
            return [];
        else:
            return parsed_command;


    def decode_and_execute(self, parsed_command):
        """ Function receives an array that contains the parsed client's command.
        Depending on what was inputted, decode and execute the command according to the lab instructions.
        If parsed_command was something unrecognized (command unrecognized or file_path doesn't exist), return true
        indicating that an error occurred.

        Args:
            <parsed_command : [string]> : An array of strings of the parsed command that satisfies the conditions.
            Returns: returns enum value UNRECOG_COMM when command unrecognized, returns enum value NONEXIST_PATH
            when the file path does not exist.
        """

        # Unpack parsed_command (since it looks cleaner)
        this_command, this_path = parsed_command[0], parsed_command[1];

        # Making array of valid commands here
        command_list = ['put', 'get'];

        # Check if command is valid and if the path exists. Return error status accordingly to main.
        if this_command not in command_list:
            return ServerErrors.UNRECOG_COMM;

        if not os.path.exists(this_path):
            return ServerErrors.NONEXIST_PATH;

        # Do things here depending on the job sent job...
        print("\nCall functions that do stuff here...");

if __name__ == "__main__":
    # Your program must be able to be run from the command line/IDE (using the line below).
    sys.exit(FTServer().run())
