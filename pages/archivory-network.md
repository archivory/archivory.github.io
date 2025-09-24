---
title: ArchIvory Network
layout: page
permalink: /pages/archivory-network
bannerphoto: research.jpg
---


<div class="cell large-10">
<h3>The ArchIvory Network</h3>
<p>This page introduces the people and institutions collaborating on the ArchIvory project. More information about our network and partners will be added soon.</p>
</div>

<div id="indiana-map" style="height: 400px; margin-bottom: 2em;"></div>

<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />

<script>
	var indianaMap = L.map('indiana-map').setView([39.7684, -86.1581], 7); // Centered on Indiana
	L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
		maxZoom: 18,
		attribution: '© OpenStreetMap contributors'
	}).addTo(indianaMap);

		// Example marker: Indiana University Bloomington
		L.marker([39.1653, -86.5264]).addTo(indianaMap)
			.bindPopup('<b>Indiana University Bloomington</b>');

		// Vigo County Public Library
		L.marker([39.4667, -87.4139]).addTo(indianaMap)
			.bindPopup('<b>Vigo County Public Library</b>');

		// New Harmony, Indiana: Working Men's Institute
		L.marker([38.1295, -87.9359]).addTo(indianaMap)
			.bindPopup('<b>New Harmony, Indiana</b><br>The Working Men\'s Institute, founded in 1838, is Indiana\'s oldest public library and a center for education, research, and community engagement. Established by philanthropist William Maclure, it served as a hub for working people to access books, lectures, and scientific resources, reflecting New Harmony\'s legacy as a utopian community and intellectual center.');

		// Porter County, Indiana: Porter County History Museum
		L.marker([41.4748, -87.0551]).addTo(indianaMap)
			.bindPopup('<b>Porter County History Museum</b><br>The Porter County History Museum in Valparaiso, Indiana, preserves and shares the rich heritage of Porter County. The museum generously donated an ivory cane to the ArchIvory project, supporting our research and educational mission.');

		// Brazil, Indiana: ArchIvory Programming
		L.marker([39.5231, -87.1250]).addTo(indianaMap)
			.bindPopup('<b>Brazil, Indiana</b><br>The ArchIvory project is actively engaged in programming and outreach in Brazil, Indiana, bringing educational events and research to the local community.');
</script>
