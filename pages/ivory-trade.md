---
title: Ivory Trade
layout: page
permalink: /pages/ivory-trade
bannerphoto: research.jpg
---

<div class="cell large-10">
<h3>The Ivory Trade</h3>
<p>This interactive map visualizes the global ivory trade from the 19th century onward, tracing the movement of ivory from African elephant populations to major ports, manufacturing centers, and consumer markets around the world. Colored lines represent maritime and overland trade routes, while shaded regions and circles highlight areas of production, industry, and consumption. Click on markers, polygons, and circles to reveal popups with historical context and details about each location's role in the ivory trade. Use the map to explore how technological innovation, shifting political conditions, and consumer demand shaped the flow of ivory and transformed societies across continents. The map is a tool for understanding the interconnected histories of people, places, and commodities in the age of global trade.</p>
</div>

<div id="ivory-map" style="height: 600px; margin-bottom: 2em;"></div>

<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />

<script>
		var map = L.map('ivory-map').setView([10, 20], 2);
		L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
			maxZoom: 18,
			attribution: '© OpenStreetMap contributors'
		}).addTo(map);


		   // More accurate polygon for the Omani Empire (c. 1800)
		   var omaniEmpireCoords = [
			   [25.5, 56.3],   // Musandam Peninsula (UAE/Oman)
			   [24.3, 54.4],   // Abu Dhabi
			   [22.5, 55.9],   // Near Al Ain
			   [20.0, 58.6],   // Sur, Oman
			   [17.0, 55.0],   // Dhofar, Oman
			   [16.0, 52.0],   // Yemen border
			   [14.0, 51.0],   // Socotra (Yemen, Omani influence)
			   [11.9, 50.0],   // Eyl, Somalia
			   [2.0, 45.5],    // Kismayo, Somalia
			   [-1.3, 41.8],   // Mombasa, Kenya
			   [-4.0, 39.7],   // Zanzibar
			   [-8.5, 39.5],   // Kilwa, Tanzania
			   [-10.5, 40.5],  // Northern Mozambique
			   [-10.5, 40.0],  // Mozambique coast (hug coast)
			   [-10.0, 39.0],  // Mozambique coast (hug coast)
			   [-8.5, 39.0],   // Back up coast
			   [-4.0, 39.5],   // Back up to Zanzibar
			   [0.0, 42.0],    // Back up to Somalia coast
			   [11.5, 43.0],   // Mogadishu, Somalia
			   [14.0, 51.0],   // Socotra (repeat for closure)
			   [25.0, 61.5],   // Gwadar, Pakistan (Omani exclave)
			   [27.5, 56.3],   // Bandar Abbas, Iran
			   [25.5, 56.3]    // Close polygon at Musandam
		   ];
		   var omaniEmpirePolygon = L.polygon(omaniEmpireCoords, {
			   color: 'orange',
			   fillColor: '#ffa500',
			   fillOpacity: 0.35,
			   weight: 2
		   }).addTo(map);
		   omaniEmpirePolygon.bindPopup('Approximate historical region of the Omani Empire (c. 1800)');

		   // Add info marker for the Omani Empire
		   var omaniEmpireMarker = L.marker([23.6, 58.5], {title: 'Omani Empire'}).addTo(map);
		   omaniEmpireMarker.bindPopup('<b>Omani Empire</b><br><a href="/pages/omani-empire.html" target="_blank">Learn more about the Omani Empire</a>');

	   // Example markers
	// Gujarat, India marker
	L.marker([22.3094, 72.1362]).addTo(map)
		.bindPopup('<b>Gujarat, India</b><br>Historic center of Indian Ocean trade and ivory craftsmanship.');

	// Paris, France marker
	L.marker([48.8566, 2.3522]).addTo(map)
		.bindPopup('<b>Paris, France</b><br>Major European center for art, luxury, and ivory craftsmanship.');

	// London, UK marker
	L.marker([51.5074, -0.1278]).addTo(map)
		.bindPopup('<b>London, UK</b><br>Major European hub for ivory trade, art, and commerce.');
	L.marker([40.0, -86.0]).addTo(map)
		.bindPopup('<b>Indiana, USA</b><br>Historic center for piano manufacturing and ivory use in the United States.<br>' +
		'<a href="/pages/fort-wayne.html" target="_blank">Fort Wayne</a> | ' +
		'<a href="/pages/richmond.html" target="_blank">Richmond</a> | ' +
		'<a href="/pages/new-harmony.html" target="_blank">New Harmony</a>');
	// Line from Ivoryton, Connecticut to Indiana, USA
	var ivorytonToIndiana = [
		[41.3476, -72.4426], // Ivoryton, Connecticut
		[40.0, -86.0]       // Indiana, USA
	];
	L.polyline(ivorytonToIndiana, {color: 'black', weight: 3, opacity: 0.7, dashArray: '4,6'}).addTo(map)
		.bindPopup('Ivory route: Ivoryton, Connecticut to Indiana');
	L.marker([41.3476, -72.4426]).addTo(map)
		.bindPopup('<b>Ivoryton, Connecticut</b><br>Historic center of US ivory manufacturing.');


	// Trade route from Zanzibar to Morocco (maritime, hugging coast but not touching land)
		   var tradeRoute = [
			   [-6.1659, 39.2026],    // Zanzibar
			   [-10, 43],             // Mozambique Channel, between Africa and Madagascar
			   [-15, 40],             // Mozambique coast
			   [-18, 37],             // Just offshore, southern Mozambique
			   [-22, 35],             // Just offshore, northern South Africa
			   [-28, 32],             // Just offshore, Durban, South Africa
			   [-33, 25],             // Just offshore, Port Elizabeth
			   [-34, 18],             // Cape Town, South Africa
			   [-28, 16],             // Lüderitz, Namibia
			   [-22, 14],             // Walvis Bay, Namibia
			   [-17, 11],             // Near Luanda, Angola
			   [-8.5, 13.7],          // Offshore Angola, hugging the coast
			   [-4.0, 8.8],           // Offshore Gabon
			   [2.8, 9.1],            // Douala, Cameroon (close to coast)
			   [4.5, 8.5],            // Lagos, Nigeria (close to coast)
			   [5.5, 0.0],            // Accra, Ghana (close to coast)
			   [4.0, -2.0],           // Abidjan, Côte d'Ivoire (hugging the coast)
			   [-4.8, -7.4],          // Monrovia, Liberia (hugging the coast)
			   [9.5, -13.7],          // Conakry, Guinea (hugging the coast)
			   [12.6, -16.3],         // Banjul, The Gambia (hugging the coast)
			   [14.7, -17.5],         // Dakar, Senegal (hugging the coast)
			   [25, -15],             // Off Morocco
			   [31.7917, -7.0926],    // Morocco (final port in Africa)
			   [41.3476, -72.4426]    // Ivoryton, Connecticut, USA
		   ];
		   L.polyline(tradeRoute, {color: 'red', weight: 4, opacity: 0.7, dashArray: '10,10'}).addTo(map)
			   .bindPopup('Ivory trade route: Zanzibar to Morocco to Ivoryton, Connecticut (maritime route, not touching land)');

	   // New trade route from Zanzibar to Gujarat (blue)
	   var tradeRouteGujarat = [
		   [-6.1659, 39.2026],    // Zanzibar
		   [0, 50],               // Indian Ocean, mid-route
		   [10, 60],              // Indian Ocean, approaching India
		   [22.3094, 72.1362]     // Gujarat, India
	   ];
	   L.polyline(tradeRouteGujarat, {color: 'blue', weight: 4, opacity: 0.7, dashArray: '5,10'}).addTo(map)
		   .bindPopup('Ivory trade route: Zanzibar to Gujarat, India (Indian Ocean route)');


		   // New trade route from Morocco to London via Atlantic coast and English Channel (green)
			   var tradeRouteLondon = [
				   [31.7917, -7.0926],    // Morocco
				   [36.0, -9.0],          // Off Lisbon, Portugal
				   [43.0, -8.0],          // Off Galicia, Spain
				   [47.0, -3.0],          // Off Brittany, France
				   [50.0, 0.0],           // English Channel
				   [51.5074, -0.1278]     // London, UK
			   ];
			   L.polyline(tradeRouteLondon, {color: 'green', weight: 4, opacity: 0.7, dashArray: '2,8'}).addTo(map)
				   .bindPopup('Ivory trade route: Morocco to London via Atlantic and English Channel');

