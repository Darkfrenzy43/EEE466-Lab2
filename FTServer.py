import os
import sys
from EEE466Baseline.TCPFileTransfer import TCPFileTransfer as CommunicationInterface

# DO NOT import socket


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

        For now, conduct simple tests of getting TCP connection from client

        PLAN: Implement the receivng of commands from the client, conduct command
        parsing on the server side.

        :return: The program exit code.
        """

        # For now, try having the server receive connection from client
        self.comm_inf.initialize_server(self.server_source_port);
        self.comm_inf.establish_server_connection();


        # --- Testing sending discrepancies ---

        print(self.comm_inf.receive_command());
        self.comm_inf.receive_file(".\Server\Receive\client_text_01.txt");



    # EXAMPLE METHOD
    def parse_command(self):
        pass



if __name__ == "__main__":
    # Your program must be able to be run from the command line/IDE (using the line below).
    sys.exit(FTServer().run())
