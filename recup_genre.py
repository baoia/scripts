
import wptools
import json

def recup_genre(word):
  try:
    wikiID = wptools.page(wikibase=word, lang="fr")
    wikiID.WIKIPROPS['P21'] = 'gender'
    wikiID.get_wikidata()
    genre=wikiID.wikidata['gender']
  except KeyError as err:
    genre="None"
  print(genre)


recup_genre(word="Q7197")