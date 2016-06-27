import requests
import random

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

    try:
        result = requests.post(url, data=values)
	print result
        result.encoding = 'UTF-8'
        result = result.text
#	print result
    except requests.exceptions.HTTPError as e:
        error =  ip + ' - We failed whit error code - %s.' + str(e)
        result = ip + "other" + error

#dicision
    if "<title>Please Input name" in result:
        returnmsg =  ip + " - Login Fail <" + user + " / " + password + ">"
    else:
        returnmsg =  ip + " - Login OK <" + user + " / " + password + ">"

    return returnmsg
