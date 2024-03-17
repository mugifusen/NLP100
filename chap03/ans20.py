import json



import gzip


with open('jawiki-country.json', mode='r') as f:
    jsons = []
    # 元データがJSON Lines≠JSONのため、１行ずつ読み込み
    lines = f.readlines() 
    for line in lines:
        jsons.append(json.loads(line))
    # イギリスを抽出
    eng = list(filter(lambda e: e['title'] == 'イギリス', jsons))
    eng_data = eng[0]
    print(eng[0]['text'])