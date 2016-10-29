

########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '4e3ecd34501e4b52ad056ed7df847705',
}

params = urllib.urlencode({
})
try:
    conn = httplib.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/face/v1.0/identify?%s" % params, "{'personGroupId':'001','faceIds':['fe2aac59-7bca-4dcb-b09d-24d4bd3db37f'],'maxNumOfCandidatesReturned' : 1 }", headers)
    response = conn.getresponse()
    data = response.read()
    print(data+"\n")
    
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

####################################

