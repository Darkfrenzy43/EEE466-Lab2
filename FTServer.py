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

        # Receive a message from a user for now...
        print("TCPSERVER STATUS: Waiting to receive msg from client...");
        recv_msg = self.comm_inf.receive_command();
        print(f"TCPSERVER STATUS: Received msg is {recv_msg}.");

        # Send some random msg to the server for now
        self.comm_inf.send_command("""
        
        
                                                   x xxxx
                                             x x x         x
                                        x xx                x
                                 x  xxx
                             x
xx                   x  x  x                                  x
               x  x
             x                                                  x
   xx xx  x
      x
                                                                  x

         x                                                         x
                                                                     x
            x

              x                                                        x

                x                                                       x

                                                                         x
                                                                      xxx
                    x                                              xxx     x
                                                              xx x          xx
                                                            xx
                      x                                 xxxx                 x
                                                    x x                      xxx
                        x                       x x                        xxx x
                                           x  x                   x     x       x
                          x             x x                   x x
                                    x x                  x xx                    x
                              x  x                   x x                           x
                           xx                     xx                               x
                           x                  x x                                   x
                           x            x   x                                       x                                                                           x
                                                                                      x                                                                     x x x x
                            x      x                                                   x                                                                x  x
                              xxx                                                       x                                                        xxxx
                                                                                         x                                                 x xx x
                            x                                                             x    x                                 x  x xx
                                                                                           xxx                               x xx
                            x                                                                xx  x                     xxxxx
                                                                                               xxx               x x x
                            x                                                                    xx     x     x
                                                                                                  x   x
                             x                                                            xx   x  x
                                                                                x    x
                             x
                                                                xxx xxx xxxxxxx xxxxxx   x xxxxx
                             x                               xxx       x                        x xx
                             x                         xxxx x       x                               x x
                                                   x xx       xx  x                                    xx x
                             x                   xx      x  x                                              x
                             x                x x    x  x                       xx x                        x x x
                             x             xx    x                                   x                           xxx x
                                         xx                                            xx                            x x
                             x       xxxx                                                xx                              x        xx
                             x    x  x                                                    x                                          x
                             x x x  xx                                                    x                                x          xx
                        x           xxx xxx                                             xxx                                 x          x
                     x             x        xx  x x                                    x                                     x          x
               xx                xx                xx xx x xxxx xxx xxx x x xxx xx xxxxx    xxxxxxxxxxxx x     xx             x         x
            xx                                         x                              x                           xxxxxxxxx    x x x x xx
         xx                     x                      x                         xxxx xxx              x                   xxxx x
                               x                       x                        xx xx xxxx             x                   xxxx  x
                               x                       x                      xxxxxxx xxxx             x                  xxxxxx xx
                              x                         x                  xx     xxxxxx x                               xxxx xx xx
                              x                         xx                 x  x    xxxx x              x                 xx  x x xx
                              x                          x                 xx x  xxxxx                 x                xx   x xx  x
                              x                           xx                  xxxx                                     xxxxxxxxxx  x
                              x                             xx               xxx                                       xxxxxxxxx   x
                              x                               xx xxx x x xx x                            x              xx xxx     x
                              x                                                                            x x             xx      x
                               x                                               x x xx xx xxxx x               xxx        xx       x
                               x                                             xx                xxx               xxxxxxx          x
                               xx                                           x                     xx                              x
                                x                                        xx                        xx                             x
                                 x                                      xx                           x                            x
                                 x                                     x                              x                          x
                                                           x           x                               x                         x
                                                                      x
                                 x                          x        x                                 x                         x
                                  x                                  x                                 x                         x
                                  xx                        x        x             xxx     x            x                       x
                                   xx                               x          x x    x    x            x                       x
                                     xx                     x      x       xxxx                         x                      x
                                      x x                          x     xx                x            x              x
                                         x x                x     x    x                   x            x             x       x
                                              x                   x   x                    x                     xxxx        x
                                               xx           x     x  x                     x           xx       xx          x
                                                  xx        x     x x                      x           x      x            x
                                                     xx                                               xx    x
                                                       x x  x     xx                       x             x x             xx
                                                         x x x   x                         x         x x                x
                                                             xxxx                          x        x                  x
                                                   x            x                          x      x                  x                                                                                 ┌────────────────────────────────────────────────────┐
                                                   x                   x  x                 x  xx                  x                                                                                   │                                                    │
                                                  xx                          x  x          xxx               x x                                                                                      │                                                    │
                                                  x                                  x    x  x          x    x                                                                                         │                                                    │
                                                 xx                                            x xxx xx                                                                                                │            │                                       │
                                                 x                                                                                                                                                     │    │       │     │                 │               │
                                                x                                                                                                                                                      │    │       │     │                 │               │
                                               x                                                                                                                                                       │    │       │     │ │               │               │
                                               x                                                                                                                                                       │    │       │     │ │               │               │
                                              x                                                                                                                                                        │    │       │     │ │               ├───┬──────┐    │
                                             x                                                                                                                                                         │    │       │     │ │               │   │      │    │
                                             x                                                                                                                                                         │    │       │     ├─┼─────────────┐ │   │      │    │
                                            xx                                                                                                                                                         │    │       │     │ │             │ │   │      │    │
                                                                                                                                                                                                       │   ┌┤       │     └─┼────┬──      │ │   │      │    │
                                           x                                                                                                                                                           │   ││       │       │    │        │ │   │      │    │
                                          x                                                               xxx xx                                                                                       │   ├┴───────┼───────┼─── │        │ │   │      │    │
                                          x                                xx                          xx      x                                                                                       │   │        │       │    │        │ │   │      │    │
                                                                          x  x      xxx              xx       xx       xx x  xxx                                                                       │   │        │       │    │        │ │   │      │    │
                                                                      x   x    x    x  x           x         x      x x         x                                                                      │   │        │       └────┼───     │ │   │      │    │
                                                                      x  x         x    xx        x         xx       x           x                                                                     │   │        │            │        │ │   │      │    │
                                                                         x     x  x              x         xxx       x           x                                                                     │   │        │            │        │ │   │      │    │
                                       x                               xx       xx        x               xx x       x           x                                                                     │   │        │            │        │ │   │      │    │
                                                                                xx         x     x       xx  x       x            x                                                                    │   │        │            │        │ │   │      │    │
                                                                       xx       x          x     x      xx           x            x                                                                    │   │        │            │        │ │   │      │    │
                                                                                x          x     x           xx      x            x                                                                    │   │   │    │            │        │ │   │      │    │
                                    x                                           x          x     xx   xx      x      x            x                                                                    │   │   │    │            │        │ │   │      │    │
                                                                        x                  x       xxx        xx                  x                                                                    │   │   │    │            │        │ │   │      │    │
                                   x                                    x                                            x            x                                                                    │   │   │    │      │     │        │ └───┼────  │    │
                                  x                                     x                                                                                                                              │   │   │    │      │     │        │     │           │
                                x                                       x                                                                                                                              │   │   │    │      │  ───┼─┐      │     │           │
                                                                                                                                                                                                       │   │   │    │      │     │ │      │     │           │
                                x                                                                                                                                                                      │   │   │    │      │     │ │      │     │           │
                               x                                                                   x                                                                                                   │   │   │    │      │     │ │      │     └────       │
                              x                                                                    x                                                                                                   │   │   │    │      │    ─┘ │      │                 │
                                                                                                   x                   xx                                                                              │   │   └────┼────  │       │      │                 │
                              x                                                                    x                  x x                                                                              │   │        │      │       │      │                 │
                              x                                                                    x                x   x                                                                              │   │        │      │       │      │                 │
                              x                                                                    x              x     x                                                                              │   │        │      │       │      │                 │
                                                                                                                 x                                                                                     │   │        │      │       │      │                 │
                             x                                                                     x            x                                                                                      │   │        │      └───────┼────  │                 │
                             x                                                           xxxxx  x   x xx xxx    x                                                                                      │   │        │              │      │                 │
                                                                                                                                                                                                       │   │        └──────────────┴──────┴───────────────  │
                            xx                                       x                             x            x                                                                                      │   │                                                │
                            x                                        x          xx     x                                                                                                               │   └──────────────────────                          │
                           x xx                                       x         xx     x           x            x   x    x        x  xx                                                                │                                                    │
                             x  x                                                     x            x           x                                                                                       └────────────────────────────────────────────────────┘
                          x                                            x       x                  xx    x  x     x
                          x x     x                                    x     xx  x xx              x
                          x x        x                                 x    x    xx
                          x x         x                                                                           x
                                       x                                xxx                                       x
                         x  x            x                                                                        xx
                         x  x
                         x                x
                            x               x
                        x
                             x                x
                        x    x
                        x
                             x                  x
                        x
                             x                    x
                              x                    x
                       x                            x
                       x      x                      x
                       x                             x
                              x                      x
                       x       x                      x
                       x                              x
                       x       x                      xx
                       x                               xx
                       x       x
                       x
                       x       x
                       x
                       x        x
                       x
                       x        x
                       xx
                        x        x

                                 x

                                  x
                                  x

                                   x

                                    x
                                    x

                                    x
                                    x

                                     x
                                     x

                                     x
                                      x
                                      x

                                      xx

                                        xx

                                          xx x
                                            x
                                         x   xx
                                         x
                                                xx
                                         x
                                                  x
                                         x          x
                                        x             x
                                        x
                                        x              xx

                                       x                 x

                                       x                  x
                                       x                   x
                                       x
                                       x                    x
                                       x                      x
                                       x                       x
                                       x                        x
                                       x                         x
                                        x                         x
                                        x                         x
                                        x                          x
                                         x                         xx
                                         x
                                          x
                                          x
                                           x
                                           x
                                           x
                                           x
                                           x
    
""");


    # EXAMPLE METHOD
    def parse_command(self):
        pass



if __name__ == "__main__":
    # Your program must be able to be run from the command line/IDE (using the line below).
    sys.exit(FTServer().run())
