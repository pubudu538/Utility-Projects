import urllib2
import json
import base64
import os 
import time

file_path = '/home/pubudu/Documents/readme.md'
log_analyzer_url = 'http://localhost:9764/api/logs/publish'
log_analyzer_username = 'admin'
log_analyzer_password = 'admin'


read_file = open(file_path, "r")

auth = base64.encodestring('%s:%s' % (log_analyzer_username, log_analyzer_password)).replace('\n', '')

while True:
    where = read_file.tell()  # where the seeker is in the file
    line = read_file.readline()  # read the current line
    if not line:
        # no new line entered
        time.sleep(1)
        read_file.seek(where)  # set seeker
    else:
      

        data = {
		 "@logstream"  : "['ESB', 'node-01']",
		 "@timestamp" : "2013-11-28T17:01:32.003Z",
		 "message": "%s" % line,
		 "cartridge"     : "Test"
		}

        request = urllib2.Request(log_analyzer_url, json.dumps(data))
        request.add_header('Content-Type', 'application/json')
        request.add_header('Authorization', 'Basic %s' % auth)

        try:
            urllib2.urlopen(request)
            print('Published' + line)
            
        except Exception:
            print("Failed to publish event.")
            continue