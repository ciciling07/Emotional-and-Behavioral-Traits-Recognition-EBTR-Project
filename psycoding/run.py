# encoding:utf-8
from aip import AipSpeech
from ffmpeg import psy_ffmpeg
import json

""" 你的 APPID AK SK """
APP_ID = '14293560'
API_KEY = 'qtjdwwOsGvEN836DsyM4SpTj'
SECRET_KEY = '99eEeI8IC5wPypcoSz3jWnioAiqQjGYd'

def get_config(cfg):
    """
    return cfg json 
    """
    configjson = {}
    with open(cfg,'r') as f:
        configjson = json.load(f)
    return configjson

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
cfg_json = get_config("C:\\Users\\hongy\\Documents\\work\\cici\\BehavioralCoding-cs410project\\config.json")
print(cfg_json)
psy_ffmpeg_ins = psy_ffmpeg.psy_ffmpeg(cfg_json = cfg_json)
converted_audio_filename = psy_ffmpeg_ins.VideoToAudio(videofilefullpath="C:\\Users\\hongy\\Documents\\work\\cici\\BehavioralCoding-cs410project\\sample.mov")


# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
res = client.asr(get_file_content(converted_audio_filename), 'wav', 16000, {
    'dev_pid': 1536,
})
print(res)
with open(cfg_json['rootfile'] + "/data/text/sample.txt",'w') as f:
    f.writelines(res['results'])