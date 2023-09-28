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



        :return: The program exit code.
        """

        # Upon initialization, open port 9000 on server and wait for connections from clients.
        self.comm_inf.initialize_server(self.server_source_port);
        self.comm_inf.establish_server_connection();

        # Waiting to receive a command from the client...
        client_comm = self.comm_inf.receive_command();
        print(client_comm);



    # EXAMPLE METHOD
    def parse_command(self, in_command):
        """ Function receives in a raw client command. Parses it, and
        TODO: THIS PART NOT DECIDED YET. how we notify the server this is what is wanted.

        Do we wanna have the commands get handled and executed from here? If so, might need to rename function"""

        # Use a delimiter to parse command
        parsed_command = in_command.split(',');

        # Throw error if we got more than 2 elements in parsed_command (meaning we got to many arguments)
        if len(parsed_command) > 2:
            print("YOO ERROR: dawg, too many arguments in the command fam.");

        # Do something here for unrecognized commands too.




if __name__ == "__main__":
    # Your program must be able to be run from the command line/IDE (using the line below).
    sys.exit(FTServer().run())
