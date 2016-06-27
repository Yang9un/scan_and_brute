import urllib
import urllib2
import base64

def check(ip,user,password):

    url = str("http://" + ip + "/base/web_main.html")
    password = " ".join(password)
#    values = {}
#    data = urllib.urlencode(values)
    base64string = base64.encodestring('%s:%s' % (user, password)).replace('\n', '')

    try:
        req = urllib2.Request(url)
        req.add_header("Authorization", "Basic %s" % base64string)
#result = urllib2.urlopen(request)
        response = urllib2.urlopen(req)
        result = response.read()
    except urllib2.HTTPError, e:
        error =  ip + " - Login fail : ID/PW is <" + user + " / " + password + ">"
        return error


#dicision
    if "401 Unauthorized" in result:
        returnmsg =  ip + " - Login OK <" + user + " / " + password + ">"
    else:
        returnmsg =  ip + " - Login Fail <" + user + " / " + password + ">"

    return returnmsg