// New trade route from London to New York (purple)
var tradeRouteNY = [
	[51.5074, -0.1278],    // London, UK
	[53.0, -20.0],         // North Atlantic, mid-route
	[50.0, -40.0],         // North Atlantic, mid-route
	[42.3601, -71.0589],   // Boston, USA (optional stop)
	[40.7128, -74.0060]    // New York, USA
];
L.polyline(tradeRouteNY, {color: 'purple', weight: 4, opacity: 0.7, dashArray: '4,8'}).addTo(map)
	.bindPopup('Ivory trade route: London to New York (transatlantic route)');
// London, UK marker
L.marker([51.5074, -0.1278]).addTo(map)
	.bindPopup('<b>London, UK</b><br>Major European hub for ivory trade, art, and commerce.');

// New trade route from Cherbourg to the St. Lawrence River (orange)
var tradeRouteStLawrence = [
	[49.6337, -1.6221],    // Cherbourg, France
	[51.0, -10.0],         // North Atlantic, mid-route
	[52.0, -30.0],         // North Atlantic, mid-route
	[52.5, -48.0],         // North of Newfoundland
	[51.5, -55.0],         // North of Newfoundland
	[50.5, -59.0],         // North of Newfoundland, entering Gulf
	[49.7, -63.5],         // North of Île d'Anticosti
	[49.3, -65.5],         // West of Île d'Anticosti, entering St. Lawrence
	[46.8139, -71.2082]    // Quebec City, St. Lawrence River
];
L.polyline(tradeRouteStLawrence, {color: 'orange', weight: 4, opacity: 0.7, dashArray: '6,8'}).addTo(map)
	.bindPopup('Ivory trade route: Cherbourg to St. Lawrence River (Quebec City)');

	   // New trade route from Massachusetts to Zanzibar (brown)
	var tradeRouteMAtoZanzibar = [
		[44.3601, -71.0589],   // Boston, Massachusetts (offset +2.0 lat)
		[43.3476, -72.4426],   // Ivoryton, Connecticut
		[33.7917, -7.0926],    // Morocco (offset +2.0 lat)
		[27, -15],             // Off Morocco
		[25, -15],             // Continue hugging coast (no ocean detour)
		[14.7, -17.5],         // Dakar, Senegal
		[12.6, -16.3],         // Banjul, The Gambia
		[9.5, -13.7],          // Conakry, Guinea
		[-4.8, -7.4],          // Monrovia, Liberia
		[4.0, -2.0],           // Abidjan, Côte d'Ivoire
		[5.5, 0.0],            // Accra, Ghana
		[4.5, 8.5],            // Lagos, Nigeria
		[2.8, 9.1],            // Douala, Cameroon
		[-4.0, 8.8],           // Offshore Gabon
		[-8.5, 13.7],          // Offshore Angola
		[-17, 11],             // Near Luanda, Angola
		[-22, 14],             // Walvis Bay, Namibia
		[-28, 16],             // Lüderitz, Namibia
		[-33, 25],             // Just offshore, Port Elizabeth
		[-34, 18],             // Cape Town, South Africa
		[-28, 32],             // Just offshore, Durban, South Africa
		[-22, 35],             // Just offshore, northern South Africa
		[-18, 37],             // Just offshore, southern Mozambique
		[-15, 40],             // Mozambique coast
		[-10, 43],             // Mozambique Channel
		[-6.1659, 39.2026]     // Zanzibar
];
L.polyline(tradeRouteMAtoZanzibar, {color: 'brown', weight: 4, opacity: 0.7, dashArray: '8,8'}).addTo(map)
	.bindPopup('Ivory trade route: Massachusetts to Zanzibar (reverse of main route)');

