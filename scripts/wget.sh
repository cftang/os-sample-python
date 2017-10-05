
cd /tmp
while true 
do
rm map*
wget http://127.0.0.1:8080/map2
sleep 300
wget http://127.0.0.1:8080/map3
sleep 300
done
