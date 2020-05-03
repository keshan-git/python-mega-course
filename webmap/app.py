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


def create_volcano_marker_layer():
    file_name = 'data/volcanoes.txt'
    print('Loading data from the {}'.format(file_name))
    data_set = pd.read_csv(file_name)

    volcano_group = folium.FeatureGroup(name='Volcano Markers')

    for index, row in data_set.iterrows():
        volcano_group.add_child(folium.Marker(location=[row['LAT'], row['LON']],
                                              popup=create_popup(row), icon=create_icon(row)))
    return volcano_group


def create_population_layer():
    file_name = 'data/world.json'
    print('Loading data from the {}'.format(file_name))
    data_json = open(file_name, 'r', encoding='utf-8-sig').read()

    word_group = folium.FeatureGroup(name='Population Layer')
    word_group.add_child(folium.GeoJson(data=data_json, style_function=population_style_function))

    return word_group


def main():
    print('Creating new map instance')
    folium_map = folium.Map(location=[38.58, -99.09], zoom_start=6)

    print('Creating Volcano details markers')
    volcano_group = create_volcano_marker_layer()
    folium_map.add_child(volcano_group)

    print('Creating Population Layer')
    population_group = create_population_layer()
    folium_map.add_child(population_group)

    folium_map.add_child(folium.LayerControl())

    target_file = 'target/webmap.html'
    folium_map.save(target_file)
    print('WebMap is generated in target folder - {}'.format(target_file))


if __name__ == '__main__':
    main()