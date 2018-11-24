# -*- coding: UTF-8 -*-
import urllib3
import time
import urllib.response
import urllib.request
import json
import hashlib
import base64


API_KEY = "c8699fdf1208cfbbe87272ead4148afa"
AUDIO_PATH = r"C:\Users\\hongy\\Documents\\work\\cici\\BehavioralCoding-cs410project\\data\\audio\\sample.wav"
Output_path = r"C:\Users\\hongy\\Documents\\work\\cici\\BehavioralCoding-cs410project\\data\\text\\sample.txt"
APPID = "5bbde482"

class xunfei:
    def __init__(self, audio_list = None):
        self.__audio_path = audio_list
        pass
    
    def set_audio_path(self, audio_list):
        self.__audio_list = audio_list
    
    def get_audio_path(self):
        return self.__audio_list

    def audio2text(self, index):
        with open(self.__audio_list[index], 'rb') as f:
            base64_audio = base64.b64encode(f.read())
            body = urllib.parse.urlencode({'audio': base64_audio})
            body = body.encode("utf8")
            url = 'http://api.xfyun.cn/v1/service/v1/iat'
            api_key = API_KEY
            param = {"engine_type": "sms16k", "aue": "raw"}
            x_appid = APPID
            x_param = json.dumps(param)
            x_param = x_param.encode('utf8')
            x_param = base64.b64encode(x_param)
            x_param = x_param.decode('utf8')
            x_time = int(int(round(time.time() * 1000)) / 1000)
            checksum = (api_key + str(x_time) + x_param).encode('utf8')
            x_checksum = hashlib.md5(checksum).hexdigest()
            x_header = {'X-Appid': x_appid,
                        'X-CurTime': x_time,
                        'X-Param': x_param,
                        'X-CheckSum': x_checksum}
            #x_header = x_header.encode('utf8'
            req = urllib.request.Request(url, body, x_header)
            result = urllib.request.urlopen(req)
            result = result.read()
            resjson = json.loads(result)
            data =""
            if resjson["desc"] == "success":
                data = resjson["data"]
        return data 

    def generate_text(self):
        res_list = []
        for index in range(len(self.__audio_list)):
            res_list += [self.audio2text(index)]
            print("process one video successfully")
            #break # for test use
        return res_list

def main():
    f = open(AUDIO_PATH, 'rb')
    file_content = f.read()
    #print(file_content)
    base64_audio = base64.b64encode(file_content)
    body = urllib.parse.urlencode({'audio': base64_audio})
    body = body.encode("utf8")
    url = 'http://api.xfyun.cn/v1/service/v1/iat'
    api_key = API_KEY
    param = {"engine_type": "sms16k", "aue": "raw"}

    x_appid = APPID
    print(type(json.dumps(param)))
    #x_param = base64.b64encode(json.dumps(param).replace(' ', ''))
    x_param = json.dumps(param)
    x_param = x_param.encode('utf8')
    x_param = base64.b64encode(x_param)
    x_param = x_param.decode('utf8')
    x_time = int(int(round(time.time() * 1000)) / 1000)
    checksum = (api_key + str(x_time) + x_param).encode('utf8')
    x_checksum = hashlib.md5(checksum).hexdigest()
    x_header = {'X-Appid': x_appid,
                'X-CurTime': x_time,
                'X-Param': x_param,
                'X-CheckSum': x_checksum}
    #x_header = x_header.encode('utf8'
    req = urllib.request.Request(url, body, x_header)
    result = urllib.request.urlopen(req)
    result = result.read()
    print(result)
    return



if __name__ == '__main__':
    #main() 
    result = "\xe7\x9c\x8b\xe7\x9c\x8b\xe5\x91\x97\xe5\x87\xba\xe5\x8f\x91\xef\xbc\x8c\xe5\xb0\xb1\xe6\x98\xaf\xe8\xbf\x99\xe6\xa0\xb7\xef\xbc\x8c\xe6\x88\x91\xe4\xb8\x8d\xe6\x83\xb3\xe6\xaf\x8f\xe5\xa4\xa9\xe5\xb0\xb1\xe6\x98\xaf\xe5\xb7\xa5\xe4\xbd\x9c\xe5\x8d\x95\xe4\xbd\x8d\xe5\x88\xb0\xe5\xae\xb6\xef\xbc\x8c\xe7\x84\xb6\xe5\x90\x8e\xe5\xb0\xb1\xe3\x80\x82"
    result = result.encode("raw_unicode_escape")
    print(result.decode())
    with open(Output_path,"w") as f:
        f.writelines(result.decode('utf-8'))
    with open(Output_path,'r') as f:
        str1 = f.read()
        print(str1[0]==str1[1])



