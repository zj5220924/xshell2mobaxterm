#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import configparser
import os

suffix_name = '.xsh'
path = 'E:\\sessions\\'
moba_configfile = 'E:\\MobaX_Sessions.mxtsessions'

cnt = 0
for rootdir, dirs, files in os.walk(path):
    for fileName in files:
        if fileName.endswith(suffix_name):

            configfile = rootdir + '\\' + fileName
            config = configparser.ConfigParser()
            config.read(configfile)

            host = config.get('CONNECTION', 'Host')
            port = config.getint('CONNECTION', 'Port')
            username = config.get('CONNECTION:AUTHENTICATION', 'UserName')
            session_name = fileName.replace(suffix_name, '')

            moba_config = configparser.RawConfigParser()
            moba_config.optionxform = lambda option: option
            moba_config.read(moba_configfile)

            middle_dir = rootdir.replace(path, '')
            if middle_dir == '':
                section_name = 'Bookmarks'
            else:
                section_name = 'Bookmarks_' + str(cnt)

            if section_name not in moba_config:
                moba_config.add_section(section_name)

            moba_config.set(section_name, 'SubRep', middle_dir)
            moba_config.set(section_name, 'ImgNum', '41')
            moba_config.set(section_name, session_name, '#109#0%{}%{}%{}%%-1%-1%%%%%0%0%0%%%-1%0%0%0%%1080%%0%0%1#MobaFont%10%0%0%-1%15%236,236,236%30,30,30%180,180,192%0%-1%0%%xterm%-1%-1%_Std_Colors_0_%80%24%0%1%-1%<none>%%0%0%-1#0# #-1'.format(host, port, username))

            with open(moba_configfile, 'w+') as f:
                moba_config.write(f)
                f.close()
    cnt += 1

