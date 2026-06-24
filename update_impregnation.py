import json
import re

with open('sections/page-teamwear.liquid', 'r') as f:
    content = f.read()

# 1. Update the HTML
old_html = """              {% if block.settings.tab_content_type == 'color_overviews' %}
                {% if block.settings.co_header != blank %}
                  <h2 class="tw-co-header">{{ block.settings.co_header }}</h2>
                {% endif %}
                
                <div class="tw-co-list">
                  {% for img_block in section.blocks %}
                    {% if img_block.type == 'color_image' %}
                      <div class="tw-co-item" {{ img_block.shopify_attributes }}>
                        {% if img_block.settings.title != blank %}
                          <h3 class="tw-co-title">{{ img_block.settings.title }}</h3>
                        {% endif %}
                        
                        {% if img_block.settings.link != blank %}<a href="{{ img_block.settings.link }}" target="_blank" class="tw-co-link">{% endif %}
                        
                        {% if img_block.settings.image != blank %}
                          <img src="{{ img_block.settings.image | image_url: width: 1400 }}" alt="{{ img_block.settings.title | escape }}" loading="lazy" class="tw-co-img">
                        {% elsif img_block.settings.default_img != blank %}
                          <img src="{{ img_block.settings.default_img }}" alt="{{ img_block.settings.title | escape }}" loading="lazy" class="tw-co-img">
                        {% endif %}

                        {% if img_block.settings.link != blank %}</a>{% endif %}
                      </div>
                    {% endif %}
                  {% endfor %}
                </div>
              
              {% else %}
                {% if block.settings.custom_html != blank %}
                  {{ block.settings.custom_html }}
                {% endif %}
              {% endif %}"""

new_html = """              {% if block.settings.tab_content_type == 'color_overviews' %}
                {% if block.settings.co_header != blank %}
                  <h2 class="tw-co-header">{{ block.settings.co_header }}</h2>
                {% endif %}
                
                <div class="tw-co-list">
                  {% for img_block in section.blocks %}
                    {% if img_block.type == 'color_image' %}
                      <div class="tw-co-item" {{ img_block.shopify_attributes }}>
                        {% if img_block.settings.title != blank %}
                          <h3 class="tw-co-title">{{ img_block.settings.title }}</h3>
                        {% endif %}
                        
                        {% if img_block.settings.link != blank %}<a href="{{ img_block.settings.link }}" target="_blank" class="tw-co-link">{% endif %}
                        
                        {% if img_block.settings.image != blank %}
                          <img src="{{ img_block.settings.image | image_url: width: 1400 }}" alt="{{ img_block.settings.title | escape }}" loading="lazy" class="tw-co-img">
                        {% elsif img_block.settings.default_img != blank %}
                          <img src="{{ img_block.settings.default_img }}" alt="{{ img_block.settings.title | escape }}" loading="lazy" class="tw-co-img">
                        {% endif %}

                        {% if img_block.settings.link != blank %}</a>{% endif %}
                      </div>
                    {% endif %}
                  {% endfor %}
                </div>
                
              {% elsif block.settings.tab_content_type == 'impregnation_service' %}
                <div class="tw-imp-container">
                  {% if block.settings.imp_title != blank %}
                    <h2 class="tw-imp-title">{{ block.settings.imp_title }}</h2>
                  {% endif %}
                  {% if block.settings.imp_text != blank %}
                    <div class="tw-imp-text">{{ block.settings.imp_text }}</div>
                  {% endif %}
                  {% if block.settings.imp_subtitle != blank %}
                    <h3 class="tw-imp-subtitle">{{ block.settings.imp_subtitle }}</h3>
                  {% endif %}
                  
                  <div class="tw-imp-grid">
                    {% for step_block in section.blocks %}
                      {% if step_block.type == 'service_step' %}
                        <div class="tw-imp-step" {{ step_block.shopify_attributes }}>
                          <div class="tw-imp-step-icon">
                            {% if step_block.settings.icon_img != blank %}
                              <img src="{{ step_block.settings.icon_img | image_url: width: 100 }}" alt="{{ step_block.settings.title | escape }}" loading="lazy">
                            {% elsif step_block.settings.icon_url != blank %}
                              <img src="{{ step_block.settings.icon_url }}" alt="{{ step_block.settings.title | escape }}" loading="lazy">
                            {% endif %}
                          </div>
                          <div class="tw-imp-step-content">
                            <h4 class="tw-imp-step-title">{{ step_block.settings.title }}</h4>
                            <div class="tw-imp-step-text">{{ step_block.settings.text }}</div>
                          </div>
                        </div>
                      {% endif %}
                    {% endfor %}
                  </div>
                </div>
              
              {% else %}
                {% if block.settings.custom_html != blank %}
                  {{ block.settings.custom_html }}
                {% endif %}
              {% endif %}"""

