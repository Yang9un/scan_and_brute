from modules import *
import bander_checker
import os
import sys


dir = list(sys.argv)
#print dir[1]


#file open and list create
def file_open():
    global pre
    pre=[]
    f = open(dir[1], 'r')
    pre = f.readlines()
    f.close()

    pre = [pres.replace("\n","") for pres in pre]

#    print pre_11
#    print pre_12
#    print pre_21
#    print pre_22
#    p = [password.replace("\n","") for password in p]
#    len_ip = len(ip)
#    len_u = len(u)
#    len_p = len(p)


def brute(attack_list):
#    print attack_list
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
#    print pre
    brute(pre)
#    print str(sys.argv)
#    print "Scanning...\n"



if __name__ == '__main__':
    main()