// Marker for midpoint in the Atlantic, placed off the brown route for clarity
L.marker([34.0, -44.0]).addTo(map)
	.bindPopup('<b>Mid-Atlantic Point</b><br>Here, US traders crossed the Atlantic carrying gunpowder and the famous Massachusetts-made <i>merikani</i> cloth, a key trade good in East Africa. These goods were exchanged for ivory and other commodities in Zanzibar and beyond.');

	// Marker for Zanzibar & the Swahili City States (grouped)
L.marker([-6.1659, 39.2026]).addTo(map)
	.bindPopup('<b>Zanzibar & the Swahili City States</b><br>\
<img src="/assets/img/port of zanzibar.webp" alt="Port of Zanzibar" style="width:180px; margin-top:8px; border-radius:6px; border:1px solid #ccc;"><br>\
This region, including <a href="/pages/zanzibar.html" target="_blank">Zanzibar</a>, <a href="/pages/bagamoyo.html" target="_blank">Bagamoyo</a>, and <a href="/pages/tabora.html" target="_blank">Tabora</a>, was a vibrant center of Swahili culture and commerce. After centuries of struggle, these city states were conquered by the Omani Empire. The mercantile-minded Omanis moved their capital to Zanzibar in 1840 to oversee the region\'s rich trade. The Swahili city states were crucial hubs for the ivory trade, connecting the African interior to the Indian Ocean world. Zanzibar served as a major port, Bagamoyo as a key coastal entry, and Tabora as an inland crossroads for caravans. Together, these cities played a pivotal role in the movement of people, goods, and ideas across East Africa and beyond.');

