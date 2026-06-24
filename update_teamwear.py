import json

with open('sections/page-teamwear.liquid', 'r') as f:
    content = f.read()

# 1. Replace the HTML loop content
old_html = """            {% if block.settings.custom_html != blank %}
              {{ block.settings.custom_html }}
            {% else %}
              <div style="padding: 40px; text-align: center; color: #666;">Content for {{ block.settings.title }} will go here.</div>
            {% endif %}"""

new_html = """            {% if block.settings.tab_content_type == 'color_overviews' %}
              {% if block.settings.co_header != blank %}
                <h2 class="tw-co-header">{{ block.settings.co_header }}</h2>
              {% endif %}
              
              <div class="tw-co-list">
                {% for i in (1..10) %}
                  {% capture title_key %}co_title_{{ i }}{% endcapture %}
                  {% capture image_key %}co_image_{{ i }}{% endcapture %}
                  {% capture default_img_key %}co_default_img_{{ i }}{% endcapture %}
                  {% capture link_key %}co_link_{{ i }}{% endcapture %}

                  {% assign img_title = block.settings[title_key] %}
                  {% assign img_obj = block.settings[image_key] %}
                  {% assign default_img = block.settings[default_img_key] %}
                  {% assign link_url = block.settings[link_key] %}

                  {% if img_title != blank or img_obj != blank or default_img != blank %}
                    <div class="tw-co-item">
                      {% if img_title != blank %}
                        <h3 class="tw-co-title">{{ img_title }}</h3>
                      {% endif %}
                      
                      {% if link_url != blank %}<a href="{{ link_url }}" target="_blank" class="tw-co-link">{% endif %}
                      
                      {% if img_obj != blank %}
                        <img src="{{ img_obj | image_url: width: 1400 }}" alt="{{ img_title | escape }}" loading="lazy" class="tw-co-img">
                      {% elsif default_img != blank %}
                        <img src="{{ default_img }}" alt="{{ img_title | escape }}" loading="lazy" class="tw-co-img">
                      {% endif %}

                      {% if link_url != blank %}</a>{% endif %}
                    </div>
                  {% endif %}
                {% endfor %}
              </div>

            {% else %}
              {% if block.settings.custom_html != blank %}
                {{ block.settings.custom_html }}
              {% else %}
                <div style="padding: 40px; text-align: center; color: #666;">Content for {{ block.settings.title }} will go here.</div>
              {% endif %}
            {% endif %}"""

content = content.replace(old_html, new_html)

# 2. Add CSS
css_to_add = """
/* Color Overviews */
.tw-co-header {
  color: #000;
  font-family: "Ziener Helvetica", Arial, sans-serif;
  font-size: 32px;
  font-style: normal;
  font-weight: 400;
  line-height: 48px; /* 150% */
  margin: 0 0 60px 0;
}
.tw-co-list {
  display: flex;
  flex-direction: column;
  gap: 80px;
}
.tw-co-item {
  width: 100%;
}
.tw-co-title {
  color: #000;
  text-align: left;
  font-family: "Ziener Helvetica", Arial, sans-serif;
  font-size: 22px;
  font-style: normal;
  font-weight: 700;
  line-height: 150%; /* 33px */
  margin: 0 0 30px 0;
}
.tw-co-link {
  display: block;
  text-decoration: none;
}
.tw-co-img {
  width: 100%;
  height: auto;
  display: block;
}

@media screen and (max-width: 990px) {
  .tw-co-header {
    font-size: 28px;
    line-height: 120%; /* 33.6px */
    margin-bottom: 40px;
  }
  .tw-co-list {
    gap: 60px;
  }
}
"""

content = content.replace("/* Mobile Breakpoints */", css_to_add + "\n/* Mobile Breakpoints */")

# 3. Inject schema
import re
# We need to add the new settings to the block settings array
# First, let's build the settings list to inject
new_settings = [
    {
        "type": "select",
        "id": "tab_content_type",
        "label": "Tab Content Type",
        "options": [
            {"value": "custom_html", "label": "Custom HTML / Embed"},
            {"value": "color_overviews", "label": "Color Overviews (Images)"}
        ],
        "default": "custom_html"
    },
    {
        "type": "text",
        "id": "co_header",
        "label": "Color Overviews Header",
        "default": "Color overviews for the winter season 2026/27"
    }
]

for i in range(1, 11):
    new_settings.extend([
        {
            "type": "header",
            "content": f"Image Item {i}"
        },
        {
            "type": "text",
            "id": f"co_title_{i}",
            "label": f"Title {i}"
        },
        {
            "type": "image_picker",
            "id": f"co_image_{i}",
            "label": f"Image {i}"
        },
        {
            "type": "text",
            "id": f"co_default_img_{i}",
            "label": f"Fallback Image URL {i}"
        },
        {
            "type": "url",
            "id": f"co_link_{i}",
            "label": f"Link {i}"
        }
    ])

# Find the start of the block settings
# We'll isolate the schema block, parse it as JSON, update it, and write it back
schema_str = re.search(r'{% schema %}(.*?){% endschema %}', content, re.DOTALL).group(1)
schema_obj = json.loads(schema_str)

# Update the block schema
block_settings = schema_obj['blocks'][0]['settings']
schema_obj['blocks'][0]['settings'] = block_settings + new_settings

# Re-insert the schema
new_schema_str = json.dumps(schema_obj, indent=2)
content = re.sub(r'{% schema %}.*?{% endschema %}', f'{{% schema %}}\n{new_schema_str}\n{{% endschema %}}', content, flags=re.DOTALL)

with open('sections/page-teamwear.liquid', 'w') as f:
    f.write(content)

