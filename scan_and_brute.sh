#!/bin/bash

help()
{
	echo "Usage: $0 [command] [interval]"
}

iprange=$1

echo "iprange:$iprange"

nmap $iprange -p80 --open -oG - | awk '/80\/open/{print $2}' > result.txt
python default_password_checker.py