import json



import gzip


with open('jawiki-country.json', mode='r') as f:
    jsons = []
    # ���f�[�^��JSON Lines��JSON�̂��߁A�P�s���ǂݍ���
    lines = f.readlines() 
    for line in lines:
        jsons.append(json.loads(line))
    # �C�M���X�𒊏o
    eng = list(filter(lambda e: e['title'] == '�C�M���X', jsons))
    eng_data = eng[0]
    print(eng[0]['text'])