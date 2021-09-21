import whois

import mysql.connector
import whois

db = mysql.connector.connect(
	host = "",
	user = "",
	passwd = "",
	database=""
	)

def is_registered(domain_name):
    """
    A function that returns a boolean indicating 
    whether a `domain_name` is registered
    """
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)

domains = ['yahoo.com','facebook.com','google.com','absbsba.com']
for domain in domains:

    #print(domain, "is registered" if is_registered(domain) else "is not registered")
    
    if is_registered(domain):
    	result = whois.whois(domain)

    	
    	mycursor = db.cursor()
    	mycursor.execute("INSERT INTO ___________________________")
        db.commit()







