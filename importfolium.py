import folium
import webbrowser
import os

# Verificar la versión de Folium
print(folium.__version__)

# Crear un mapa centrado en Londres
london_map = folium.Map(location=[51.5074, -0.1278], zoom_start=12)

# Marcadores para los lugares del itinerario
itinerary_locations = {
    "Buckingham Palace": (51.5014, -0.1419),
    "St. James’s Park": (51.5033, -0.1426),
    "Westminster Abbey": (51.4992, -0.1270),
    "Big Ben": (51.5007, -0.1246),
    "Trafalgar Square": (51.5089, -0.1283),
    "National Gallery": (51.5089, -0.1283),
    "Covent Garden": (51.5120, -0.1229),
    "Chinatown": (51.5110, -0.1281),
    "Piccadilly Circus": (51.5117, -0.1344),
    "Museo de Historia Natural": (51.4967, -0.1764),
    "Museo de Ciencias": (51.4972, -0.1764),
    "Victoria and Albert Museum": (51.4962, -0.1720),
    "Notting Hill": (51.5074, -0.1950),
    "Hyde Park": (51.5072, -0.1657),
    "Kensington Gardens": (51.5060, -0.1944),
    "Camden Town": (51.5416, -0.1426),
    "Tower Bridge": (51.5055, -0.0754),
    "Sky Garden": (51.5127, -0.0815)
}

# Añadir marcadores al mapa
for location, coords in itinerary_locations.items():
    folium.Marker(location=coords, popup=location).add_to(london_map)

# Guardar el mapa en el directorio actual
map_file_path = 'london_itinerary_map.html'
london_map.save(map_file_path)

# Abrir el mapa en el navegador
webbrowser.open('file://' + os.path.realpath(map_file_path))
