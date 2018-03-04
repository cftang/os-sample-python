
cd /tmp
while true 
do
    rm map*
    wget http://127.0.0.1:8080/map2
    sleep 43
    wget http://127.0.0.1:8080/map3
    sleep 43
    wget http://127.0.0.1:8080/map4
    sleep 43
    wget http://127.0.0.1:8080/map5
    sleep 43
done
