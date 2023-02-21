import requests
from pprint import pprint as print

app_id = "63c1ac6c"
app_key = "046240bbd55d4bb49a920516598c5f59"
language = "en-gb"
# word_id = "apple"
# url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
# r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
# res=r.json()
# # print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
# # print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['definitions'])
# # # print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['shortDefinitions'][0])
# # print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]['shortDefinitions'][0])
# # print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['subsenses'][0]['shortDefinitions'][0])
# # print(res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile'])
# for i in range(len(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'])):
#     print(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][i]['definitions'][0])
# # print(len(res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']))

def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()

    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    res = r.json()
    if 'error' in res.keys():
        return False
    output= {}
    senses = res['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    dictions = []
    for sense in senses:
        dictions.append(f">>>{sense['definitions'][0]}")
    output['definitions'] = "\n".join(dictions)
    if res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio']=res['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    return output
#
if __name__ == '__main__':
    from pprint import pprint as print

    print(getDefinitions('apple')['definitions'])