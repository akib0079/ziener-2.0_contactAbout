import { Component } from '@theme/component';
import { debounce, onDocumentLoaded } from '@theme/utilities';
import {
  ThemeEvents,
  CartUpdateEvent,
  CartAddEvent,
} from '@theme/events';

class ProductMainAlt extends Component {
    #product = null;
    connectedCallback() {
        super.connectedCallback();
        this.init();
    }
    init(){
        this.#product = JSON.parse(this.querySelector('script[data-product-json]').innerHTML);
        if(this.classList.contains('variant-based-gallery')){
            this.separateGallery();
        }
        this.initQuantityInput();
        this.initVariantPicker();
        this.initAjaxForm();
        this.handleVariantChange();
        onDocumentLoaded(() => {
            this.initGallery(); 
            // this.initSwatches(); 
            // this.initAjaxCart(); 
        });
        // if(this.classList.contains('globo-template-product')){
        //     this.fetchReviews();
        // }
    }
    handleVariantChange(){
        this.addEventListener('variant_changed', (e) => {
            const variant = e.detail.variant;
            this.updateVariantURL(variant);
            this.updateSelectedOptions(variant);
            this.updateVariantVisibilityArea(variant);
            this.updateAvailableState(e.detail.product);
            this.updateButButtons(variant);
            if(this.classList.contains('variant-based-gallery')){
            this.updateActiveGallery(variant);
            }
        });
    }
    initAjaxForm(){
          this.querySelectorAll('.product-form').forEach((form) => {
            form.addEventListener('submit', (e) => {
            e.preventDefault();
            const btn = form.querySelector('.product-alt__add-cart');
            const variantId = form.querySelector('[data-input-curr-variant-id]').value;
            btn.classList.add('btn--in-progress');
            fetch(Theme.routes.cart_add_url, {
                method: 'POST',
                body: JSON.stringify({
                items: [
                    {
                    id: variantId,
                    quantity: form.querySelector('.product-alt__buy-qty-input')?.value || 1,
                    },
                ],
                }),
                headers: {
                'Content-Type': 'application/json',
                },
            })
                .then((response) => {
                btn.classList.remove('btn--in-progress');
                return response.json();
                })
                .then((response) => {
                if (!response.status || response.status === 200) {
                    document.dispatchEvent(new CustomEvent('Theme:cartchanged', { bubbles: true, cancelable: false }));
                    document.dispatchEvent(
                    new CustomEvent('cart:update', {
                        detail: {
                        data: {
                            source: 'quick-add',
                            variantId: variantId,
                        },
                        },
                    })
                    );
                    btn.classList.add('check');
                    setTimeout(() => {
                    btn.classList.remove('check');
                    }, 1500);
                } else if (response.description) {
                    Theme.showQuickPopup(response.description, btn);
                }
                });
            });
        });
    }
    initVariantPicker(){
        this.querySelectorAll('.product-alt__option-selector').forEach((selector) => {
            selector.style.setProperty('--height', selector.scrollHeight + 'px');
        });
    }
    initQuantityInput(){
          this.querySelectorAll('.product-alt__buy-quantity').forEach((qty) => {
            const qtyInput = qty.querySelector('.product-alt__buy-qty-input');
            const minusBtn = qty.querySelector('[data-qty-minus]');
            const plusBtn = qty.querySelector('[data-qty-plus]');
            if (minusBtn && qtyInput) {
            minusBtn.addEventListener('click', function () {
                const val = parseInt(qtyInput.value) || 1;
                if (val > 1) qtyInput.value = val - 1;
            });
            }

            if (plusBtn && qtyInput) {
            plusBtn.addEventListener('click', function () {
                const val = parseInt(qtyInput.value) || 1;
                qtyInput.value = val + 1;
            });
            }
        });
    }
    initGallery(){
        const thumbsSwiper = new Swiper(this.querySelector('.product-alt__thumb'), {
            slidesPerView: 'auto',
            freeMode: {
                enabled: true,
                sticky: true,
                momentumRatio: 0.8,
            },
            breakpoints: {
                750: {
                direction: 'vertical',
                },
            },
        });
        const gallerySwiper = new Swiper(this.querySelector('.product-alt__gallery'), {
            slidesPerView: 1,
            effect: 'fade',
            thumbs: {
                swiper: thumbsSwiper,
            },
            navigation: {
                nextEl: this.querySelector('.slider_nav.nav-next'),
                prevEl: this.querySelector('.slider_nav.nav-prev'),
            },
        });
    }
    separateGallery() {
        const productData = this.#product;
        let optionNameMediaMap = {}, groupingOptionIndex = 0;
        productData.media.forEach((media) => {
            productData.variants.forEach((variant) => {
                if (variant.featured_media && variant.featured_media.id == media.id) {
                    if (!optionNameMediaMap[variant.options[groupingOptionIndex]]) {
                        optionNameMediaMap[variant.options[groupingOptionIndex]] = media.id;
                    }
                }
            });
        });
        console.log(optionNameMediaMap)
        let currentMediaOptionName = '';
        let mainSwiperCont = this.querySelector(".product-alt__gallery-wrap");
        this.querySelectorAll('.product-alt__gallery .swiper-slide').forEach((item, index) => {
            for (let optionName in optionNameMediaMap) {
                if (item.dataset.mediaId == optionNameMediaMap[optionName]) {
                    currentMediaOptionName = optionName;
                }
            }
            let currMainSwiperCont = this.querySelector(`.product-alt__gallery-wrap[data-variant-image-group="${currentMediaOptionName}"]`);
            if(currMainSwiperCont == undefined){
                currMainSwiperCont = mainSwiperCont.cloneNode(true);
                currMainSwiperCont.setAttribute('data-variant-image-group', currentMediaOptionName);
                currMainSwiperCont.querySelector('.product-alt__thumb .swiper-wrapper').replaceChildren();
                currMainSwiperCont.querySelector('.product-alt__gallery .swiper-wrapper').replaceChildren();
                mainSwiperCont.insertAdjacentElement('afterend', currMainSwiperCont);
            }
            currMainSwiperCont.querySelector('.product-alt__gallery .swiper-wrapper').append(item)
            currMainSwiperCont.querySelector('.product-alt__thumb .swiper-wrapper').append(mainSwiperCont.querySelector(`.product-alt__thumb .swiper-slide[data-media-id="${item.dataset.mediaId}"]`))
            // $(item).attr('data-variant-image-group', currentMediaOptionName);
        });
        mainSwiperCont.remove();
        
        let activeGallery = this.querySelector('.product-alt__gallery-wrap');
        const preselected = this.querySelector('.product-alt__gallery-wrap-outer').dataset.preSelectedGroup;
        if(preselected)
            activeGallery = this.querySelector(`.product-alt__gallery-wrap[data-variant-image-group="${preselected}"]`);
        activeGallery.classList.add('active');
        this.querySelector('.product-alt__gallery-wrap-outer').style.setProperty('--height', activeGallery.scrollHeight + 'px');
    }

