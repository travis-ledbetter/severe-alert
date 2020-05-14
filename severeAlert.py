import xml.etree.ElementTree as ET
import urllib2 as URL
from datetime import datetime
import time
import os
from apscheduler.schedulers.blocking import BlockingScheduler
from switcher import state

def alert_pull():
	tree = ET.parse(URL.urlopen('https://alerts.weather.gov/cap/us.php?x=1'))
	root = tree.getroot()

	for x in root.findall('{http://www.w3.org/2005/Atom}entry'):
		event = x.find('{urn:oasis:names:tc:emergency:cap:1.1}event').text
		severity = x.find('{urn:oasis:names:tc:emergency:cap:1.1}severity').text
		location = x.find('{urn:oasis:names:tc:emergency:cap:1.1}areaDesc').text
		geo = x.find('{urn:oasis:names:tc:emergency:cap:1.1}geocode')
		stateAbr = geo[3].text[0:2]
	
		if severity == "Severe":
			print "There is a " + event + " in " + location + " ", state(stateAbr)
			
scheduler = BlockingScheduler()
#Script is set to pull alerts every 10 minutes, that can be changed below
scheduler.add_job(alert_pull,'interval',minutes=10)
scheduler.start()
	
