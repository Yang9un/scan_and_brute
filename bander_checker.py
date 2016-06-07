import module__ruby_l2
import module__netgear_l2
import urllib
import urllib2
import random

def bander_check(ip, user, password):
    url = str("http://" + ip)
    values = {}
    try:
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        result = response.read()
    except urllib2.HTTPError, e:
        error =  'We failed whit error code - %s.' % e.code
        result = "other" + error


#bander check
    if "Netgear" in result:
        bander = "Netgear"
#        brute_result = "'Netgear' isn't support" + " - " + bander
        brute_result = module__netgear_l2.check(ip,user,password) + " - " + bander

    elif "bgindex.jpg" in result:
        bander = "PSGS"
        brute_result =  module__ruby_l2.check(ip,user,password) + " - " + bander

    else:
        bander = "other"
        brute_result = "No Match Banders" + " - " + bander
    print brute_result

    return brute_result