# all scrapper functions, get the name, description, price, number of reviews, number of stars and price difference according to hdd
def extract_text(page, xpath):
    return page.locator(xpath).inner_text()

def extract_name(page):
    xpath = "xpath=//html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/h4[2]"
    return extract_text(page, xpath)

def extract_description(page, name):
    xpath = "xpath=//html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/p"
    text = extract_text(page, xpath)
    return text.replace(name, "").strip()

def extract_reviews_count(page):
    return extract_text(page, '.ratings')

def extract_star_count(page):
    return len(page.locator('.glyphicon.glyphicon-star').element_handles())

def extract_hdd_price_values(page):
    button_filter = lambda button: button.is_visible() and not button.evaluate('el => el.classList.contains("disabled")')
    hdd_buttons = filter(button_filter, page.locator('.btn.swatch').element_handles())
    return [(button.inner_text(), extract_price_for_hdd(page, button)) for button in hdd_buttons]

def extract_price_for_hdd(page, button):
    button.click()
    page.wait_for_load_state()
    return extract_text(page, '.pull-right.price')