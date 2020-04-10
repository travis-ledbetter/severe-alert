import xml.etree.ElementTree as ET
import urllib2 as URL

tree = ET.parse(URL.urlopen('https://alerts.weather.gov/cap/us.php?x=1'))
root = tree.getroot()

def state(stateAbr):
	switcher={
		"AL":"ALABAMA",
		"AK":"ALASKA",
		"AZ":"ARIZONA",
		"AR":"ARKANSAS",
		"CA":"CALIFORNIA",
		"CO":"COLORADO",
		"CT":"CONNECTICUT",
		"DE":"DELAWARE",
		"FL":"FLORIDA",
		"GA":"GEORGIA",
		"HI":"HAWAII",
		"ID":"IDAHO",
		"IL":"ILLINOIS",
		"IN":"INDIANA",
		"IA":"IOWA",
		"KS":"KANSAS",
		"KY":"KENTUCKY",
		"LA":"LOUISIANA",
		"ME":"MAINE",
		"MD":"MARYLAND",
		"MA":"MASSACHUSETTS",
		"MI":"MICHIGAN",
		"MN":"MINNESOTA",
		"MS":"MISSISSIPPI",
		"MO":"MISSOURI",
		"MT":"MONTANA",
		"NE":"NEBRASKA",
		"NV":"NEVADA",
		"NH":"NEW HAMPSHIRE",
		"NJ":"NEW JERSEY",
		"NM":"NEW MEXICO",
		"NY":"NEW YORK",
		"NC":"NORTH CAROLINA",
		"ND":"NORTH DAKOTA",
		"OH":"OHIO",
		"OK":"OKLAHOMA",
		"OR":"OREGON",
		"PA":"PENNSYLVANIA",
		"RI":"RHODE ISLAND",
		"SC":"SOUTH CAROLINA",
		"SD":"SOUTH DAKOTA",
		"TN":"TENNESSEE",
		"TX":"TEXAS",
		"UT":"UTAH",
		"VT":"VERMONT",
		"VA":"VIRGINIA",
		"WA":"WASHINGTON",
		"WV":"WEST VIRGINIA",
		"WI":"WISCONSIN",
		"WY":"WYOMING"
	}
	return switcher.get(stateAbr)

for x in root.findall('{http://www.w3.org/2005/Atom}entry'):
	event = x.find('{urn:oasis:names:tc:emergency:cap:1.1}event').text
	severity = x.find('{urn:oasis:names:tc:emergency:cap:1.1}severity').text
	location = x.find('{urn:oasis:names:tc:emergency:cap:1.1}areaDesc').text
	geo = x.find('{urn:oasis:names:tc:emergency:cap:1.1}geocode')
	stateAbr = geo[3].text[0:2]
	
	
	if severity == "Severe":
		print "There is a " + event + " in " + location + " ", state(stateAbr)
	
