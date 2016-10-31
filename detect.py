########### Python 2.7 #############./ngrok http 80

import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '',
}

params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': ''
})

def cleanData(data):
	pass
	strng = data.split('"')
	return strng[3]




link = ""
try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/detect?%s" % params, "{'url':'"+link+"'}", headers)
    response = conn.getresponse()
    data = response.read()
    data=cleanData(data)
    print(data)
    conn.request("POST", "/face/v1.0/identify?%s" % params, "{'personGroupId':'001','faceIds':['"+data+"'],'maxNumOfCandidatesReturned' : 1 }", headers)

    response = conn.getresponse()
    data = response.read()
    print(data+"\n")
    conn.close()



except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))