content = content.replace(old_html, new_html)

# 2. Add CSS
css_to_add = """
/* Impregnation Service */
.tw-imp-container {
  max-width: 100%;
}
.tw-imp-title {
  color: #000;
  font-family: "Ziener Helvetica", Arial, sans-serif;
  font-size: 32px;
  font-style: normal;
  font-weight: 400;
  line-height: 120%; /* 38.4px */
  margin: 0 0 24px 0;
  max-width: 800px;
}
.tw-imp-text {
  color: #000;
  font-family: Arial, sans-serif;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 150%; /* 21px */
  margin: 0 0 40px 0;
}
.tw-imp-subtitle {
  color: #000;
  font-family: "Ziener Helvetica", Arial, sans-serif;
  font-size: 22px;
  font-style: normal;
  font-weight: 700;
  line-height: 150%; /* 33px */
  margin: 0 0 24px 0;
}
.tw-imp-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 10px;
}
.tw-imp-step {
  display: flex;
  height: 332px;
  padding: 30px;
  flex-direction: column;
  justify-content: space-between;
  align-items: flex-start;
  flex: 1 0 0;
  border: 1px solid rgba(0, 0, 0, 0.10);
  background: #FFF;
}
.tw-imp-step-icon {
  width: 40px;
  height: 40px;
}
.tw-imp-step-icon img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}
.tw-imp-step-content {
  margin-top: auto;
}
.tw-imp-step-title {
  color: #000;
  font-family: "Ziener Helvetica", Arial, sans-serif;
  font-size: 20px;
  font-style: normal;
  font-weight: 700;
  line-height: 120%; /* 24px */
  margin: 0 0 12px 0;
}
.tw-imp-step-text {
  color: #202020;
  font-family: Arial, sans-serif;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 150%; /* 21px */
  margin: 0;
}

@media screen and (max-width: 990px) {
  .tw-imp-title {
    font-size: 28px;
    line-height: 120%; /* 33.6px */
  }
  .tw-imp-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  .tw-imp-step {
    height: auto;
    min-height: 250px;
  }
}
"""

content = content.replace("/* Mobile Breakpoints */", css_to_add + "\n/* Mobile Breakpoints */")

# 3. Update JSON schema using regex
# Find the tab_content_type options
schema_str = re.search(r'{% schema %}(.*?){% endschema %}', content, re.DOTALL).group(1)
schema_obj = json.loads(schema_str)

# Find Tab Block
tab_block = next(b for b in schema_obj['blocks'] if b['type'] == 'tab')
# Add impregnation option to select
content_type_setting = next(s for s in tab_block['settings'] if s['id'] == 'tab_content_type')
content_type_setting['options'].append({"value": "impregnation_service", "label": "Impregnation Service Layout"})

# Add new settings to tab block
tab_block['settings'].extend([
    {
      "type": "text",
      "id": "imp_title",
      "label": "Impregnation Title",
      "default": "Full functionality. Full performance. Like new again - with our waterproofing service."
    },
    {
      "type": "textarea",
      "id": "imp_text",
      "label": "Impregnation Text"
    },
    {
      "type": "text",
      "id": "imp_subtitle",
      "label": "Impregnation Subtitle",
      "default": "How the service works:"
    }
])

# Add service_step block type
schema_obj['blocks'].append({
  "type": "service_step",
  "name": "Service Step (Icon)",
  "settings": [
    {
      "type": "image_picker",
      "id": "icon_img",
      "label": "Icon Image"
    },
    {
      "type": "text",
      "id": "icon_url",
      "label": "Icon Fallback URL (SVG)"
    },
    {
      "type": "text",
      "id": "title",
      "label": "Title",
      "default": "Step Title"
    },
    {
      "type": "textarea",
      "id": "text",
      "label": "Text",
      "default": "Description of the service step goes here."
    }
  ]
})

new_schema_str = json.dumps(schema_obj, indent=2)
content = re.sub(r'{% schema %}.*?{% endschema %}', f'{{% schema %}}\n{new_schema_str}\n{{% endschema %}}', content, flags=re.DOTALL)

with open('sections/page-teamwear.liquid', 'w') as f:
    f.write(content)

