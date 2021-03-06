# -*- coding:utf-8 -*- 
import json
import urllib.request
import urllib.parse
import datetime
import pytz
from testMongo import save2mongoMap2, save2mongoMap3, save2mongoMap4, save2mongoMap5
from copy import deepcopy

from flask import Flask, request, send_from_directory

application = Flask(__name__, static_url_path='')

@application.route("/")
def hello():
    return "Hello World! python 3.5"

# How to serve static files in Flask
# https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask

@application.route("/plot")
def plot():
    return "<iframe width=\"900\" height=\"800\" frameborder=\"0\" \
             scrolling=\"no\" src=\"//plot.ly/~cftang/28.embed\"></iframe>"

@application.route("/plot1")
def plot1():
    return application.send_static_file('plot.html')

@application.route('/plot2')
def plot2():
    return send_from_directory('scripts', 'temp-plot.html')

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
        'origin': '国科路29弄1号',
        'destination': '竖新派出所',
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
    #json_data = json.loads(html)
    json_data2 = deepcopy(json_data)
    save2mongoMap2('baidu', 'map2', json_data2)
    if show == 'y':
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
    save2mongoMap3('baidu', 'map3', json_data2)
    if show == 'y':
        return json.dumps(json_data, indent=4, sort_keys=False, ensure_ascii=False) + ','
    else:
        return '0'


@application.route("/map4")
def map4():
    show = request.args.get('show')

    params = {
        'mode': 'driving',
        'origin': '上海市鞍山实验中学',
        'destination': '上海市浦东新区高行镇朱家浜村民委员会',
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
    save2mongoMap4('baidu', 'map4', json_data2)
    if show == 'y':
        return json.dumps(json_data, indent=4, sort_keys=False, ensure_ascii=False) + ','
    else:
        return '0'


@application.route("/map5")
def map5():
    show = request.args.get('show')

    params = {
        'mode': 'driving',
        'origin': '上海市浦东新区浦东北路1569号',
        'destination': '翔殷路300弄2号',
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
    save2mongoMap5('baidu', 'map5', json_data2)
    if show == 'y':
        return json.dumps(json_data, indent=4, sort_keys=False, ensure_ascii=False) + ','
    else:
        return '0'


if __name__ == "__main__":
    application.run()
