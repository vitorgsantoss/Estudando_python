import json
import os

string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''
# filme = json.loads(string_json)

os.system('cls')

file_name = 'aula290.json'
caminho = os.path.join(os.path.dirname(__file__),file_name)

with open(caminho, 'w', encoding='utf8') as arquivo:
    # json.dump(filme, arquivo, ensure_ascii=False, indent=2)
    arquivo.write(string_json)

with open (caminho, 'r') as arquivo:
    filme_json= json.load(arquivo)

print(filme_json)