    function updateButButtons(variant) {
        this.querySelectorAll('[data-input-curr-variant-id]').forEach((input) => {
        input.value = variant.id;
        });
        this.querySelectorAll('.product-alt__buy-buttons .product-alt__add-cart').forEach((btn) => {
        if(variant.available && btn.dataset.addToCartText){
            btn.innerHTML = btn.dataset.addToCartText
        }else if(!variant.available && btn.dataset.soldOutText){
            btn.innerHTML = btn.dataset.soldOutText
        }
        btn.toggleAttribute('disabled', !variant.available);
        });
    }
    function updateVariantURL(variant) {
        if (variant) {
        var newurl =
            window.location.protocol + '//' + window.location.host + window.location.pathname + '?variant=' + variant.id;
        window.history.replaceState({ path: newurl }, '', newurl);
        }
    }
    function updateSelectedOptions(variant) {
        if (variant) {
        variant.options.forEach((opt, i) => {
            this.querySelectorAll('.product-alt__option-selectors').forEach((selectors) => {
            const node = selectors.querySelector(`[data-option-index="${i}"] .product-alt__selected_option`);
            if (node) node.innerText = opt;
            });
        });
        }
    }
    function updateVariantVisibilityArea(variant) {
        this.querySelectorAll('.variant-visibility-area').forEach((area) => {
        Array.from(area.children).forEach((child) => {
            if (child.tagName !== 'SCRIPT') {
            child.remove();
            }
        });

        const variantId = variant ? variant.id : '';
        const script = area.querySelector(`script[data-variant-id="${variantId}"]`);

        if (script) {
            area.insertAdjacentHTML('beforeend', script.innerHTML);
        }
        });
    }
    function updateAvailableState(productData) {
        const optionStatusMap = [];
        const currentSelectedOptionValues = [];

        // Collect current selected option values
        this
        .querySelectorAll('.product-alt__option-selectors[data-disable-unavailable] .product-alt__option-selector')
        .forEach((selector) => {
            const checkedInput = selector.querySelector('input:checked');
            let value = null;
            if (checkedInput) {
            value = checkedInput.value;
            }

            currentSelectedOptionValues.push(value);
        });

        // Build option value map
        productData.options.forEach((optionName, optionIndex) => {
        const values = {};

        productData.variants.forEach((variant) => {
            const optionValue = variant.options[optionIndex];
            if (!(optionValue in values)) {
            values[optionValue] = false;
            }
        });

        optionStatusMap.push({
            name: optionName,
            values,
        });
        });

        // Determine availability per option value
        productData.options.forEach((optionName, optionIndex) => {
        const fixedOptions = currentSelectedOptionValues.slice(0, optionIndex);

        Object.keys(optionStatusMap[optionIndex].values).forEach((optionValue) => {
            const fixedOptionsForValue = [...fixedOptions, optionValue];

            let availableVariantExists = false;

            productData.variants.forEach((variant) => {
            let variantComplies = true;

            fixedOptionsForValue.forEach((fixedValue, idx) => {
                if (fixedValue && fixedValue != variant.options[idx]) {
                variantComplies = false;
                }
            });

            if (variantComplies && variant.available) {
                availableVariantExists = true;
            }
            });

            optionStatusMap[optionIndex].values[optionValue] = availableVariantExists;
        });
        });
        // Apply unavailable state to UI
        optionStatusMap.forEach((option, optionIndex) => {
        let available = false;
        Object.entries(option.values).forEach(([optionValue, isAvailable]) => {
            // Listed (radio / swatch)
            available = available || isAvailable;
            this
            .querySelectorAll(`.product-alt__option-selector[data-option-index="${optionIndex}"] .product-alt__opt-btn`)
            .forEach((btn) => {
                if (btn.value === optionValue) {
                btn.classList.toggle('is-unavailable', !isAvailable);
                }
            });
        });
        this
            .querySelector(`.product-alt__option-selector[data-option-index="${optionIndex}"]`)
            ?.classList.toggle('is-unavailable', !available);
        });
    }
    function updateActiveGallery(variant) {
        if (variant) {
        const activeGallery = this.querySelector(`.product-alt__gallery-wrap[data-variant-image-group="${variant.option1}"]`);
        if(activeGallery){
            this.querySelector('.product-alt__gallery-wrap.active').classList.remove('active')
            activeGallery.classList.add('active');
            this.querySelector('.product-alt__gallery-wrap-outer').style.setProperty('--height', activeGallery.scrollHeight + 'px');
        }
        }
    }
}

if (!customElements.get('product-main-alt')) {
  customElements.define('product-main-alt', ProductMainAlt);
}