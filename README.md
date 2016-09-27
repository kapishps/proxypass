##*For educational purposes only.*

The important thing is to understand that bruteforce and Dictionary attack programs are very easy to make therefore it is always advised to keep long strong passwords.

For eg:-
For an alphanumeric password of length 8 characters even with 10000 pings/sec it would take 9 years to search all possible values. Thats why in real life situations hackers prefer network sniffing, sql injection etc.

###**How to use**

The whole process is done in 3 steps
 1. create a dictionary of words from letters/numbers
 2. extract username from html doc 
 3. use username and pass from above two steps and ping proxy server with login credentials.

####**Step 1:**
Create dictionary of words from letters/numbers.
```python
a=list(bruteforce('0123456789', 5))
```
In above function parameters replace firstpart of string with characters you want to appear in dictionary and second number represents the max length of the string.
For eg:- for a dictionary of 5 letter alphanumeric chaacters
```python
a=list(bruteforce('0123456789abcdefghijklmnopqrstuvwxyz', 5))
```
####**Step 2:**
Extract username from html doc
#####*This is only applicable for Squid proxy using squish*
open [http://yourproxyaddress:8080/squish/?]
 and save the page as html doc. and then using username_extracter.py extract all the usernames and save in a text file.
####**Step 3:**
To start the program specify the path of dictionary (in my case 5dnum.txt)
```python
with open('Temp/5dnum.txt','r') as pwd:
```
and list of usernames (18_usernames.txt) 
```python
with open('Temp/18_usernames.txt', 'r') as usr:
```
and initialise Last.txt with 0 in first two lines.
```python
0
0
```
The Script is optimised to run for long durations handling errors efficiently.
Finally the usernamepassword will be saved in user_pass.txt
