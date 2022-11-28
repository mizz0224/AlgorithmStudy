import math
import itertools
def solution(m, musicinfos):
    m = removeShop(devide(m))
    dic = dict()
    for musicinfo in musicinfos:

        musicinfo = musicinfo.split(",")
        
        startHour = int(musicinfo[0].split(":")[0])
        startMinute = int(musicinfo[0].split(":")[1])
        
        endHour = int(musicinfo[1].split(":")[0])
        endMinute = int(musicinfo[1].split(":")[1])
        
        playtime = (endHour * 60 + endMinute) - (startHour * 60 + startMinute)
        if playtime < 1 : 
            continue
        musicName = musicinfo[2]
        music = devide(musicinfo[3])
        
        totalMusic = music
        totalMusic *= math.ceil(playtime/ len(music))
        totalMusic = totalMusic[:playtime]
    
        if m in removeShop(totalMusic) and playtime not in dic.keys():
            dic[playtime] = musicName
    if len(dic.keys()) > 0 :
        return dic[max(dic.keys())]
    else :
        return "(None)"

def removeShop(pitches) :
    transferted = []
    for ch in pitches:
        if "#" in ch :
            transferted.append(chr(ord(ch[0])+32))
        else :
            transferted.append(ch)
    return "".join(transferted)

def devide(pitches) :
    devided = []
    pitch = ""
    for ch in pitches:
        if 64 < ord(ch) and ord(ch) < 90:
            if pitch != "":
                devided.append(pitch)
            pitch = ch
        else :
            pitch += ch
    devided.append(pitch)
    return devided