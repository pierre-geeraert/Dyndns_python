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

new_subdomain = credential_perso.my_subdomain
new_domain = credential_perso.my_zone

def Domain_id():
    domain_id = client.get('/domain/zone/'+new_domain+'/dynHost/record', subDomain=new_subdomain)
    return domain_id

def update_zone(subdomain,new_ip,domain_id):
    result = client.put('/domain/zone/'+new_domain+'/dynHost/record/'+domain_id,
        ip=new_ip,
        subDomain=subdomain)
    refresh_dns()
    return result

def refresh_dns():
    result_refresh = client.post('/domain/zone/'+new_domain+'/refresh')
    return result_refresh

def MyIP():
    response = requests.get('https://ifconfig.me/ip')
    return response.text

result_update = update_zone(new_subdomain,MyIP(),str(Domain_id()[0]))
