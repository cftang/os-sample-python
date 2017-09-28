# -*- coding:utf-8 -*- 
import json
import urllib.request
import urllib.parse
import datetime
import pytz
from testMongo import save2mongo
from copy import deepcopy

from flask import Flask
from flask import request

application = Flask(__name__)


@application.route("/")
def hello():
    return "Hello World! python 3.5"


@application.route("/map1")
def map1():
    show = request.args.get('show')
    if show=='y':
        return "Hello World! map1"
    else:
        return '0'

@application.route("/map2")
def map2():
    show = request.args.get('show')

    params = {
        'mode': 'driving',
        'origin': u'绿色米兰奥特莱斯',
        'destination': u'四平路773号金大地商务楼',
        'origin_region': u'上海',
        'destination_region': u'上海',
        'waypoints': u'上海市鞍山实验中学',
        'output': 'json',
        'ak': '67c1ea196201cb1521170cf746fb7466'
    }
    url = 'http://api.map.baidu.com/direction/v1?%s' % urllib.parse.urlencode(params)

    # with urllib.request.urlopen(url) as f:
    #	print(f.read().decode('utf-8'))

    tz = pytz.timezone('Asia/Shanghai')
    dt = datetime.datetime.now(tz)

    # print (dt.strftime('%Y-%m-%d %H:%M:%S'))
    # http://api.map.baidu.com/direction/v1?mode=driving&origin=%E7%AB%96%E6%96%B0%E6%B4%BE%E5%87%BA%E6%89%80&destination=%E4%B8%8A%E6%B5%B7%E6%96%B0%E5%8D%8E%E5%8C%BB%E9%99%A2&origin_region=%E4%B8%8A%E6%B5%B7&destination_region=%E4%B8%8A%E6%B5%B7&output=json&ak=67c1ea196201cb1521170cf746fb7466
    # url = 'http://api.map.baidu.com/direction/v1?mode=driving&origin=竖新派出所&destination=上海新华医院&origin_region=上海&destination_region=上海&output=json&ak=67c1ea196201cb1521170cf746fb7466'
    html = urllib.request.urlopen(url).read().decode('utf-8')
    json_data = json.loads(html)
    json_data['dt'] = dt.strftime('%Y-%m-%d %H:%M:%S')
    # print json_data['result']['origin']['wd']
    # print json_data['result']['destination']['wd']
    # print json_data['result']['traffic_condition']
    # print(json.dumps(json_data,encoding="utf-8", indent=4, sort_keys=False, ensure_ascii=False))
    #json_data = json.loads(html)
    json_data2 = deepcopy(json_data)
    save2mongo('baidu','map2', json_data2)
    if show=='y':
        return json.dumps(json_data, indent=4, sort_keys=False, ensure_ascii=False) + ','
    else:
        return '0'

@application.route("/map3")
def map3():
    show = request.args.get('show')

    params = {
        'mode': 'driving',
        'origin': '竖新派出所',
        'destination': '国科路29弄1号',
        'origin_region': '上海',
        'destination_region': '上海',
        'output': 'json',
        'ak': '67c1ea196201cb1521170cf746fb7466'
    }
    url = 'http://api.map.baidu.com/direction/v1?%s' % urllib.parse.urlencode(params)

    # with urllib.request.urlopen(url) as f:
    #	print(f.read().decode('utf-8'))

    tz = pytz.timezone('Asia/Shanghai')
    dt = datetime.datetime.now(tz)

    # print (dt.strftime('%Y-%m-%d %H:%M:%S'))
    # http://api.map.baidu.com/direction/v1?mode=driving&origin=%E7%AB%96%E6%96%B0%E6%B4%BE%E5%87%BA%E6%89%80&destination=%E4%B8%8A%E6%B5%B7%E6%96%B0%E5%8D%8E%E5%8C%BB%E9%99%A2&origin_region=%E4%B8%8A%E6%B5%B7&destination_region=%E4%B8%8A%E6%B5%B7&output=json&ak=67c1ea196201cb1521170cf746fb7466
    # url = 'http://api.map.baidu.com/direction/v1?mode=driving&origin=竖新派出所&destination=上海新华医院&origin_region=上海&destination_region=上海&output=json&ak=67c1ea196201cb1521170cf746fb7466'
    html = urllib.request.urlopen(url).read().decode('utf-8')
    json_data = json.loads(html)
    json_data['dt'] = dt.strftime('%Y-%m-%d %H:%M:%S')
    # print json_data['result']['origin']['wd']
    # print json_data['result']['destination']['wd']
    # print json_data['result']['traffic_condition']
    # print(json.dumps(json_data,encoding="utf-8", indent=4, sort_keys=False, ensure_ascii=False))
    #return json.dumps(json_data, indent=4, sort_keys=False, ensure_ascii=False) + ','
    json_data2 = deepcopy(json_data)
    save2mongo('baidu','map3', json_data2)
    if show=='y':
        return json.dumps(json_data, indent=4, sort_keys=False, ensure_ascii=False) + ','
    else:
        return '0'

if __name__ == "__main__":
    application.run()
