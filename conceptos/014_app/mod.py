def get_population():
    key = ['col', 'bol']
    value = ['300', '400']
    return key, value

def population_by_country(data, country):
    result = list(filter(lambda item: item['country'] == country, data))
    return result