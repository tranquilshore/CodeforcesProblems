mail = raw_input().split("@")
at_rate_flag = True
if len(mail) > 2:
    at_rate_flag = False
if at_rate_flag == True:
    username = mail[0]
    onlyusername = False
    if len(mail) == 1:
        onlyusername = True
    else:
        rest = mail[1].split("/")
        hostname = rest[0]
        resource_flag = False

        if len(rest) > 1:
            resource_flag = True
            resource = rest[1]

def UsernameCheck(username):
    if len(username) < 1 or len(username) > 16:
        return False
    for i in username:
        if (ord(i) < 65 and ord(i) > 57) or ord(i) < 48 or (ord(i) > 90 and ord(i) < 97 and i != "_") or ord(i)>122:
            return False
    return True

def HostName(hostname):
    if len(hostname) < 1 or len(hostname) > 32:
        return False
    h_words = hostname.split(".")
    for w in h_words:
        if UsernameCheck(w) == False:
            return False
    return True

def Resource(resource):
    if len(rest) > 2:
        return False
    if UsernameCheck(resource) == False:
        return False
    return True
if at_rate_flag == True:
    if onlyusername == False:
        if resource_flag == False:
            if UsernameCheck(username) and HostName(hostname):
                print "YES"
            else:
                print "NO"
        else:
            if UsernameCheck(username) and HostName(hostname) and Resource(resource):
                print "YES"
            else:
                print "NO"
    else:
        print "NO"
else:
    print "NO"
    


            



