---
title: Indiana Studies
layout: page
permalink: /indiana-studies
bannerphoto:
---

<div style="display:flex;align-items:flex-start;gap:2rem;">
  <div style="flex:1;min-width:220px;">
  <h1>Indiana Studies</h1>
  <p>We are studying the collections of ivory in the state of Indiana to better understand the state's history through the observable data of ivory across time. By examining artifacts, craft goods, and industrial products made with ivory, we uncover stories about Indiana's people, economy, and cultural connections from early statehood to the industrial era.</p>

  <h2>Early Statehood</h2>
  <p>During Indiana's early statehood, ivory objects were rare and often imported, reflecting the aspirations and connections of settlers. These items included personal adornments, small tools, and keepsakes that traveled with families as they established new communities.</p>

  <h2>Frontier Craft Goods</h2>
  <p>As Indiana's frontier developed, local craftspeople began to incorporate ivory into their work. Ivory was used in knife handles, sewing tools, and decorative items, blending practicality with artistry and connecting Indiana to global trade networks.</p>

  <h2>Starr Piano</h2>
  <p>The Starr Piano Company, based in Richmond, Indiana, became a major industrial user of ivory in the late 19th and early 20th centuries. Ivory keys produced by Starr Piano are found in instruments across the country, representing Indiana's role in music history and manufacturing.</p>

  <h2>Industrial Period</h2>
  <p>With the rise of industry, ivory use expanded into mass-produced goods, including combs, buttons, and piano keys. Indiana's factories and workshops contributed to the broader story of ivory in American life, while also raising questions about conservation and ethical sourcing.</p>
  </div>
  <div style="flex:0 0 400px;">
    <!-- Leaflet Map of Indiana -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <div id="indiana-map" style="height: 320px; width: 400px; border-radius: 10px; box-shadow: 0 2px 8px #ccc;"></div>
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
      var map = L.map('indiana-map').setView([40.2735, -86.1267], 6.7); // Center Indiana, zoom in
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 12,
        attribution: '© OpenStreetMap contributors'
      }).addTo(map);
  // Marker for Bloomington
  L.marker([39.1653, -86.5264]).addTo(map).bindPopup('Bloomington, IN');
  // Marker for Terre Haute
  L.marker([39.4667, -87.4139]).addTo(map).bindPopup('<b>Terre Haute, IN</b><br>ArchIvory has partnered with the Vigo County Public Library to be a partner at Family Learning Day on September 27th.<br>We will present a formal talk on December 18.');
  // Marker for Porter County (Valparaiso)
  L.marker([41.4731, -87.0611]).addTo(map).bindPopup('<b>Porter County (Valparaiso), IN</b><br>The Porter County History Museum has donated an ivory cane.');
      // Marker for Tipton County (Tipton)
      L.marker([40.2828, -86.0417]).addTo(map).bindPopup('<b>Tipton County (Tipton), IN</b><br>We are presenting a pair of elephant and conservation themed story times at Tipton County Public Library with our Elephantologist Daniella.');
    });
    </script>
  </div>
</div>
