
while true 
do
    python ~/test1.py map2 "G40沪陕高速(上海高东收费口->崇明陈家镇收费口)路况 更新时间:"
    sleep 900
    python ~/test1.py map3 "G40沪陕高速(崇明陈家镇收费口->上海高东收费口)路况 更新时间:"
    sleep 900
    python ~/test1.py map4 "翔殷路隧道(西向东)路况 更新时间:"
    sleep 900
    python ~/test1.py map5 "翔殷路隧道(东向西)路况 更新时间:"
    sleep 900
done
