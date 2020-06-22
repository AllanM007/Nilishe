const roomName = JSON.parse(document.getElementById('room-name').textContent);

const mapSocket = new WebSocket(
    'wss://'
    + window.location.host
    + '/ws/map/'
    + roomName
    + '/'
);

uRL = (mapSocket.url)

mapSocket.onopen = function (event) {
    mapSocket.send(JSON.stringify({
        'latlng': latlng
    }));

    console.log(latlng);
    
    console.log('map data sent');
};

mapSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    console.log(data.latlng.lat, data.latlng.lng);

    var deliveries = [
        { "lat": location.coords.latitude, "lon": location.coords.longitude},
        { "lat": data.latlng.lat, "lon": data.latlng.lng},
    ];

    var marker = (function() {
    for (let index = 0; index < deliveries.length; index++) {
        L.marker([deliveries[index].lat, deliveries[index].lon])
        .bindPopup("Your delivery is within " + radius + " meters of your area")
        .addTo(mymap);
        }
    })();

    L.Routing.control({
        waypoints: [
            L.latLng(deliveries[0].lat, deliveries[0].lon),
            L.latLng(deliveries[1].lat, deliveries[1].lon)
        ]
    }).addTo(mymap);
};

mapSocket.onclose = function(e) {
    console.error('Map socket closed unexpectedly');
};

mapSocket.onerror = function(event) {
    console.error("WebSocket error observed:", event);
};

var map = L.map('mapid'),
    realtime = L.realtime({
        //url: 'https://wanderdrone.appspot.com/',
        url: uRL,
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