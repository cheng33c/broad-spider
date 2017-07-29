#!/bin/bash
cd ../cspider
curl http://120.24.231.4:6801/schedule.json -d project=cspider -d spider=ebayredis