// Major ivory ports in Qing dynasty China
L.marker([23.1291, 113.2644]).addTo(map)
	.bindPopup('<b>Guangzhou (Canton), China</b><br>Primary port for ivory imports during the Qing dynasty, connecting China to Africa and Southeast Asia.');
L.marker([31.2304, 121.4737]).addTo(map)
	.bindPopup('<b>Shanghai, China</b><br>Major international port for ivory and luxury goods in the late Qing era.');

// Maritime ivory trade route: Gujarat to Guangzhou (not touching land)
var routeGujaratGuangzhou = [
	[22.3094, 72.1362], // Gujarat, India
	[15, 90],           // Indian Ocean, mid-route
	[10, 110],          // South China Sea, mid-route
	[23.1291, 113.2644] // Guangzhou, China
];
L.polyline(routeGujaratGuangzhou, {color: 'teal', weight: 4, opacity: 0.7, dashArray: '8,8'}).addTo(map)
	.bindPopup('Maritime ivory route: Gujarat to Guangzhou (not touching land)');

// Maritime ivory trade route: Gujarat to Shanghai (not touching land)
var routeGujaratShanghai = [
	[22.3094, 72.1362], // Gujarat, India
	[15, 90],           // Indian Ocean, mid-route
	[10, 120],          // East China Sea, mid-route
	[31.2304, 121.4737] // Shanghai, China
];
L.polyline(routeGujaratShanghai, {color: 'navy', weight: 4, opacity: 0.7, dashArray: '8,8'}).addTo(map)
	.bindPopup('Maritime ivory route: Gujarat to Shanghai (not touching land)');

	// Bengal waypoint for ivory trade
L.marker([22.5726, 88.3639]).addTo(map)
	.bindPopup('<b>Bengal (Kolkata), India</b><br>Major waypoint for ivory trade between India and China.');

