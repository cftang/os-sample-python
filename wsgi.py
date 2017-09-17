# -*- coding:utf-8 -*- 
import json
import urllib.request
import urllib.parse
import time
import datetime
import pytz

from flask import Flask

application = Flask(__name__)

@application.route("/")
def hello():
	return "Hello World! python 3.5"

@application.route("/map1")
def map1():
	return "Hello World! map1"

@application.route("/map2")
def map2():
	return "Hello World! map2"

@application.route("/map3")
def map3():

	# 百度地图 Direction API v1.0Web服务API
	# http://lbsyun.baidu.com/index.php?title=webapi/direction-api

	# json format tool
	# http://www.bejson.com/

	# python 3.5 urllib
	# https://docs.python.org/3.5/library/urllib.request.html#urllib-examples

	#print(datas)
	#datas = {"text": "中文","polyline": "116.621248,41.02831"}

	#print(json.dumps(datas,encoding="utf-8",sort_keys=False,ensure_ascii=False,indent=2))
	#url = 'api.map.baidu.com/direction/v1?mode=driving&origin=竖新派出所&destination=上海新华医院&origin_region=上海&destination_region=上海&output=json&ak=67c1ea196201cb1521170cf746fb7466'

	params = {
		'mode': 'driving',
		'origin': '绿色米兰奥特莱斯',
		'destination': '四平路773号金大地商务楼',
		'origin_region': '上海',
		'destination_region': '上海',
		'waypoints': '上海市鞍山实验中学',
		'output': 'json',
		'ak': '67c1ea196201cb1521170cf746fb7466'
	}
	url= 'http://api.map.baidu.com/direction/v1?%s' % urllib.parse.urlencode(params)

	#with urllib.request.urlopen(url) as f:
	#	print(f.read().decode('utf-8'))

	tz = pytz.timezone('Asia/Shanghai')
	dt = datetime.datetime.now(tz)

	#print (dt.strftime('%Y-%m-%d %H:%M:%S'))
	# http://api.map.baidu.com/direction/v1?mode=driving&origin=%E7%AB%96%E6%96%B0%E6%B4%BE%E5%87%BA%E6%89%80&destination=%E4%B8%8A%E6%B5%B7%E6%96%B0%E5%8D%8E%E5%8C%BB%E9%99%A2&origin_region=%E4%B8%8A%E6%B5%B7&destination_region=%E4%B8%8A%E6%B5%B7&output=json&ak=67c1ea196201cb1521170cf746fb7466
	#url = 'http://api.map.baidu.com/direction/v1?mode=driving&origin=竖新派出所&destination=上海新华医院&origin_region=上海&destination_region=上海&output=json&ak=67c1ea196201cb1521170cf746fb7466'
	html = urllib.request.urlopen(url).read().decode('utf-8')
	json_data = json.loads(html)
	json_data['dt']=dt.strftime('%Y-%m-%d %H:%M:%S')
	#print json_data['result']['origin']['wd'] 
	#print json_data['result']['destination']['wd']
	#print json_data['result']['traffic_condition']
	#print(json.dumps(json_data,encoding="utf-8", indent=4, sort_keys=False, ensure_ascii=False))
	return json.dumps(json_data, indent=4, sort_keys=False, ensure_ascii=False)+','

if __name__ == "__main__":
    application.run()
