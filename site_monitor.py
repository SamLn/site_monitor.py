#site gatherer
import requests 
#parser
from bs4 import BeautifulSoup 
#timer
import time
#mail notification
import smtplib

#choose site
url = raw_input("enter URL https:// needed: ")
headers = {'User-Agent': 'Chrome/39.0.2171.95'} 
response = requests.get(url, headers=headers)
#if response contains cookies
response.cookies ['example_cookie_name']
#send cookies to server
url = "exampleurl" 
cookies = dict(cookies_are='working')

response = requests.get(url, cookies=cookies)
response.text
#html parser
Firstrun = BeautifulSoup(response.text, "html.parser")
Lookagain = BeautifulSoup(response.text, "html.parser")
	
while True:
#if no change
	if str(Firstrun) == str(Lookagain):
		print "meow"
		response = requests.get(url, headers=headers)
		#looks into site again
		Lookagain = BeautifulSoup(response.text, "html.parser")
		#wait until redo
		time.sleep(2)
#if change, send e-mail
	else:
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.ehlo()
		server.starttls()
		server.login("Mye-mailhere","Mypasswordhere") 
		#what's in the email
		Msg = "I think the website changed..." 
		From = "Mye-mailhere"
		#the receiver
		To = "Anotheremailthatidonotcareabout" 
		
		server.sendmail(From, To, Msg)
		server.quit()
		
		break
