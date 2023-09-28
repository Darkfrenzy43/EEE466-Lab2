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

        # Hard code server address for now
        self.server_address = ('localhost', 9000);

    def run(self):
        """

        Upon initialization, connect to server.
        Prompt user for input to send as commands to server.

        :return: The program exit code.
        """

        print("CLIENT STATUS: Client started. Looking for server to connect to...")

        # Upon initialization, connect client to the server
        self.comm_inf.initialize_client(self.server_address[0], self.server_address[1]);

        # Client main loop:
        while True:

            # Getting user input (stripped of whitespace)
            user_input = input("\nType in a command to send to server: \n> ");

            # Send user input to server
            self.comm_inf.send_command(user_input);

            # Wait for a server response, decode received msg accordingly:
            # "TOO MANY ARGS" --> client sent too many args to the server.
            # "UNRECOG COMM"  --> client sent an unrecognizable command to server.
            # "NONEXIST PATH" --> client sent a non-existent file path to server.
            server_resp = self.comm_inf.receive_command();
            if server_resp == "TOO MANY ARGS":
                print(f"\nCLIENT SIDE ERROR: Last command had too many arguments. Follow format <command,file_name>.");
                continue;
            elif server_resp == "UNRECOG COMM":
                print(f"\nCLIENT SIDE ERROR: Last command sent unrecognized by server. Choose either <get> or <put>.");
                continue;
            elif server_resp == "NONEXIST PATH":
                print(f"\nCLIENT SIDE ERROR: Last command had a nonexistent file path. Verify and try again.");
                continue;






    # EXAMPLE METHOD - lol do we even need this
    def send_cmd(self, command: str, param: str = ""):
        pass

    # EXAMPLE METHOD
    def parse_cmd(self, input_str: str):
        pass


if __name__ == "__main__":
    # Your program must be able to be run from the command line/IDE (using the line below).
    # However, you may want to add test cases to run automatically.
    sys.exit(FTClient().run())

