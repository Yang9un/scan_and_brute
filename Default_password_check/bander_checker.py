from modules import *
import urllib
import urllib2
import httplib
import requests

def bander_check_requests(ip, user, password):
    url = str("http://" + ip)
    try:
        result = requests.get(url)
        result.encoding = 'UTF-8'
	result = result.text
    except requests.exceptions.HTTPError as e:
        error =  ip + ' - We failed whit error code - %s.' + str(e)
        result = ip + "other" + error
#    print result
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

    elif "BelAirLogo.jpg" in result:
        bander = "BelAir"
        brute_result =  module__belair_wifi.check(ip,user,password) + " - " + bander

    elif "401" in result:
        bander = "Login to Basic Authorization"
        brute_result =  module__basic.check(ip,user,password) + " - " + bander

    else:
        bander = "Other"
        brute_result = ip + " - No Match Banders & Check to basic Auth" + " - " + bander

    print brute_result
    return brute_result
