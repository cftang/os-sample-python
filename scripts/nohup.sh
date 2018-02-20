
mkdir ~/.plotly

cp /opt/app-root/src/scripts/.credentials ~/.plotly

nohup python /opt/app-root/src/scripts/sd.heartbeat.py > /tmp/heartbeat.out &

nohup sh /opt/app-root/src/scripts/wget.sh > /tmp/wget.out &

nohup python /opt/app-root/src/scripts/h1.hello.py > /tmp/h1.out &

nohup python /opt/app-root/src/scripts/hello.py > /tmp/hello.out &


