import argparse
import requests
import pyquery

def login(session, email, password):
    response = session.get('https://m.facebook.com')
    
    # Attempt to login to Facebook
    response = session.post('https://m.facebook.com/login.php', data={
        'email': email,
        'pass': password
    }, allow_redirects=False)
    
    # If c_user cookie is present, login was successful
    if 'c_user' in response.cookies:
        #print("success")
        return True
    else:
        return False 


parser = argparse.ArgumentParser(description='Login to Facebook')
parser.add_argument('ip', help='proxy ip to use')
parser.add_argument('email', help='Email address')
parser.add_argument('password', help='Login password')

args = parser.parse_args()

session = requests.session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Linux i686; rv:39.0) Gecko/20100101 Firefox/39.0'
})

session.proxies = {
    'http':args.ip,
    'https':args.ip,
}

lgn = login(session, args.email, args.password)
if lgn == False:
    print("nop")
elif lgn == True:
    print("success")