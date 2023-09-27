
# --- Importing Libraries ---

import os
import socket
import math
from constants_file import DeviceTypes

from EEE466Baseline.CommunicationInterface import CommunicationInterface


# --- Defining the class TCPFileTransfer ---

"""
    NOTES: 
        
        1. For now, we'll be making our own "protocol" of how we're sending messages more than 1028 bytes over. 
        Whenever we send a message, we slice up the bytes, let the receiving device know how many slices we're sending
        their way, and then we send the bytes accordingly. The receiving device will receive the first byte telling
        them how many slices to expect, and calls recv() the appropriate amount of times to receive it. 

        2. Decided to implement a send-recv ack msg in the send_and_slice() and recv_and_parse() relations
        since it seems the sender would send the contents of the databyte stream along with the initial
        slice number count, essentially filling up the buffer with data more than the slice number, meaning
        this is something that we can't convert back to an integer and running into an error. Essentially,
        I'm trying to not let them step over eachother by adding an ack in between the two steps. 

    STATUS: 
    1. Implement the sending of files over the network. Might need to do some research (involves opening up files, 
        and sending contents appropriately). 
    2. Implement the reading of commands, and setting up the rest of the program in general
    

"""

class TCPFileTransfer(CommunicationInterface):
    """
    This class inherits and implements the CommunicationInterface. It enables file transfers between client and server
    using TCP.
    """

    def __init__(self):
        """
        This method is used to initialize your Communication Interface object. Class variables are defined here.

        NOTE: class objects default to Device Type TCPCLIENT upon initialization.
        """

        # Setting the device type - default to TCP client
        self.device_type = DeviceTypes.TCPCLIENT;

        # Creating the initial socket (this only gets used by server before receiving TCP connection)
        self.initial_sock = None; #CHANGE NAME???

        # Creating the connection socket only used by the server after receiving connection. Not used by client.
        self.server_connection = None;

        # Creating attribute which contains the address of the client device (only used by Server)
        self.client_addr = None;

        # Creating a server address attribute. Likely will be used by client and server
        self.server_addr = None;


    def initialize_server(self, source_port):
        """
        Performs any necessary communication setup for the server. Creates a socket and binds it to a port. The server
        listens for all IP addresses (e.g., "0.0.0.0").

        NOTE: Switches the object's device type to TCPSERVER.

        :param source_port: port that provides a service.
        """
        #First, change the device type to TCP server
        self.device_type = DeviceTypes.TCPSERVER;


        # Set self.server_addr as a tuple
        self.server_addr = ('localhost', source_port);

        # Call socket(), bind(), and listen() methods for server TCP connections
        self.initial_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        self.initial_sock.bind(self.server_addr);
        self.initial_sock.listen(0); # <-- Unlimited retries for connection

        # Print statement for status
        print(f"{self.device_type} STATUS: Server bounded and listening on port {self.server_addr[1]}...")



    def establish_server_connection(self):
        """
        Accepts incoming connections for the server socket. Not implemented for connectionless protocols.

        The active connection is used to perform send and receive function calls. There should never be more than one
        active connection. If the CommunicationInterface does not have an established connection this method should
        establish one. If there is an existing, established connection this call should close it and create a new one.
        """

        # Stop calling of function if detected not a server
        if self.device_type != DeviceTypes.TCPSERVER:
            print(f"ERROR: Can't establish connection as a server with device type {self.device_type}.");
            return;

        # Call accept() method, wait for a client to connect, and save new connection socket in self.server_sock
        self.server_connection, self.client_addr = self.initial_sock.accept();

        # Print status
        print(f"{self.device_type} STATUS: Server received connection from client at {self.client_addr}.");


    def initialize_client(self, address, destination_port):
        """
        Performs any necessary communication setup for the server. Creates a socket and attempts to connect to the
        server.

        :param address: the address you wish to connect to. (e.g., "localhost","127.0.0.1")
        :param destination_port: the port you want the client to connect to.
        """

        # Stop calling of function if detected not a client
        if self.device_type != DeviceTypes.TCPCLIENT:
            print(f"ERROR: Can't establish a client connection with device type {self.device_type}.");
            return;

        # Set server address attribute
        self.server_addr = (address, destination_port);

        # Create TCP client socket, connect the client to the address and port passed through params
        self.initial_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
        self.initial_sock.connect(self.server_addr);

        # Print status
        print(f"{self.device_type} STATUS: successfully connected to server at {self.server_addr}.")


    def send_file(self, file_path):
        """
        Transfers a file from the local directory to the "remote" directory. Can be used by either client (i.e., in a
        put request), or by the server when receiving a get request.

        This method will need to read the file from the sender's folder and transmit it over the connection. If the
        file is larger than 1028 bytes, it will need to be broken into multiple buffer reads.

        :param file_path: the location of the file to send. E.g., ".\Client\Send\\ploadMe.txt".
        """
        print("TODO implement this method")

    def receive_file(self, file_path):
        """
        Receives a filename and data over the communication channel to be saved in the local directory. Can be used by
        the client or the server.

        This method has a maximum buffer size of 1028 bytes. Multiple reads from the channel are required for larger
        files. This method writes the data it receives to the client or server "Receive" directory. Note: the filename
        must be sent over the wire and cannot be hard-coded.

        :param file_path: this is the destination where you wish to save the file. E.g.,
        ".\Server\Receive\\ploadMe.txt".
        """
        print("TODO implement this method")

    def send_command(self, command):
        """
        Sends a command from the client to the server. At a minimum this includes GET, PUT, QUIT and their parameters.

        This method may also be used to have the server return information, i.e., ACK, ERROR. This method can be used to
        inform the client or server of the filename ahead of sending the data.

        :param command: The command you wish to send to the server.
        """

        # Convert msg into utf-8 bytes
        send_data = bytes(command, 'utf-8');

        # If the current device is a server...
        if self.device_type == DeviceTypes.TCPSERVER:

            # Send message to the client (slice up into 1028 byte msgs if needed)
            self.slice_and_send(self.server_connection, send_data);

        # If the current device is a client...
        elif self.device_type == DeviceTypes.TCPCLIENT:

            # Send message to the server (slice up into 1028 byte msgs if needed)
            self.slice_and_send(self.initial_sock, send_data);



    def error(self, error_msg):
        """
        OPTIONAL error method can be used to display an error to the client or server, or can be used to send
        an error message across an open connection if something fails.

        :param error_msg: The error message you would like to display.
        """
        print("TODO implement this method")

    def receive_command(self):
        """
        This method should be called by the server to await a command from the client. It can also be used by the
        client to receive information such as an ACK or ERROR message.

        :return: the command received and any parameters.
        """

        # Initializing dummy var to remove warnings
        recv_msg = None;

        # If the current device is a server...
        if self.device_type == DeviceTypes.TCPSERVER:

            # Receive the data byte stream from the client
            recv_msg = self.recv_and_parse(self.server_connection);

        # If the current device is a client...
        elif self.device_type == DeviceTypes.TCPCLIENT:

            # Receive the data bytes tream from the server
            recv_msg = self.recv_and_parse(self.initial_sock);

        # Decode and return received command
        return recv_msg.decode();


    def close_connection(self):
        """
        If an unrecoverable error occurs or a QUIT command is called the server and client and tear down the
        connection.
        """
        print("TODO implement this method")


    # ---- Making my own functions ---

    def slice_and_send(self, in_socket, in_data):
        """
        Function slices up message in 1028 byte groupings. The sending device then sends
        the separate messages in order to the device on the other side of the TCP connection.

        ONLY HANDLES STRINGS FOR NOW

        Args:
             <in_socket : socket > : A TCP socket object through which the message is to be sent.
             <in_data : bytes> : The data which is to be sent to the other device in the TCP connection.
             Returns: nothing
        """

        # First, find how many slices of 1028 bytes we are sending
        bytes_len = len(in_data);
        slice_num = math.ceil(bytes_len / 1028)

        # First send the slice number (converted to string, then into bytes for easiest time)
        in_socket.send(bytes(str(slice_num), 'utf-8'));

        # Wait for acknowledgement first before proceeding
        if in_socket.recv(3) == b'ACK': pass;

        # Send the slices of the bytes next
        for i in range(slice_num):

            # Check if sending last slice (is likely not exactly 1028 bytes)
            if i == slice_num - 1:

                start_ind = i * 1028;
                slice_bytes = in_data[start_ind: ]; # Send like this for good practice

            # Otherwise, compute start and end indices and send
            else:

                start_ind = i * 1028;
                end_ind = (i + 1) * 1028;
                slice_bytes = in_data[start_ind : end_ind]

            in_socket.send(slice_bytes);


    def recv_and_parse(self, in_socket):
        """
        Function receives messages of max size 1028 bytes from sender, and reconstructs
        the original message accordingly.

        ONLY HANDLES STRINGS FOR NOW

        Args:
            <in_socket : socket> : A TCP socket object to receive the msg through
            Returns: The reconstructed stream of bytes received in slices from the sender.
        """

        # Creating dummy var to contain total received data
        recv_data = b'';

        # Receive the number of slices from sender (from bytes, conv to str then int).
        # Shouldn't be more than 5 bytes lol
        slice_num = int(in_socket.recv(5).decode())

        # Send acknowledgement that number received
        in_socket.send(b'ACK');

        # Next, call recv() slice_num number of times and receive the slices and reconstruct through concatenation
        for i in range(slice_num):
            recv_data += in_socket.recv(1028);

        return recv_data;








