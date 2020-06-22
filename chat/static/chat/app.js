const roomName = JSON.parse(document.getElementById('room-name').textContent);

const mapSocket = new WebSocket(
    'wss://'
    + window.location.host
    + '/ws/map/'
    + roomName
    + '/'
);

uRL = (mapSocket.url)

var map = L.map('mapid'),
    realtime = L.realtime({
        url: 'https://wanderdrone.appspot.com/',
        //url: uRL,
        crossOrigin: true,
        type: 'json'
    }, {
        interval: 3 * 1000
    }).addTo(map);

realtime.on('update', function() {
    map.fitBounds(realtime.getBounds(), {maxZoom: 3});
});

L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);