import urllib2
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()
import urllib2
response = urllib2.urlopen('http://shroomery.org/ythan/proxycheck.php?ip=' + ip)
html = response.read()

if html == "N":
	print "Your IP is not listed as a Proxy or a VPN."
elif html == "X":
	print "Your IP is listed as a VPS or a Dedicated server and can be used as a proxy."
elif html == "Y":
	print "Your IP is listed as a Proxy or a VPN"
else: 
	print "ERROR."
