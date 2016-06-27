import random
import urllib
import urllib2


def check(ip,user,password):

#url open
    url = str("http://" + ip + "/systemGeneralConfig.html")
    password = " ".join(password)

    values = { 'Login': user,'Password': password, 'submit': 'Sign+In' }
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
    if "IP Interfaces" in result:
        returnmsg =  ip + " - Login OK <" + user + " / " + password + ">"
    else:
        returnmsg =  ip + " - Login Fail <" + user + " / " + password + ">"

    return returnmsg
