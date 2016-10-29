

########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'e120910955f64c9e9586855f6b9eeba0',
}


Gid = raw_input("Enter")
params = urllib.urlencode({
})

prm="?%s" % params
strng =  "/face/v1.0/persongroups/"+Gid+prm
try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("GET",strng, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

