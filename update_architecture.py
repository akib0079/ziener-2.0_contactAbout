import json

# 1. Generate the completely new page-teamwear.liquid content
liquid_content = """<div class="tw-page">
  <!-- Banner -->
  {% assign desktop_img_url = section.settings.image_desktop_url | default: 'https://cdn.shopify.com/s/files/1/0999/0701/0937/files/placeholder-banner.png' %}
  {% assign mobile_img_url = section.settings.image_mobile_url | default: 'https://cdn.shopify.com/s/files/1/0999/0701/0937/files/placeholder-banner-mobile.png' %}

  <div class="tw-banner">
    <div class="tw-banner__image-wrapper">
      {% if section.settings.image_desktop != blank %}
        <img src="{{ section.settings.image_desktop | image_url: width: 2500 }}" alt="{{ section.settings.heading | escape }}" class="tw-banner__img tw-desktop-only" loading="eager">
      {% else %}
        <img src="{{ desktop_img_url }}" alt="{{ section.settings.heading | escape }}" class="tw-banner__img tw-desktop-only" loading="eager">
      {% endif %}
      
      {% if section.settings.image_mobile != blank %}
        <img src="{{ section.settings.image_mobile | image_url: width: 800 }}" alt="{{ section.settings.heading | escape }}" class="tw-banner__img tw-mobile-only" loading="eager">
      {% else %}
        <img src="{{ mobile_img_url }}" alt="{{ section.settings.heading | escape }}" class="tw-banner__img tw-mobile-only" loading="eager">
      {% endif %}
    </div>
    <div class="tw-banner__overlay"></div>
    {% if section.settings.heading != blank %}
      <div class="tw-banner__content tw-container">
        <h1 class="tw-banner__heading">{{ section.settings.heading }}</h1>
      </div>
    {% endif %}
  </div>

  <!-- Tabs Section -->
  <div class="tw-tabs-section">
    <div class="tw-container">
      
      <!-- Tab Headers -->
      <div class="tw-tabs-nav">
        {% if section.settings.tab_1_name != blank %}
          <button class="tw-tab-btn is-active" data-target="tab-1">{{ section.settings.tab_1_name }}</button>
        {% endif %}
        {% if section.settings.tab_2_name != blank %}
          <button class="tw-tab-btn" data-target="tab-2">{{ section.settings.tab_2_name }}</button>
        {% endif %}
        {% if section.settings.tab_3_name != blank %}
          <button class="tw-tab-btn" data-target="tab-3">{{ section.settings.tab_3_name }}</button>
        {% endif %}
        {% if section.settings.tab_4_name != blank %}
          <button class="tw-tab-btn" data-target="tab-4">{{ section.settings.tab_4_name }}</button>
        {% endif %}
      </div>

      <!-- Tab Content -->
      <div class="tw-tabs-content-area">
        
        <!-- Tab 1 -->
        <div class="tw-tab-content is-active" id="tab-1">
          {% assign has_tab_1 = false %}
          {% for block in section.blocks %}
            {% if block.type == 'tab_1_html' %}
              {% assign has_tab_1 = true %}
              <div {{ block.shopify_attributes }}>
                {{ block.settings.html }}
              </div>
            {% endif %}
          {% endfor %}
          {% if has_tab_1 == false %}
            <div style="padding: 40px; text-align: center; color: #666;">Please add a 'Tab 1 HTML' block.</div>
          {% endif %}
        </div>

        <!-- Tab 2 -->
        <div class="tw-tab-content" id="tab-2">
          {% if section.settings.tab_2_heading != blank %}
            <h2 class="tw-co-header">{{ section.settings.tab_2_heading }}</h2>
          {% endif %}
          
          <div class="tw-co-list">
            {% for block in section.blocks %}
              {% if block.type == 'tab_2_image' %}
                <div class="tw-co-item" {{ block.shopify_attributes }}>
                  {% if block.settings.title != blank %}
                    <h3 class="tw-co-title">{{ block.settings.title }}</h3>
                  {% endif %}
                  
                  {% if block.settings.link != blank %}<a href="{{ block.settings.link }}" target="_blank" class="tw-co-link">{% endif %}
                  
                  {% if block.settings.image != blank %}
                    <img src="{{ block.settings.image | image_url: width: 1400 }}" alt="{{ block.settings.title | escape }}" loading="lazy" class="tw-co-img">
                  {% elsif block.settings.default_img != blank %}
                    <img src="{{ block.settings.default_img }}" alt="{{ block.settings.title | escape }}" loading="lazy" class="tw-co-img">
                  {% endif %}

                  {% if block.settings.link != blank %}</a>{% endif %}
                </div>
              {% endif %}
            {% endfor %}
          </div>
        </div>

        <!-- Tab 3 -->
        <div class="tw-tab-content" id="tab-3">
          {% assign has_tab_3 = false %}
          {% for block in section.blocks %}
            {% if block.type == 'tab_3_html' %}
              {% assign has_tab_3 = true %}
              <div {{ block.shopify_attributes }}>
                {{ block.settings.html }}
              </div>
            {% endif %}
          {% endfor %}
          {% if has_tab_3 == false %}
            <div style="padding: 40px; text-align: center; color: #666;">Please add a 'Tab 3 HTML' block.</div>
          {% endif %}
        </div>

        <!-- Tab 4 -->
        <div class="tw-tab-content" id="tab-4">
          {% assign has_tab_4 = false %}
          {% for block in section.blocks %}
            {% if block.type == 'tab_4_html' %}
              {% assign has_tab_4 = true %}
              <div {{ block.shopify_attributes }}>
                {{ block.settings.html }}
              </div>
            {% endif %}
          {% endfor %}
          {% if has_tab_4 == false %}
            <div style="padding: 40px; text-align: center; color: #666;">Please add a 'Tab 4 HTML' block.</div>
          {% endif %}
        </div>

      </div>
    </div>
  </div>
</div>

<style>
  #shopify-section-{{ section.id }} .tw-banner {
    min-height: {{ section.settings.banner_height_desktop }}px;
  }
  @media screen and (max-width: 990px) {
    #shopify-section-{{ section.id }} .tw-banner {
      min-height: {{ section.settings.banner_height_mobile }}px;
    }
  }
</style>

<style>
/* Global */
.tw-page {
  width: 100%;
  overflow-x: hidden;
  color: #000;
  padding-bottom: 80px;
}
.tw-container {
  max-width: 1440px;
  margin: 0 auto;
  padding: 0 8px;
  width: 100%;
}
.tw-desktop-only { display: block !important; }
.tw-mobile-only { display: none !important; }

@media screen and (max-width: 767px) {
  .tw-container { padding: 0 20px; }
  .tw-desktop-only { display: none !important; }
  .tw-mobile-only { display: block !important; }
}

/* Banner */
.tw-banner {
  position: relative;
  width: 100%;
  display: flex;
  align-items: flex-end;
}
.tw-banner__image-wrapper {
  position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0;
}
.tw-banner__img {
  width: 100%; height: 100%; object-fit: cover;
}
.tw-banner__overlay {
  position: absolute; top: 0; left: 0; width: 100%; height: 100%;
  background: linear-gradient(180deg, rgba(0, 0, 0, 0.00) 0%, rgba(0, 0, 0, 0.35) 100%);
  z-index: 1;
}
.tw-banner__content {
  position: relative; z-index: 2;
  padding-bottom: 40px;
}
.tw-banner__heading {
  color: #FFF;
  font-family: "Ziener Helvetica", Arial, sans-serif;
  font-size: 80px;
  font-style: normal;
  font-weight: 700;
  line-height: 100px;
  margin: 0;
}

/* Tabs Section */
.tw-tabs-section {
  padding-top: 60px;
}
.tw-tabs-nav {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 40px;
}
.tw-tab-btn {
  display: flex;
  height: 50px;
  padding: 0 20px;
  justify-content: center;
  align-items: center;
  gap: 6px;
  flex: 1 0 0;
  
  background: rgba(249, 249, 249, 1);
  border: 1px solid transparent;
  cursor: pointer;
  transition: all 0.3s ease;
  
  color: #000;
  font-family: Arial, sans-serif;
  font-size: 14px;
  font-style: normal;
  font-weight: 400;
  line-height: 98%; /* 13.72px */
  letter-spacing: -0.28px;
  text-transform: capitalize;
}
.tw-tab-btn:hover {
  background: rgba(235, 235, 235, 1);
  border: 1px solid rgba(0, 0, 0, 1);
}
.tw-tab-btn.is-active {
  border: 1px solid rgba(0, 0, 0, 1);
}

.tw-tab-content {
  display: none;
  animation: fadeIn 0.4s ease forwards;
}
.tw-tab-content.is-active {
  display: block;
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(5px); }
  to { opacity: 1; transform: translateY(0); }
}

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
  text-align: center;
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

/* Mobile Breakpoints */
@media screen and (max-width: 990px) {
  .tw-banner__heading {
    font-size: 48px;
    line-height: 100%;
  }
  .tw-tabs-nav {
    flex-direction: column;
    gap: 10px;
  }
  .tw-tab-btn {
    width: 100%;
    flex: none;
  }
  .tw-co-header {
    font-size: 28px;
    line-height: 120%; /* 33.6px */
    margin-bottom: 40px;
  }
  .tw-co-list {
    gap: 60px;
  }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const tabBtns = document.querySelectorAll('.tw-tab-btn');
  const tabContents = document.querySelectorAll('.tw-tab-content');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      // Remove active from all
      tabBtns.forEach(b => b.classList.remove('is-active'));
      tabContents.forEach(c => c.classList.remove('is-active'));

      // Add active to clicked
      btn.classList.add('is-active');
      const targetId = btn.getAttribute('data-target');
      document.getElementById(targetId).classList.add('is-active');
    });
  });
});
</script>

{% schema %}
{
  "name": "Teamwear Page",
  "settings": [
    {
      "type": "text",
      "id": "heading",
      "label": "Banner Heading",
      "default": "Teamwear"
    },
    {
      "type": "image_picker",
      "id": "image_desktop",
      "label": "Banner Image (Desktop)"
    },
    {
      "type": "image_picker",
      "id": "image_mobile",
      "label": "Banner Image (Mobile)"
    },
    {
      "type": "text",
      "id": "image_desktop_url",
      "label": "Fallback Desktop Image URL"
    },
    {
      "type": "text",
      "id": "image_mobile_url",
      "label": "Fallback Mobile Image URL"
    },
    {
      "type": "header",
      "content": "Banner Dimensions"
    },
    {
      "type": "range",
      "id": "banner_height_desktop",
      "min": 200,
      "max": 800,
      "step": 10,
      "unit": "px",
      "label": "Desktop Banner Height",
      "default": 410
    },
    {
      "type": "range",
      "id": "banner_height_mobile",
      "min": 150,
      "max": 600,
      "step": 5,
      "unit": "px",
      "label": "Mobile Banner Height",
      "default": 290
    },
    {
      "type": "header",
      "content": "Tabs Navigation Settings"
    },
    {
      "type": "text",
      "id": "tab_1_name",
      "label": "Tab 1 Name",
      "default": "Catalog"
    },
    {
      "type": "text",
      "id": "tab_2_name",
      "label": "Tab 2 Name",
      "default": "Color Overviews"
    },
    {
      "type": "text",
      "id": "tab_3_name",
      "label": "Tab 3 Name",
      "default": "Impregnation Service"
    },
    {
      "type": "text",
      "id": "tab_4_name",
      "label": "Tab 4 Name",
      "default": "Repair Service"
    },
    {
      "type": "header",
      "content": "Tab 2 (Color Overviews) Content Settings"
    },
    {
      "type": "text",
      "id": "tab_2_heading",
      "label": "Tab 2 Header Text",
      "default": "Color overviews for the winter season 2026/27"
    }
  ],
  "blocks": [
    {
      "type": "tab_1_html",
      "name": "Tab 1 Content (HTML)",
      "limit": 1,
      "settings": [
        {
          "type": "html",
          "id": "html",
          "label": "HTML Embed",
          "info": "Paste the PDF flipbook iframe here."
        }
      ]
    },
    {
      "type": "tab_2_image",
      "name": "Tab 2 Image (Color)",
      "settings": [
        {
          "type": "text",
          "id": "title",
          "label": "Title"
        },
        {
          "type": "image_picker",
          "id": "image",
          "label": "Image"
        },
        {
          "type": "text",
          "id": "default_img",
          "label": "Fallback Image URL"
        },
        {
          "type": "url",
          "id": "link",
          "label": "Link"
        }
      ]
    },
    {
      "type": "tab_3_html",
      "name": "Tab 3 Content (HTML)",
      "limit": 1,
      "settings": [
        {
          "type": "html",
          "id": "html",
          "label": "HTML"
        }
      ]
    },
    {
      "type": "tab_4_html",
      "name": "Tab 4 Content (HTML)",
      "limit": 1,
      "settings": [
        {
          "type": "html",
          "id": "html",
          "label": "HTML"
        }
      ]
    }
  ],
  "presets": [
    {
      "name": "Teamwear Page"
    }
  ]
}
{% endschema %}
"""

