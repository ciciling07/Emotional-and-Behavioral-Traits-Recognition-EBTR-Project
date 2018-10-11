# encoding:utf-8
"""
This is a wrapper for ffmpeg in the system.
"""
import json
import os


class psy_ffmpeg:
    def __init__(self,cfg_json):
        #TODO Add different system fit
        self.cfg = cfg_json
        self.ffmpegbin = cfg_json['ffmpegbinpath'] + "\\ffmpeg.exe"
        #print(self.ffmpegbin)

        
    def VideoToAudio(self,videofilefullpath):
        """
        Convert video to audio
        return outfilename
        """
        #assert(videofilepath is not None)
        prefix = videofilefullpath.split('\\')[-1]
        prefix = prefix.split('.')[0]
        outname = self.cfg['rootfile'] + "/data/audio/" + prefix + ".wav"
        runcommand = self.ffmpegbin + " -y -i " + videofilefullpath + " -acodec pcm_s16le -ac 1 -ar 16000 " + outname
        #print(runcommand)
        os.system(runcommand)
        return outname


#psy_ffmpeg_ins = psy_ffmpeg()
#psy_ffmpeg_ins.VideoToAudio(videofilefullpath=r"C:\Users\hongy\Documents\work\cici\BehavioralCoding-cs410project\sample.mov")




#os.system(r"C:\Users\hongy\Documents\work\cici\ffmpeg-4.0.2-win64\bin\ffmpeg.exe") # -i ../../data/test.mov -acodec pcm_s16le -ac 1 -ar 16000 out.wav")




