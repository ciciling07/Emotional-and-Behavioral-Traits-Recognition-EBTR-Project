# encoding:utf-8

"""
This is a wrapper for ffmpeg in the system.
"""

import json
import os, platform,re

class psy_ffmpeg:
    def __init__(self,cfg_json=None):
        
        if platform.platform().startswith("Windows"):
            self.systemtype = "windows"
        else:
            self.systemtype = "unix"
        
        self.cfg = cfg_json
        self.ffmpegbinpath = ""

    def checkffmpeg(self,ffmpegbinpath):
        """
        check the rightness of ffmpeg binary
        """
        if type(ffmpegbinpath) is tuple:
            ffmpegbinpath = ffmpegbinpath[0]
        else:
            assert(type(ffmpegbinpath) is str)
        if ffmpegbinpath.find('ffmpeg') < 0:
            return False
        #print(ffmpegbinpath + " -version")
        result = os.popen(ffmpegbinpath + " -version").read().strip().split('\n')[0]
        if not result.startswith('ffmpeg'):
            return False
        self.ffmpegbinpath = ffmpegbinpath
        return True

    def VideoToAudio(self,videofilefullpath):
        """
        Convert video to audio
        return outfilename
        """
        #assert(videofilepath is not None)
        self.videoinfo = os.popen(self.ffmpegbinpath + " -i " + videofilefullpath + " 2>&1").read()
        print(self.videoinfo)
        videoinfolist = self.videoinfo.split('\n')
        for i in videoinfolist:
            if i.strip().startswith('Duration'):
                self.videolength = i.split(',')[0].split(' ')[-1]
                print(self.videolength)
        [hours,minutes,seconds] = self.videolength.split(":")
        cnt = int(hours)*60 + int(minutes)
        if float(seconds) > 10.0:
            cnt += 1
        # cnt is minute count.
        #print(cnt)
        #return 
        hint, mint = int(hours), int(minutes)
        print(hint,mint)
        namecnt = 1
        for h in range(hint+1):
            for m in range(61):
                if h == hint and m > mint:
                    break
                if h < 10:
                    hourstr = "0" + str(h)
                else:
                    hourstr = str(hourstr)
                if m < 10:
                    minstr = "0" + str(m)
                else:
                    minstr = str(minstr)
                ss_time = hourstr + ":" + minstr + ":" + "00"
                outname = str(namecnt) + ".wav"
                runcommand = self.ffmpegbinpath + " -y -i " + videofilefullpath + " -ss " + ss_time + " -t 60 -acodec pcm_s16le -ac 1 -ar 16000 " + outname
                #print(runcommand)
                #os.system(runcommand)
                namecnt += 1
        current_path = os.getcwd()
        print(current_path)

        return
        prefix = videofilefullpath.split('\\')[-1]
        prefix = prefix.split('.')[0]
        outname = self.cfg['rootfile'] + "/data/audio/" + prefix + ".wav"
        runcommand = self.ffmpegbin + " -y -i " + videofilefullpath + " -acodec pcm_s16le -ac 1 -ar 16000 " + outname
        #print(runcommand)
        os.system(runcommand)
        return outname


if __name__ == "__main__":
    ffmpegbinpath = ""
    videofilefullpath="C:\\Users\\hongy\\Documents\\work\\cici\\BehavioralCoding-cs410project\\sample.mov"
    ffins = psy_ffmpeg()
    ffins.checkffmpeg("C:\\Users\\hongy\\Documents\\work\\cici\\ffmpeg-4.0.2-win64\\bin\\ffmpeg.exe")
    ffins.VideoToAudio(videofilefullpath)


#psy_ffmpeg_ins = psy_ffmpeg()
#psy_ffmpeg_ins.VideoToAudio()




#os.system(r"C:\Users\hongy\Documents\work\cici\ffmpeg-4.0.2-win64\bin\ffmpeg.exe") # -i ../../data/test.mov -acodec pcm_s16le -ac 1 -ar 16000 out.wav")




