import requests
import pandas as pd
from bs4 import BeautifulSoup

base_url = 'http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/'
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'


def get_content(url):
    print('Loading content from - {}'.format(url))
    response = requests.get(url, headers={'User-agent': user_agent})
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    return soup


def extract_property_details(property_tag):
    result = {}
    wrapper_tag = property_tag.find('div', {'class': 'propertyCard'})
    result['price'] = wrapper_tag.find('h4').text.strip()

    details_tag = wrapper_tag.find('div', {'class': 'CardDetails'})
    result['address'] = ', '.join([span.text
                                  for span in details_tag.find('div', {'class': 'primaryDetails'}).find_all('span')])

    secondary_details_tags = details_tag.find('div', {'class': 'secondaryDetails'}).find_all('div')
    bed_tag = secondary_details_tags[0].find('span')
    bath_tag = secondary_details_tags[1].find('span')

    if bed_tag:
        result['beds'] = bed_tag.find('b').text

    if bath_tag:
        result['full_baths'] = bath_tag.find('b').text

    return result


def extract_description(description):
    if description:
        description_tag = description.find('div', {'class': 'propertyDescCollapse'})
        return {'description': description_tag.text}
    return {'description': ''}


def extract_features(features):
    result = {}
    for feature in features:
        for feature_group in feature.find_all('div'):
            for feature_tag in feature_group.find_all('div'):
                features = feature_tag.find_all('span')
                if features:
                    result[features[0].text.replace(':', '').strip()] \
                        = ''.join([feature.text for feature in features[1:]])

    return result


def export(data):
    data_set = pd.DataFrame(data)
    data_set.to_csv('property_data.csv')


def scrap():
    data = []

    for page in ['t=0&s=0.html', 't=0&s=10.html', 't=0&s=20.html']:
        soup = get_content(base_url + page)
        for property_row_tag in soup.find_all('div', {'class': 'propertyRow'}):
            property_info = {}
            property_tag = property_row_tag.find('div', {'class': 'propertyCard'})
            property_details = extract_property_details(property_tag)
            property_info.update(property_details)

            property_detail_tag = property_row_tag.find('div', {'class': 'propertyDetails'})

            description_tags = property_detail_tag.find('div', {'class': 'propertyDescription'})
            descriptions = extract_description(description_tags)
            property_info.update(descriptions)

            features_tags = property_detail_tag.find_all('div', {'class': 'propertyFeatures'})
            features = extract_features(features_tags)
            property_info.update(features)

            data.append(property_info)
            print(property_info)

    return data


def main():
    data = scrap()
    export(data)


if __name__ == '__main__':
    main()
