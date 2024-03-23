import socket
import argparse
import sys
from myHTTPLibrary import *

#demo
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#demo
params = {"color" : "blue", "size" : "large"}

def run_client(host, port):
    conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        conn.connect((host, port))

        #print("Type any thing then ENTER. Press Ctrl+C to terminate")
        while True:
            #test query for demo
            #queriedLine = addQuery("/search", params)
            #test query line
            #print("The queried line is: "+queriedLine)

            line = makeGetRequest("/get", Connection="close")

            request = line.encode("utf-8")
            conn.sendall(request)

            # MSG_WAITALL waits for full request or error
            response = conn.recv(len(request), socket.MSG_WAITALL)
            response = response.decode("utf-8")
            sys.stdout.write(response)


    finally:
        conn.close()


# Usage: python echoclient.py --host host --port port
parser = argparse.ArgumentParser()
parser.add_argument('-method', '-GET', help='HTTP request method')
parser.add_argument("--host", help="server host", default="httpbin.org")
parser.add_argument("--port", help="server port", type=int, default=80)
args = parser.parse_args()

run_client(args.host, args.port)


