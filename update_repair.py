import json
import re

with open('sections/page-teamwear.liquid', 'r') as f:
    content = f.read()

# 1. Update the HTML
old_html = """              {% else %}
                {% if block.settings.custom_html != blank %}
                  {{ block.settings.custom_html }}
                {% endif %}
              {% endif %}"""

new_html = """              {% elsif block.settings.tab_content_type == 'repair_service' %}
                <div class="tw-rep-container">
                  {% if block.settings.rep_text != blank %}
                    <div class="tw-rep-text">{{ block.settings.rep_text | newline_to_br }}</div>
                  {% endif %}
                </div>
              
              {% else %}
                {% if block.settings.custom_html != blank %}
                  {{ block.settings.custom_html }}
                {% endif %}
              {% endif %}"""

content = content.replace(old_html, new_html)

# 2. Add CSS
css_to_add = """
/* Repair Service */
.tw-rep-container {
  max-width: 100%;
}
.tw-rep-text {
  color: #000;
  font-family: Arial, sans-serif;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 150%; /* 21px */
  margin: 0;
}
"""

content = content.replace("/* Mobile Breakpoints */", css_to_add + "\n/* Mobile Breakpoints */")

# 3. Update JSON schema using regex
schema_str = re.search(r'{% schema %}(.*?){% endschema %}', content, re.DOTALL).group(1)
schema_obj = json.loads(schema_str)

# Find Tab Block
tab_block = next(b for b in schema_obj['blocks'] if b['type'] == 'tab')
# Add repair option to select
content_type_setting = next(s for s in tab_block['settings'] if s['id'] == 'tab_content_type')
content_type_setting['options'].append({"value": "repair_service", "label": "Repair Service Layout"})

# Add new settings to tab block
tab_block['settings'].extend([
    {
      "type": "textarea",
      "id": "rep_text",
      "label": "Repair Text",
      "info": "Only used if 'Repair Service Layout' is selected above."
    }
])

new_schema_str = json.dumps(schema_obj, indent=2)
content = re.sub(r'{% schema %}.*?{% endschema %}', f'{{% schema %}}\n{new_schema_str}\n{{% endschema %}}', content, flags=re.DOTALL)

with open('sections/page-teamwear.liquid', 'w') as f:
    f.write(content)

