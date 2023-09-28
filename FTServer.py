import os
import sys
from EEE466Baseline.TCPFileTransfer import TCPFileTransfer as CommunicationInterface

# DO NOT import socket

""" 
    Notes:
    
        1. I have not yet decided how I want the server to run commands after I parse them. 

"""

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

        # Wait to receive a command from the client
        client_command = self.comm_inf.receive_command();

        # Parse command into an array, if more than 2 args throw error and todo: repeat loop?
        parsed_command = [];

        # Decode the array and execute the request as applicable




    # EXAMPLE METHOD
    def parse_command(self, in_command):
        """ Function receives in a raw client command. Parses it, and returns
        the parsed words in an array if it does not violate conditions (2 elements or less).

        If parsed more than 2 elements, returns nothing to indicate error.

        Args:
            <in_command : string> : The raw string that contains the command sent by the client.
        """

        # Use a delimiter to parse command
        parsed_command = in_command.split(',');

        # Throw error if we got more than 2 elements in parsed_command (meaning we got to many arguments)
        if len(parsed_command) > 2:
            print("YOO ERROR: dawg, too many arguments in the command fam.");
            # Return empty string...

        # Do something here for unrecognized commands too.


    def decode_and_execute(self, parsed_command):
        """ Function receives an array that contains the parsed client's command.
        Depending on what was inputted, decode and execute the command according to the lab instructions.
        If parsed_command was something unrecognized, throw error and todo figure out how this is handled

        Args:
            <parsed_command : [string]> : An array of strings of the parsed command that satisfies the conditions.
        """

        # Decode the parsed command, check for anything unrecognized.


if __name__ == "__main__":
    # Your program must be able to be run from the command line/IDE (using the line below).
    sys.exit(FTServer().run())
