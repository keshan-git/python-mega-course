import folium
import pandas as pd

marker_popup_template = '<b>{}</b> (<i>elevation={}m</i>) <br>Located in {} <hr><em>Status</em>:{} <br><em>Type</em>:{}'


def create_popup(data):
    content = marker_popup_template.format(data['NAME'], data['ELEV'], data['LOCATION'], data['STATUS'], data['TYPE'])
    return folium.Popup(html=content, max_width=150)


def create_icon(data):
    elev = data['ELEV']
    color = 'red'
    if elev < 1000:
        color = 'green'
    elif elev < 3000:
        color = 'orange'
    return folium.Icon(icon='binoculars', prefix='fa', color=color)


def population_style_function(param):
    population = param['properties']['POP2005']
    color = 'red'
    if population < 10000000:
        color = 'green'
    elif population < 20000000:
        color = 'orange'

    return {'fillColor': color}

map = folium.Map(location=[38.58, -99.09], zoom_start=6)
# map.add_child(folium.Marker(location=[38.2, -99.1], popup='Test marker', icon=folium.Icon(color='green')))

group = folium.FeatureGroup(name='Markers')
map.add_child(group)

group.add_child(folium.Marker(location=[38.2, -99.1], popup='Test marker', icon=folium.Icon(color='green')))
group.add_child(folium.Marker(location=[37.2, -97.1], popup='Test marker', icon=folium.Icon(color='green')))

for coordinates in [[36.2, -98.1], [36.2, -97.1]]:
    group.add_child(folium.Marker(location=coordinates, popup='Test marker', icon=folium.Icon(color='green')))
    group.add_child(folium.Marker(location=coordinates, popup='Test marker', icon=folium.Icon(color='green')))

volcano_group = folium.FeatureGroup(name='Volcanoe Markers')
map.add_child(volcano_group)

data_set = pd.read_csv('data/volcanoes.txt')

# for lat, lon in zip(data_set['LAT'], data_set['LON']):
#     group.add_child(folium.Marker(location=[lat, lon], popup='Test marker', icon=folium.Icon(color='green')))

for index, row in data_set.iterrows():
    group.add_child(folium.Marker(location=[row['LAT'], row['LON']], popup=create_popup(row), icon=create_icon(row)))

word_group = folium.FeatureGroup(name='World Layer')
map.add_child(word_group)

data_json = open("data/world.json", 'r', encoding='utf-8-sig').read()
word_group.add_child(folium.GeoJson(data=data_json, style_function=population_style_function))

map.add_child(folium.LayerControl())

map.save('target/webmap.html')
print('WebMap is generated in target folder')