# Copyright (c) 2012 Jaap Weel.

# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import sqlite3
import os
import os.path
import SimpleHTTPServer
import SocketServer

def get_dropbox_path():
    connection = sqlite3.connect(os.environ['HOME'] + '/.dropbox/config.db')
    cursor = connection.cursor()
    cursor.execute("SELECT value FROM config WHERE key='dropbox_path'")
    return cursor.fetchall()[0][0]

def get_password_path(dropbox_path):
    for root, dirs, files in os.walk(dropbox_path):
        short = os.path.basename(root)
        if short == '1Password.agilekeychain':
            return root

def run_webserver(path, port=8000):
    os.chdir(path)
    print path
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    httpd = SocketServer.TCPServer(("", port), Handler)
    httpd.serve_forever()

def main():
    dropbox_path = get_dropbox_path()
    password_path = get_password_path(dropbox_path)
    run_webserver(password_path)

if __name__ == '__main__':
    main()
