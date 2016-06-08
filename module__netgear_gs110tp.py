import random
import urllib
import urllib2


def check(ip,user,password):

#url open
    url = str("http://" + ip + "/base/main_login.html")
    password = "".join(password)

    values = { 'pwd': password,'login.x': '24', 'login.y' : '4', 'err_flag' : '0', 'err_msg' : '' }
#values = { 'textuser': textuser,'textpass': textpass, 'Submit' : 'Login' }
    data = urllib.urlencode(values)

    try:
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        result = response.read()
    except urllib2.HTTPError, e:
        error =  'We failed whit error code - %s.' % e.code
        return error

#dicision
    if "begin hiding" in result:
        returnmsg =  ip + " - Login OK : ID/PW is <" + "NONE" + " / " + password + ">"
    else:
        returnmsg =  ip + " - Login fail : ID/PW is <" + "NONE" + " / " + password + ">"

    return returnmsg
