navigator.geolocation.watchPosition(function(location) {
    const roomName = JSON.parse(document.getElementById('room-name').textContent);

    if (window.location.protocol == "https:") {
        var ws_scheme = "wss://";
    } else {
        var ws_scheme = "ws://"
    };

    const mapSocket = new WebSocket(
        ws_scheme
        + window.location.host
        + '/ws/map/'
        + roomName
        + '/'
    );

    var readyState = mapSocket.readyState;

    console.log(readyState)

    var latlng = new L.LatLng(location.coords.latitude, location.coords.longitude);

    var radius = 1000;

    var map = L.map('map').setView(latlng, 14)
    
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);
    
    L.circle(latlng).addTo(map).setRadius(radius);

    mapSocket.onopen = function (event) {
        mapSocket.send(JSON.stringify({
            'latlng': latlng
        }));

        console.log(latlng);
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
            .addTo(map);
            }
        })();

        L.Routing.control({
            waypoints: [
                L.latLng(deliveries[0].lat, deliveries[0].lon),
                L.latLng(deliveries[1].lat, deliveries[1].lon)
            ],
        }).addTo(map);
    };

    mapSocket.onclose = function(e) {
        console.error('Map socket closed unexpectedly');
    };

    mapSocket.onerror = function(event) {
        console.error("WebSocket error observed:", event);
    };
});