import os
import sys
from EEE466Baseline.TCPFileTransfer import TCPFileTransfer as CommunicationInterface

# DO NOT import socket

"""
    Notes:
    
        1. Just an interesting observation I've made when we're getting files from the server. I added code that 
        verifies if we actually did receive a particular file from the server and placed it into the client's Receive
        folder, because when I ended up calling "get, server_text_01.txt" and subsequently "get, server_text_02.txt",
        nothing would change in pycharm's Project Explorer window, but until I quit the program then the Project
        Explorer populates and I see that the client's Receive folder contains the requested files. Seems like pycharm
        doesn't automatically update the Project Explorer until the current program it is executing terminates.
        Accordingly, to ensure that we really did receive the files, I do an extra check on the client side if
        we actually have the files in the Receive directory, even if pycharm hasn't updated to reflect accordingly. 

"""


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



            # I think we're going to need to capture the input and clean it up on our side too.



            # Wait for a server response, decode received msg accordingly:
            # "TOO MANY ARGS" --> client sent too many args to the server.
            # "UNRECOG COMM"  --> client sent an unrecognizable command to server.
            # "NONEXIST PATH" --> client sent a non-existent file path to server.
            # "PUT ACK" --> server acknowledges the put command it was sent. Prep client to send file.
            # "GET ACK" --> server acknowledges the get command it was sent. Prep client to receive file.
            # "NO PATH" --> client had sent a put/get request, but without specifying a file path.
            # "QUIT ACK" --> server acknowledges the quit command that was sent. Prep client to quit as well.
            # "QUIT INVALID" --> client had sent the server arguments with the quit command. Server refused.
            server_response = self.comm_inf.receive_command();
            match server_response:

                case "TOO MANY ARGS":
                    print(f"\nCLIENT SIDE ERROR: Last command had too many arguments. Follow format <command,file_name>.");
                    continue;

                case "UNRECOG COMM":
                    print(f"\nCLIENT SIDE ERROR: Last command sent unrecognized by server. Choose either <get> or <put>.");
                    continue;

                case "NONEXIST FILE":
                    print(f"\nCLIENT SIDE ERROR: Requested file does not exist in "
                          f"server database. Verify and try again.");
                    continue;

                case "GET ACK":

                    # Parse the command on client's side to get the file name sent to carry out get/put requests
                    parsed_command = self.parse_command(user_input);
                    file_name = parsed_command[1];
                    client_file_path = "Client\\Receive\\" + file_name;

                    # Receive the sent file and place in Client\Receive\ directory
                    self.comm_inf.receive_file(client_file_path);

                    # Verify here if client received the file (refer to Notes 1)
                    if os.path.exists(client_file_path):
                        print("CLIENT STATUS: Requested file confirmed received in client database.");
                    else:
                        print("CLIENT SIDE ERROR: Requested file failed to be placed in client database.");


                case "PUT ACK":
                    pass;

                case "NO FILE":
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


if __name__ == "__main__":
    # Your program must be able to be run from the command line/IDE (using the line below).
    # However, you may want to add test cases to run automatically.
    sys.exit(FTClient().run())

