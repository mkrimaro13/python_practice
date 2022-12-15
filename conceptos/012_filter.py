print('********************LISTAS********************')
numbers_list = [1, 2, 3, 4, 5, 6]
filtered_list = list(filter(lambda x : x % 2 ==  0, numbers_list))
filtered_list_2 = list(filter(lambda x : x % 2 !=  0, numbers_list))
filtered_list_3 = list(map(lambda x : x % 2 !=  0, numbers_list))
print(f'Lista incial: {numbers_list}      \nLista filtrada: {filtered_list}      \nLista filtrada: {filtered_list_2}      \nLista filtrada: {filtered_list_3}')


print('********************DICCIONARIOS********************')
matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
]

print(f'Información de partidos: \n{matches}')
filtered_matches = list(filter(lambda item: item['home_team_result'] == 'Win', matches ))
print(f'Información filtrada de partidos: \n{filtered_matches}')



