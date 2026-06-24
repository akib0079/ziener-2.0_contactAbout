import json

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
        {% assign tab_count = 0 %}
        {% for block in section.blocks %}
          {% if block.type == 'tab' %}
            {% assign tab_count = tab_count | plus: 1 %}
            <button class="tw-tab-btn {% if tab_count == 1 %}is-active{% endif %}" data-target="tab-{{ block.id }}" {{ block.shopify_attributes }}>
              {{ block.settings.title }}
            </button>
          {% endif %}
        {% endfor %}
      </div>

      <!-- Tab Content Area -->
      <div class="tw-tabs-content-area">
        {% assign tab_count = 0 %}
        {% for block in section.blocks %}
          {% if block.type == 'tab' %}
            {% assign tab_count = tab_count | plus: 1 %}
            
            <div class="tw-tab-content {% if tab_count == 1 %}is-active{% endif %}" id="tab-{{ block.id }}">
              
              {% if block.settings.tab_content_type == 'color_overviews' %}
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
              {% endif %}
              
            </div>
          {% endif %}
        {% endfor %}
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
.tw-page { width: 100%; overflow-x: hidden; color: #000; padding-bottom: 80px; }
.tw-container { max-width: 1440px; margin: 0 auto; padding: 0 8px; width: 100%; }
.tw-desktop-only { display: block !important; }
.tw-mobile-only { display: none !important; }

@media screen and (max-width: 767px) {
  .tw-container { padding: 0 20px; }
  .tw-desktop-only { display: none !important; }
  .tw-mobile-only { display: block !important; }
}

/* Banner */
.tw-banner { position: relative; width: 100%; display: flex; align-items: flex-end; }
.tw-banner__image-wrapper { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; }
.tw-banner__img { width: 100%; height: 100%; object-fit: cover; }
.tw-banner__overlay { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: linear-gradient(180deg, rgba(0, 0, 0, 0.00) 0%, rgba(0, 0, 0, 0.35) 100%); z-index: 1; }
.tw-banner__content { position: relative; z-index: 2; padding-bottom: 40px; }
.tw-banner__heading { color: #FFF; font-family: "Ziener Helvetica", Arial, sans-serif; font-size: 80px; font-style: normal; font-weight: 700; line-height: 100px; margin: 0; }

/* Tabs Section */
.tw-tabs-section { padding-top: 60px; }
.tw-tabs-nav { display: flex; align-items: center; gap: 10px; margin-bottom: 40px; }
.tw-tab-btn { display: flex; height: 50px; padding: 0 20px; justify-content: center; align-items: center; gap: 6px; flex: 1 0 0; background: rgba(249, 249, 249, 1); border: 1px solid transparent; cursor: pointer; transition: all 0.3s ease; color: #000; font-family: Arial, sans-serif; font-size: 14px; font-style: normal; font-weight: 400; line-height: 98%; letter-spacing: -0.28px; text-transform: capitalize; }
.tw-tab-btn:hover { background: rgba(235, 235, 235, 1); border: 1px solid rgba(0, 0, 0, 1); }
.tw-tab-btn.is-active { border: 1px solid rgba(0, 0, 0, 1); }

.tw-tab-content { display: none; animation: fadeIn 0.4s ease forwards; }
.tw-tab-content.is-active { display: block; }

@keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }

/* Color Overviews */
.tw-co-header { color: #000; font-family: "Ziener Helvetica", Arial, sans-serif; font-size: 32px; font-style: normal; font-weight: 400; line-height: 48px; margin: 0 0 60px 0; }
.tw-co-list { display: flex; flex-direction: column; gap: 80px; }
.tw-co-item { width: 100%; }
.tw-co-title { color: #000; text-align: center; font-family: "Ziener Helvetica", Arial, sans-serif; font-size: 22px; font-style: normal; font-weight: 700; line-height: 150%; margin: 0 0 30px 0; }
.tw-co-link { display: block; text-decoration: none; }
.tw-co-img { width: 100%; height: auto; display: block; }

/* Mobile Breakpoints */
@media screen and (max-width: 990px) {
  .tw-banner__heading { font-size: 48px; line-height: 100%; }
  .tw-tabs-nav { flex-direction: column; gap: 10px; }
  .tw-tab-btn { width: 100%; flex: none; }
  .tw-co-header { font-size: 28px; line-height: 120%; margin-bottom: 40px; }
  .tw-co-list { gap: 60px; }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const tabBtns = document.querySelectorAll('.tw-tab-btn');
  const tabContents = document.querySelectorAll('.tw-tab-content');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('is-active'));
      tabContents.forEach(c => c.classList.remove('is-active'));
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
    }
  ],
  "blocks": [
    {
      "type": "tab",
      "name": "Tab Block",
      "limit": 4,
      "settings": [
        {
          "type": "text",
          "id": "title",
          "label": "Tab Name",
          "default": "Tab Name"
        },
        {
          "type": "select",
          "id": "tab_content_type",
          "label": "Tab Content Type",
          "options": [
            { "value": "custom_html", "label": "HTML Embed (PDF, etc)" },
            { "value": "color_overviews", "label": "Color Overviews Layout" }
          ],
          "default": "custom_html"
        },
        {
          "type": "html",
          "id": "custom_html",
          "label": "HTML Embed Content",
          "info": "Only used if 'HTML Embed' is selected above."
        },
        {
          "type": "text",
          "id": "co_header",
          "label": "Color Overviews Header",
          "default": "Color overviews for the winter season 2026/27",
          "info": "Only used if 'Color Overviews Layout' is selected above."
        }
      ]
    },
    {
      "type": "color_image",
      "name": "Color Overview Image",
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
