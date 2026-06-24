import json
import re

with open('templates/page.teamwear.json', 'r') as f:
    raw_content = f.read()

# Strip block comments
json_str = re.sub(r'/\*.*?\*/', '', raw_content, flags=re.DOTALL)
json_content = json.loads(json_str)

# Update tab_4 to use repair layout
json_content['sections']['main']['blocks']['tab_4']['settings']['tab_content_type'] = 'repair_service'
json_content['sections']['main']['blocks']['tab_4']['settings']['rep_text'] = "We want you to enjoy your favorite items for a long time. That's why we offer the TEAMWEAR REPAIR SERVICE.\n\nIf the product should break without your intervention, we will repair it for you free of charge.\nIf it is your own fault, we can also repair it for you, but at your expense.\n\nIt is very important to us that you have something from our products for a long time."

with open('templates/page.teamwear.json', 'w') as f:
    f.write(json.dumps(json_content, indent=2))

