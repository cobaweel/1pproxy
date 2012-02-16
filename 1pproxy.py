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
