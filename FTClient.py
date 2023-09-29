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
            # "PUT ACK" --> server acknowledges the put command it was sent.
            # "GET ACK" --> server acknowledges the get command it was sent.
            # "NO PATH" --> client had sent a put/get request, but without specifying a file path.
            # "QUIT ACK" --> server acknowledges the quit command it was sent.
            # "QUIT INVALID" --> client had sent the server arguments with the quit command. Server refused.
            server_response = self.comm_inf.receive_command();
            match server_response:

                case "TOO MANY ARGS":
                    print(f"\nCLIENT SIDE ERROR: Last command had too many arguments. Follow format <command,file_name>.");
                    continue;

                case "UNRECOG COMM":
                    print(f"\nCLIENT SIDE ERROR: Last command sent unrecognized by server. Choose either <get> or <put>.");
                    continue;

                case "NONEXIST PATH":
                    print(f"\nCLIENT SIDE ERROR: Last command had a nonexistent file path. Verify and try again.");
                    continue;

                case "PUT ACK":
                    pass;

                case "GET ACK":
                    pass;

                case "NO PATH":
                    print("\nCLIENT SIDE ERROR: Last command was sent without a file path. Ensure to include one.");
                    continue;

                case "QUIT ACK":
                    print("CLIENT STATUS: Server acknowledged quit request. Terminating client execution...");
                    break;

                case "QUIT INVALID":
                    print("\nCLIENT SIDE ERROR: Quit command was sent with an argument. If wish to quit, "
                          "send only <quit>.");




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

