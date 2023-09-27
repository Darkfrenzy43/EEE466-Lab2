import os
import sys
from EEE466Baseline.TCPFileTransfer import TCPFileTransfer as CommunicationInterface

# DO NOT import socket


class FTClient(object):
    """
    This class creates a client object to send and receive files with a server. It can use different interfaces that
    allow for commands and files to be sent using different transport protocols.
    """

    def __init__(self):
        self.comm_inf = CommunicationInterface()

        # Hard code server address fornow
        self.server_address = ('localhost', 9000);

    def run(self):
        """

        For now, conduct simple tests of getting TCP connection to server.

        PLAN: Implement the sending of commands to the server, and having the server
        parse the commands from there.

        :return: The program exit code.
        """

        # For now, try connecting to server
        self.comm_inf.initialize_client(self.server_address[0], self.server_address[1]);

        # # Send some random msg to the server for now
        # self.comm_inf.send_command("FILLER COMMAND");
        #
        # # Receive a message from the server for now...
        # print("TCPCLIENT STATUS: Waiting to receive msg from client...");
        # recv_msg = self.comm_inf.receive_command();
        # print(f"TCPCLIENT STATUS: Received msg is {recv_msg}.");

        # Testing the receiving of a file
        self.comm_inf.receive_file(".\Client\Receive\server_text_02.txt");




    # EXAMPLE METHOD
    def send_cmd(self, command: str, param: str = ""):
        pass

    # EXAMPLE METHOD
    def parse_cmd(self, input_str: str):
        pass


if __name__ == "__main__":
    # Your program must be able to be run from the command line/IDE (using the line below).
    # However, you may want to add test cases to run automatically.
    sys.exit(FTClient().run())

