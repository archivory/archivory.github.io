---
title: Elephant Harvesting Patterns: Africa- 19th Century
layout: page
permalink: /pages/elephant-harvesting-patterns
bannerphoto: research.jpg
---

<div class="cell large-10">
<h2>Elephant Harvesting Patterns: Africa- 19th Century</h2>
<p>This interactive map visualizes the regions and patterns of elephant harvesting in East Africa during the nineteenth century, with a focus on Tanzania. Explore the map to see key hunting areas, trade routes, and the environmental impact of ivory extraction.</p>
</div>

<div id="harvesting-map" style="height: 600px; margin-bottom: 2em;"></div>

<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />

<script>
    var map = L.map('harvesting-map').setView([-6.3690, 34.8888], 6); // Centered on Tanzania
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 18,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);
    // Example marker for Dar es Salaam
    L.marker([-6.7924, 39.2083]).addTo(map)
        .bindPopup('<b>Dar es Salaam</b><br>Major port and trade hub for ivory in the nineteenth century.');
    // Marker for Mrima Coast region with historical context
    L.marker([-5.0, 39.5]).addTo(map)
        .bindPopup('<b>Mrima Coast</b><br>This region was the first in East Africa to be intensively exploited and cleared of elephant populations during the nineteenth-century ivory trade. The Mrima Coast, stretching from Mombasa to Dar es Salaam, played a pivotal role in the early history of ivory extraction and export.');
    // Further expanded polygon near Mombasa and inland
    var coastPolygonCoords = [
        [-3.8, 39.5],   // Inland northwest of Mombasa
        [-4.05, 39.68], // Mombasa (coast)
        [-4.5, 39.75],  // South of Mombasa (coast)
        [-5.07, 39.10], // Tanga (inland)
        [-5.5, 38.80],  // Inland from Pangani
        [-6.44, 38.50], // Inland from Bagamoyo
        [-6.81, 38.90], // Inland from Dar es Salaam
        [-6.81, 39.28], // Dar es Salaam (coast)
        [-6.44, 38.90], // Bagamoyo (coast)
        [-5.5, 39.30],  // Pangani (coast)
        [-5.07, 39.10], // Tanga (coast)
        [-4.5, 39.75],  // South of Mombasa (coast)
        [-3.8, 39.5]    // Close polygon inland near Mombasa
    ];
    var coastPolygon = L.polygon(coastPolygonCoords, {
        color: 'blue',
        fillColor: '#3399ff',
        fillOpacity: 0.35,
        weight: 2
    }).addTo(map);
    coastPolygon.bindPopup('<b>Expanded Coastal & Inland Region: Mombasa to Dar es Salaam</b><br>This region now includes a larger inland area near Mombasa, as well as the coast and adjacent interior.');
    // Polygon for central Tanzania region including Legogo and Nyamwezi
    var centralTanzaniaCoords = [
        [-5.5, 34.5], // Near Tabora (Nyamwezi region)
        [-5.0, 35.5], // North of Tabora
        [-6.5, 36.5], // East of Tabora (Legogo region)
        [-7.5, 36.0], // South of Legogo
        [-7.0, 35.0], // Southwest of Legogo
        [-6.0, 34.0], // West of Tabora
        [-5.5, 34.5]  // Close polygon
    ];
    var centralTanzaniaPolygon = L.polygon(centralTanzaniaCoords, {
        color: 'red',
        fillColor: '#ff6666',
        fillOpacity: 0.35,
        weight: 2
    }).addTo(map);
    centralTanzaniaPolygon.bindPopup('<b>Central Tanzania: Legogo & Nyamwezi</b><br>This region, including the Legogo and Nyamwezi areas, was a major center for elephant hunting and ivory trade in the nineteenth century.');
    // Polygon for West Shore of Lake Victoria and Rwanda-Burundi region
    var lakeVictoriaWestCoords = [
        [-1.0, 31.5], // West shore of Lake Victoria (Tanzania)
        [-1.5, 30.5], // North Rwanda
        [-2.5, 29.7], // Rwanda
        [-3.5, 29.6], // Burundi
        [-4.0, 30.0], // South Burundi
        [-3.0, 31.0], // South of Lake Victoria
        [-1.0, 31.5]  // Close polygon
    ];
    var lakeVictoriaWestPolygon = L.polygon(lakeVictoriaWestCoords, {
        color: 'green',
        fillColor: '#66ff66',
        fillOpacity: 0.35,
        weight: 2
    }).addTo(map);
    lakeVictoriaWestPolygon.bindPopup('<b>West Shore of Lake Victoria & Rwanda-Burundi</b><br>This region was a significant area for elephant populations and ivory trade, especially in the nineteenth century.');
</script>
