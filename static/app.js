// Sample JavaScript code using Leaflet.js to display a map and fetch river flow data

const map = L.map('map').setView([37.8, -96], 4); // Set initial map view
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

// Fetch river flow data from the Flask API endpoint
axios.get('/river_flow_data')
    .then(response => {
        // Process the data and display it on the map
        console.log(response.data);
    })
    .catch(error => {
        console.error('Error fetching river flow data:', error);
    });