// Maritime ivory trade route: Gujarat → Bengal → Guangzhou (not touching land)
var routeGujaratBengalGuangzhou = [
	[22.3094, 72.1362], // Gujarat, India
	[22.5726, 88.3639], // Bengal (Kolkata), India
	[15, 100],          // Bay of Bengal, mid-route
	[10, 110],          // South China Sea, mid-route
	[23.1291, 113.2644] // Guangzhou, China
];
L.polyline(routeGujaratBengalGuangzhou, {color: 'teal', weight: 4, opacity: 0.7, dashArray: '8,8'}).addTo(map)
	.bindPopup('Maritime ivory route: Gujarat → Bengal → Guangzhou (not touching land)');

// Maritime ivory trade route: Gujarat → Bengal → Shanghai (not touching land)
var routeGujaratBengalShanghai = [
	[22.3094, 72.1362], // Gujarat, India
	[22.5726, 88.3639], // Bengal (Kolkata), India
	[15, 110],          // Bay of Bengal, mid-route
	[10, 120],          // East China Sea, mid-route
	[31.2304, 121.4737] // Shanghai, China
];
L.polyline(routeGujaratBengalShanghai, {color: 'navy', weight: 4, opacity: 0.7, dashArray: '8,8'}).addTo(map)
	.bindPopup('Maritime ivory route: Gujarat → Bengal → Shanghai (not touching land)');

	// East Africa elephant hunting progression region (shaded polygon)
	var eastAfricaIvoryRegion = [
		[-8, 39],   // Southern Tanzania
		[-8, 33],   // Southwest Tanzania
		[-6, 31],   // Near Lake Tanganyika
		[-2, 30],   // Rwanda/Burundi border
		[0, 32],    // Lake Victoria region
		[2, 36],    // Kenya interior
		[-1, 39],   // Kenya coast
		[-4, 39],   // Back to Tanzania coast
		[-8, 39]    // Close polygon
	];
	var eastAfricaIvoryPolygon = L.polygon(eastAfricaIvoryRegion, {
		color: 'red',
		fillColor: '#ff4444',
		fillOpacity: 0.35,
		weight: 2
	}).addTo(map);
	eastAfricaIvoryPolygon.bindPopup('<b>East Africa Elephant Hunting Region</b><br>In the 19th century, intensive hunting for ivory along the East African coast led to a rapid decline in local elephant populations. As coastal herds disappeared, hunters and traders pushed further into the interior, seeking new sources of ivory. This progression from the coast to the heart of the continent transformed trade routes, settlement patterns, and the environment, leaving a lasting impact on East Africa.');

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
    centralTanzaniaPolygon.bindPopup('<b>Professional Commodity Exporters</b><br>In the 19th century, groups such as the Nyamwezi and the Majikenda emerged as professional commodity exporters, funneling ivory and other goods to the coast in response to growing demand. These groups augmented older regional routes for salt and iron across central Tanzania and linked them directly to Swahili markets. Contrary to Western assumptions, these people were not slaves, but wage earners who competed directly with Arab and Swahili merchants.');

// United States ivory industry region (large green circle in Kansas)
var usIvoryCircle = L.circle([39.0, -98.0], {
	color: 'green',
	fillColor: '#44ff44',
	fillOpacity: 0.35,
	radius: 700000
}).addTo(map);
usIvoryCircle.bindPopup('<b>US Ivory Industry</b><br>The United States became a global center for ivory manufacturing in the 19th century. Factories in the heartland and New England processed imported ivory into piano keys, combs, and luxury goods, fueling demand and shaping trade routes worldwide.');

// China ivory industry region (large circle in central China)

var chinaIvoryCircle = L.circle([34.0, 108.0], {
	color: 'gold',
	fillColor: '#ffd700',
	fillOpacity: 0.35,
	radius: 700000
}).addTo(map);
chinaIvoryCircle.bindPopup('<b>China Ivory Industry</b><br>China became a major center for ivory carving and consumption in the 18th and 19th centuries. As native elephant populations declined, China imported ivory from India and Africa, fueling a global network of trade and craftsmanship.');

</script>
