# specter
SMTP Password Bruteforcer

### Setup && Install

 **python setup.py**
 
 

### Usage

 **python specter.py -h**

usage: specter.py [-h] --username U --wordlist W --server S --port P

Brute forces SMTP Passwords

optional arguments:
  -h, --help    show this help message and exit

Required Arguments:
  --username U
  --wordlist W
  --server S
  --port P
  
  ## Examples
  
> python specter.py --username "email" --wordlist "wordlist" --server "smtp server" --port "smtp port"

### Problems
Bruteforcing Gmail passwords is only possible if less secure apps is turned on, so you might need to use
you're social engineering skills to get the victim to turn it on.
