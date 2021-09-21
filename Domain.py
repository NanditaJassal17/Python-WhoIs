import whois
import pandas as pd
import mysql.connector
import datetime


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

def convertList(list1):
    unique_list=[]
    for x in list1:
        if list1.count(x)>1:

            if x not in unique_list:
                unique_list.append(x)
        str = ''  # initializing the empty string  
  
        for i in unique_list: #Iterating and adding the list element to the str variable  
            str = str+i + ','  
        else:
            str = x

  
    return str  


data = pd.read_csv('top10milliondomains(edited).csv')
df = data.drop_duplicates(subset=['Domains'])
domains = df['Domains'].tolist()

for domain in domains:

    domain_name = domain

   
    if is_registered(domain):
        result = whois.whois(domain)
        #print(result)
        registered = 'True'
        creation_date = result.creation_date 
        updated_date = result.updated_date
        expiration_date = result.expiration_date
        tld = str('.' + (domain_name.split('.',1))[1])
        print(domain_name)
        print(creation_date)
        print(tld)
        domain_status = convertList(result.status)
        name_servers = []
        name_servers_list = result.name_servers
        for x in name_servers_list:
            name_servers.append(x.lower())
        name_servers = convertList(name_servers)
        dnssec = convertList(result.dnssec)
        registrar = convertList(result.registrar)
        country = result.country 
        

        
        print(result)
       


