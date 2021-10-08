from pytube import YouTube
from moviepy.editor import *
import pandas as pd
import os
import shlex, subprocess
import numpy as np
from pathlib import Path

def readFile(file_path):
    url_list, name_list = [], []
    df = pd.read_csv(file_path, sep = '\t', header = None)
    for idx in range(df.shape[0]):
        url_list.append(df.iloc[idx][0])
        if df.shape[1] == 2:
            name_list.append(df.iloc[idx][1])
        elif df.shape[1] == 1:
            name_list.append('_')
        else:
            raise ValueError('[YouTube2MP3] The format of the input file is wrong!')
    
    return url_list, name_list


def download(url_list, name_list, position = './'):
    success_num = 0
    if len(url_list) != len(name_list):
        raise ValueError('[YouTube2MP3] The format of the inputs is wrong!')
    movie_list, mp3_list = [], []
    for idx, url in enumerate(url_list):
        yt = YouTube(url)
        origin_name = yt.title.replace(' ', '').replace('(', '').replace(')', '')
        yt.title = str(idx)
        yt.streams.first().download()
        movie_file = yt.title+'.3gpp'

        mp3_file = name_list[idx]+'.mp3' if name_list[idx] != '_' else origin_name+'.mp3'
        movie_list.append(movie_file)
        try:
            VideoFileClip(movie_file).audio.write_audiofile(mp3_file)
            mp3_list.append(mp3_file)
            success_num += 1
        except:
            print('\nWARNING: '+mp3_file+' download failed. Please check the URL or maybe this URL is unable to download.\n')

    for movie in movie_list:
        os.popen('rm '+ movie+'\n','w', 1)
    
    if not Path(position).exists():
        os.mkdir(position)
    
    if position != './':
        for mp3 in mp3_list:
            os.popen('mv '+ mp3+ ' ' +position+'\n','w', 1)
        
    print('\n[Done] '+str(success_num) + ' songs were downloaded successfully in \''+position+'\'.\n')
    
    