with open('sections/page-teamwear.liquid', 'w') as f:
    f.write(liquid_content)

# 2. Generate the new templates/page.teamwear.json
json_content = {
  "sections": {
    "main": {
      "type": "page-teamwear",
      "blocks": {
        "catalog_embed": {
          "type": "tab_1_html",
          "settings": {
            "html": "<iframe src=\"https://www.pdf-flip.com/viewers/800765/1i91ub.html\" title=\"ZIENER_TW_W2627_A4_FlippingPage_DE (5)\" style=\"width:100%;height:80vh;min-height:400px;border:0;display:block;\" loading=\"lazy\" allowfullscreen></iframe>"
          }
        },
        "color_img_1": {
          "type": "tab_2_image",
          "settings": {
            "title": "Trivor / Tewes",
            "default_img": "https://cdn.shopify.com/s/files/1/0999/0701/0937/files/ZIENER_TW_W2627_Farbuebersicht_Kollektion_Trivor_Tewes_A4_Neu.jpg?v=1782321448",
            "link": "https://ziener.com/images/pdf/2025/ZIENER_TW_W2627_Farbuebersicht_Kollektion_Trivor_Tewes_A4.pdf"
          }
        }
      },
      "block_order": [
        "catalog_embed",
        "color_img_1"
      ],
      "settings": {
        "tab_1_name": "Catalog",
        "tab_2_name": "Color Overviews",
        "tab_3_name": "Impregnation Service",
        "tab_4_name": "Repair Service",
        "tab_2_heading": "Color overviews for the winter season 2026/27"
      }
    }
  },
  "order": ["main"]
}

with open('templates/page.teamwear.json', 'w') as f:
    json.dump(json_content, f, indent=2)

