
#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

#banner of script
print (red+"""
~|~                            |       
 |   /~~||/~\ /~\   |/~\/~\/~\~|~      
_|_  \__||   |   |  |   \_/\_/ |       
                                       
~~|~~    ||                            
  |/~\/~\||~~\\  /|~~\|/~\/~\/~~/~/(~(~
  |\_/\_/||__/ \/ |__/|   \_/\__\/__)_)
              _/  |                    
              tool by i am root visit
              my Facebook account lord om 
              rsa or i am root
  
                              
                              
                                                      v 1.0
"""+red)
import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)
import os
print(os.system('ipconfig'))

# Importing random to generate
# random string sequence
import random
   
# Importing string library function
import string

def rand_pass(size):
        
    # Takes random choices from
    # ascii_letters and digits
    generate_pass = ''.join([random.choice( string.ascii_uppercase +
                                            string.ascii_lowercase +
                                        string.digits)
                                            for n in range(size)])
                            
    return generate_pass
   
# Driver Code 
password = rand_pass(10)
print(password)