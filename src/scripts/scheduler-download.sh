#!/bin/bash
cd ../cspider/
pwd
curl http://120.24.231.4:6801/schedule.json -d project=cspider -d spider=phdown -d setting=DOWNLOAD_DELAY=2 -d arg1=val1
