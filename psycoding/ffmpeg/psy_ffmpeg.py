# encoding:utf-8

"""
This is a wrapper for ffmpeg in the system.
"""

import json
import os, platform, re, shutil, time

class psy_ffmpeg:
    def __init__(self,cfg_json=None):
        
        if platform.platform().startswith("Windows"):
            self.systemtype = "windows"
        else:
            self.systemtype = "unix"
        
        self.cfg = cfg_json
        self.ffmpegbinpath = "C:\\Users\\hongy\\Documents\work\\cici\\ffmpeg-4.0.2-win64\\bin\\ffmpeg.exe"

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
        if not videofilefullpath:
            print("check video path")
            return 
        if not self.ffmpegbinpath:
            print("no ffmpegbinpath")
            exit()
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
        
        # create data directory
        save_dir = os.path.join(os.getcwd(), "data", "audio")
        
        if os.path.exists(save_dir):
            shutil.rmtree(save_dir)
            time.sleep(1)
            os.mkdir(save_dir)
        else:
            os.mkdir(save_dir)
        
        hint, mint = int(hours), int(minutes)
        name_count = 1 #  id of split audio
        comand_list = []
        output_audio_list = []
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
                    minstr = str(m)
                ss_time = hourstr + ":" + minstr + ":" + "00"
                outname = os.path.join(save_dir, str(name_count)+".wav")
                print(outname)
                runcommand = self.ffmpegbinpath + " -y -i " + videofilefullpath + " -ss " + ss_time + " -t 60 -acodec pcm_s16le -ac 1 -ar 16000 " + outname
                comand_list += [runcommand]
                output_audio_list += [outname]
                name_count += 1
                #os.system(runcommand)
        # execute the command
        for x in comand_list:
            os.system(x)
        return output_audio_list


if __name__ == "__main__":
    pass


#psy_ffmpeg_ins = psy_ffmpeg()
#psy_ffmpeg_ins.VideoToAudio()




#os.system(r"C:\Users\hongy\Documents\work\cici\ffmpeg-4.0.2-win64\bin\ffmpeg.exe") # -i ../../data/test.mov -acodec pcm_s16le -ac 1 -ar 16000 out.wav")




