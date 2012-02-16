# The problem 

1PasswordAnywhere does not work in Google Chrome because Chrome does
not let javascript read from local disk, ever, even if the page is
served over file://


# The solution

This script runs a simple webserver on port 8000. It serves the
1Password keychain directory. It finds this directory by searching the
current user's Dropbox for a directory called
1Password.agilekeychain. That's it.


# TODO 

 * Accept connections from localhost only

 * Make keychain directory configurable so it doesn't need to be from
   Dropbox

 * Make port number configurable

 * Make http://localhost:PORT/ go straight to index.html