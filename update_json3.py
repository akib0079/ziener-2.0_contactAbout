import json

with open('templates/page.teamwear.json', 'r') as f:
    json_content = json.load(f)

json_content['sections']['main']['blocks']['tab_3']['settings']['imp_text'] = "Regular care renews the functional properties of your ski clothing and extends its service life.\n\nThe outer fabric of our clothing is impregnated when new so that water and dirt simply roll off. Frequent wear, dirt, and sweat impair the breathable and waterproof properties of functional clothing. Therefore, functional clothing should be washed and re-impregnated correctly and regularly. Your functional clothing is professionally washed and 100% PFAS-free impregnated by our partner MeyerundKuhl, making it weatherproof again."

with open('templates/page.teamwear.json', 'w') as f:
    f.write(json.dumps(json_content, indent=2))

