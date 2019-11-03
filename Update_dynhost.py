# -*- encoding: utf-8 -*-
'''
First, install the latest release of Python wrapper: $ pip install ovh
'''
import json
import ovh
import requests
import credentials as credential_perso


# Instanciate an OVH Client.
# You can generate new credentials with full access to your account on
# the token creation page
client = ovh.Client(

    endpoint=credential_perso.endpoint,
    application_key=credential_perso.application_key,
    application_secret=credential_perso.application_secret,
    consumer_key=credential_perso.consumer_key,
)



def Domain_id():
    domain_id = client.get('/domain/zone/geeraert.eu/dynHost/record', subDomain='apple')
    return domain_id

def update_zone(subdomain,new_ip,domain_id):
    result = client.put('/domain/zone/geeraert.eu/dynHost/record/'+domain_id,
        ip=new_ip,
        subDomain=subdomain)
    refresh_dns()
    return result

def refresh_dns():
    result_refresh = client.post('/domain/zone/geeraert.eu/refresh')
    return result_refresh

def MyIP():
    response = requests.get('https://ifconfig.me/ip')
    return response.text

result_update = update_zone('apple',MyIP(),str(Domain_id()[0]))
