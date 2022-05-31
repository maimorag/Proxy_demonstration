from flask import Flask, render_template, request
import  threading, webbrowser

app = Flask(__name__) # '___name__'  holds the name of the current Python module


def isUrValid(url):
    """
    this function search for the word "attack" in the given URL.
    If it contain the word "attack " false will be return and true otherwise.
    """
    return (url.find("attack")==-1)

@app.route('/forward_request', methods=['GET', 'POST'])#determines the entry point; the /forward_request means the root of the website,

def forwardRequest():
    """
    this function handles the request. It preforms the following steps:
    1. checks if it is valid- url doesn't contain "attack"
    2. prints paramters, if exists
    
    """
    url = request.args.get('url')
    if(isUrValid(url)==False):
        #For urls containing a string “attack”, return HTTP code 403 and do not perform the fetching of this url.') 
        return render_template("UrlContainAttack.html")#"HTTP code 403 and do not perform the fetching of this url"
    #url doen't contain attack string
    args=request.args
    num_of_args=len(args)
    if num_of_args==1:
        return ""
    #creating the string to return
    request_info ="{<br><pre>"
    last_key=sorted(args.keys())[0]
    for key in args:
        if(key!="url"):
            value=args.get(key)
            if(not(value.isnumeric())):
                value="\""+value+"\""
            if last_key!=key:
                request_info+= "  \"{}\": {},<pre>".format(key,value) 
            else:   
                request_info+= "  \"{}\": {}<pre>".format(key,value)
    request_info+=" }"
    threading.Timer(1.25, lambda: webbrowser.open(url) ).start()    
    return request_info



if __name__ == '__main__':
    # run app on port 5000 and allow multiple request with threaded=True
    #stops only when ctrl+c is pressed
    while(True):
        app.run( port=5000,threaded=True)
        url = request.args.get('url')
        if(isUrValid(url)==False):
        #For urls containing a string “attack”, return HTTP code 403 and do not perform the fetching of this url.') 
            render_template("UrlContainAttack.html")#"HTTP code 403 and do not perform the fetching of this url"
        else:    
            threading.Timer(6000, lambda: webbrowser.open(url) ).start()
