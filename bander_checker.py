import module__ruby_l2
import module__netgear_l2
import module__netgear_gs110tp
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
    if "GS110TP" in result:
        bander = "Netgear GS110TP"
        brute_result = module__netgear_gs110tp.check(ip,user,password) + " - " + bander

    elif "Netgear" in result:
        bander = "Netgear L2"
        brute_result = module__netgear_l2.check(ip,user,password) + " - " + bander

    elif "bgindex.jpg" in result:
        bander = "PSGS"
        brute_result =  module__ruby_l2.check(ip,user,password) + " - " + bander

    else:
        bander = "other"
        brute_result = "No Match Banders" + " - " + bander
    print brute_result

    return brute_result