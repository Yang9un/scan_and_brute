import random
import urllib
import urllib2


def check(ip,user,password):
#randstrt create
    a = []

    for i in range(1, 17):
        r = str(random.randint(1, 9))
        a.append(r)

    randstr =  "0." + "".join(a)


#url open
    url = str("http://" + ip + "/login")
    password = " ".join(password)

    values = { 'textuser': user,'textpass': password, 'Submit' : 'Login', 'randstr' : randstr }
#values = { 'textuser': textuser,'textpass': textpass, 'Submit' : 'Login' }
    data = urllib.urlencode(values)

    try:
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        result = response.read()

    except urllib2.HTTPError, e:
        error =  ip + ' - We failed whit error code - %s.' % e.code
        return error

#dicision
    if "<title>Please Input name" in result:
        returnmsg =  ip + " - Login OK <" + user + " / " + password + ">"
    else:
        returnmsg =  ip + " - Login Fail <" + user + " / " + password + ">"

    return returnmsg
