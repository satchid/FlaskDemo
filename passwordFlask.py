from flask import Flask
import random
from flask import request
app=Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello Python lover"

@app.route("/getPassword")
def get_password():
    # Get length from parameters if set
    length=request.args.get('length')
    if length is None:
        length=8
    else:
        length=int(length)

    #constructs for password
    char_lower='abcdefghijklmnopqrstuvwxyz'
    char_upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers='0123456789'
    special='!@#$%&*()_+-=[]?'
    password=char_lower+char_upper+numbers+special

    #generate random password using sample method
    password=random.sample(password,length)
    return 'Password: '+''.join([str(elem) for elem in password])


if __name__ == '__main__':
    app.run()
