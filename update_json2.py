import json
import re

with open('templates/page.teamwear.json', 'r') as f:
    raw_content = f.read()

# Strip block comments
json_str = re.sub(r'/\*.*?\*/', '', raw_content, flags=re.DOTALL)

json_content = json.loads(json_str)

# Update tab_3 to use impregnation layout
json_content['sections']['main']['blocks']['tab_3']['settings']['tab_content_type'] = 'impregnation_service'
json_content['sections']['main']['blocks']['tab_3']['settings']['imp_title'] = "Full functionality. Full performance. Like new again - with our waterproofing service."
json_content['sections']['main']['blocks']['tab_3']['settings']['imp_text'] = "Regular care renews the functional properties of your ski clothing and extends its service life. The outer fabric of our clothing is impregnated when new so that water and dirt simply roll off. Frequent wear, dirt, and sweat impair the breathable and waterproof properties of functional clothing. Therefore, functional clothing should be washed and re-impregnated correctly and regularly. Your functional clothing is professionally washed and 100% PFAS-free impregnated by our partner MeyerundKuhl, making it weatherproof again."
json_content['sections']['main']['blocks']['tab_3']['settings']['imp_subtitle'] = "How the service works:"

# Add the 4 service steps
json_content['sections']['main']['blocks']['step_1'] = {
  "type": "service_step",
  "settings": {
    "icon_url": "https://cdn.shopify.com/s/files/1/0999/0701/0937/files/drop.svg?v=1782325516",
    "title": "Buy impregnation service",
    "text": "Click on the waterproofing service and select the items of clothing you want to have cleaned and waterproofed directly online from our partner MeyerundKuhl."
  }
}
json_content['sections']['main']['blocks']['step_2'] = {
  "type": "service_step",
  "settings": {
    "icon_url": "https://cdn.shopify.com/s/files/1/0999/0701/0937/files/box.svg",
    "title": "Shipping your products",
    "text": "Create the DHL shipping label for the impregnation service and stick the printed shipping label on the box containing your securely packed clothing for shipping."
  }
}
json_content['sections']['main']['blocks']['step_3'] = {
  "type": "service_step",
  "settings": {
    "icon_url": "https://cdn.shopify.com/s/files/1/0999/0701/0937/files/thumbs-up.svg",
    "title": "Your product will be impregnated",
    "text": "Your clothing will be professionally washed by our partner and sustainably impregnated without PFAS."
  }
}
json_content['sections']['main']['blocks']['step_4'] = {
  "type": "service_step",
  "settings": {
    "icon_url": "https://cdn.shopify.com/s/files/1/0999/0701/0937/files/truck.svg",
    "title": "Direct return shipping",
    "text": "Within 14 days, your cleaned and waterproofed clothing will be delivered back to your home in practical and uncomplicated manner."
  }
}

# Update block order to include the steps
json_content['sections']['main']['block_order'] = [
    "tab_1", "tab_2", "img_1", "color_image_xiVgCt", "tab_3", "step_1", "step_2", "step_3", "step_4", "tab_4"
]

with open('templates/page.teamwear.json', 'w') as f:
    f.write(json.dumps(json_content, indent=2))

