import urllib.request
import hashlib
import os
from urllib.error import HTTPError, URLError
import socket
import logging
import sys

token = 'tokenkey'
filepath = '/path/tvh_output.m3u'

# pull all tags
tags_url = 'http://host:9981/playlist/tags/'
headers = {'User-Agent': 'NSPlayer/7.10.0.3059'}
req = urllib.request.Request(tags_url,headers=headers)
try:
    response = urllib.request.urlopen(req)
except HTTPError as error:
    logging.error('Data not retrieved because %s\nURL: %s', error, tags_url)
    sys.exit(1)
except URLError as error:
    if isinstance(error.reason, socket.timeout):
        logging.error('socket timed out - URL %s', tags_url)
    else:
        logging.error('uncategorized exception - URL %s', tags_url)
    sys.exit(1)
else:
    logging.info('Access successful.')
data = response.read()
m3u_tags = data.decode('utf-8')

#split by line and read
tags = [] #store all the tags in tvh
m3u_tag_lines = m3u_tags.split('#EXTINF:-1')
for m3u_tag_line in m3u_tag_lines:
    m3u_tag = m3u_tag_line.splitlines()
    if m3u_tag[0] != '#EXTM3U':
        url = m3u_tag[1].strip()
        name = m3u_tag[0].split(',')[1].strip()
        tags.append([name, url])

#pull channel list without tags
channels_all_url = 'http://host:9981/playlist/'
headers = {'User-Agent': 'NSPlayer/7.10.0.3059'}
req = urllib.request.Request(channels_all_url,headers=headers)
try:
    response = urllib.request.urlopen(req)
except HTTPError as error:
    logging.error('Data not retrieved because %s\nURL: %s', error, channels_all_url)
    sys.exit(1)
except URLError as error:
    if isinstance(error.reason, socket.timeout):
        logging.error('socket timed out - URL %s', channels_all_url)
    else:
        logging.error('uncategorized exception - URL %s', channels_all_url)
    sys.exit(1)
else:
    logging.info('Access successful.')
data = response.read()
m3u_channels_all = data.decode('utf-8')

channels = [] #store all channel info
m3u_channels_lines = m3u_channels_all.split('#EXTINF:-1')
for m3u_channels_line in m3u_channels_lines:
    line = m3u_channels_line.splitlines()
    if line[0] != '#EXTM3U':
        url = line[len(line)-1].strip()
        name = line[0].split(',')[1].strip()
        comp = line[0].split(',')[0].strip()
        group = ''
        channels.append([comp, name, url, group])

#Loop through all tags
for tag in tags:
    if tag[0] == 'main': continue
    if tag[0] == 'alt1': continue
    url = tag[1][:-13] + '&profile=pass'
    headers = {'User-Agent': 'NSPlayer/7.10.0.3059'}
    req = urllib.request.Request(url,headers=headers)
    try:
        response = urllib.request.urlopen(req)
    except HTTPError as error:
        logging.error('Data not retrieved because %s\nURL: %s', error, url)
        sys.exit(1)
    except URLError as error:
        if isinstance(error.reason, socket.timeout):
            logging.error('socket timed out - URL %s', url)
        else:
            logging.error('uncategorized exception - URL %s', url)
        sys.exit(1)
    else:
        logging.info('Access successful.')
    data = response.read()
    m3u_channels_tag = data.decode('utf-8')

    #compare each channel and append to the group title
    m3u_channels_lines = m3u_channels_tag.split('#EXTINF:-1')
    for m3u_channels_line in m3u_channels_lines:
        line = m3u_channels_line.splitlines()
        if line[0] != '#EXTM3U':
            url = line[len(line)-1].strip()
            name = line[0].split(',')[1].strip()
            comp = line[0].split(',')[0].strip()
            x = comp.find('tvg-id="')+8
            tvgids = comp[x:]
            y = tvgids.find('"')
            tvgid = tvgids[0: y:]
            #loop through channels array and compare
            for channel in channels:
                if tvgid in channel[0]:
                    if len(channel[3]) == 0:
                        channel[3] += tag[0]
                    else:
                        channel[3] += ';' + tag[0]

#write channels to file
if len(channels) > 0:
    fo = open(filepath, 'w', encoding='utf-8')
    newM3uFile = '#EXTM3U' + '\n'

    for channel in channels:
        line = '#EXTINF:-1 ' + channel[0] + ' group-title="' + channel[3] + '", ' + channel[1] + '\n' + channel[2] + '\n'
        newM3uFile += line
    fo.write(newM3uFile)
    fo.close