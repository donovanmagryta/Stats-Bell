## This command line app has been tested on Windows only, so it may not work properly on Mac OSX or Linux. ## 
## TUTORIAL: ##
## 1. download and install Python 2.7.x from python.org  - Make sure you enable "add to path" during installation!
## 2. Open up your command line program (on windows it's "cmd.exe"_).
## 3. Type "pip install requests" without quotes and hit enter.
## 4. Type "pip install BeautifulSoup4" without quotes and hit enter.
## 5. Type "pip install pyfiglet" without quotes and hit enter.
## 6. in terminal, cd to the path of this file. for example: "cd c:/users/donovan/downloads" without quotes then hit enter.
## 7. type "python statsbell2.py" and hit enter.
##b 8. The command line app with now run and ask you to pick which website you want to monitor...
## Pick one, then paste the link to the YouTube video, Instructables tutorial, or kickstarter project you want to monitor.
## The app will now monitor the page your selected. When the amount you are monitoring increases, it will beep and disply the new amount.
## To quit the app, just close the command line.

#!/usr/bin/env python
# -*- coding: utf-8 -*-
## import required modules ##
import requests
from bs4 import BeautifulSoup
import time
from pyfiglet import Figlet
## set font and show intro ## 
f = Figlet(font = 'roman')#or use 'roman' font
print("Stats monitoring app")
print("Beeps and displays current pledge or view amount")
## Show menu ##
print (30 * '-')
print ("   M A I N - M E N U")
print (30 * '-')
print ("1. Kickstarter project pledges")
print ("2. YouTube video views")
print ("3. Instructables tutorial views")
print ("4. Facebook Likes")
print (30 * '-')
 
## Get input ###
choice = raw_input('Enter your choice [1-4] : ')
choice = int(choice)
amount = ''
url = raw_input("What is the URL?")
## Setup webpage crawler ##
def pageCrawler():
	global amount
	headers = {
		'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'
	}
	res = requests.get(url, headers=headers)
	soup = BeautifulSoup(res.text, 'html.parser')
	## Based on user's choice, set which section to parse ##
	if choice == 1 :
	    data = soup.find_all(attrs={"class": "green-700 inline-block js-usd_pledged medium type-16 type-24-md"})
	elif choice == 2 :
	    data = soup.find_all(attrs={"class": "watch-view-count"})
	elif choice == 3 :
	    data = soup.find_all(attrs={"class": "count view-count"})
	elif choice == 4 :
	    data = soup.find_all(attrs={"class": "_52id _50f5 _50f7"})
	import re
	outp = re.sub('[^0-9]','', data)
	result = outp[0].text
	## If amount changes, print new amount in big font, and play notification beeps ##
	if amount != result :
		amount = result
		amountbig = (f.renderText(amount))
		#Add newlines to make it seem like the line has updated without newline.
		newl = "\n" * 50
		print(newl)
		print(amountbig)
		print(chr(7))
		print(chr(7))
		print(chr(7))
		time.sleep(1)
		

while 1:
	pageCrawler()
	time.sleep(10)	#check amount every 10 seconds
