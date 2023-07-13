# collects, gathers and organizes all data from notebooks
from functools import partial
from browser_utils import navigate_to_page
from scraper_utils import extract_name, extract_description, extract_hdd_price_values, extract_reviews_count, extract_star_count

def collect_notebook_data(browser, link):
    page = navigate_to_page(browser, link)
    name = extract_name(page)
    description = extract_description(page, name)
    hdd_price_values = extract_hdd_price_values(page)
    reviews_count = extract_reviews_count(page)
    star_count = extract_star_count(page)
    return {"name": name, "description": description, "hdd_price_values": hdd_price_values, "reviews_count": reviews_count, "star_count": star_count}

def extract_lenovo_notebook_links(browser):
    page = navigate_to_page(browser, "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops")
    notebook_links = ["https://webscraper.io" + notebook.query_selector('a').get_attribute('href') 
                      for notebook in page.query_selector_all('.col-sm-4.col-lg-4.col-md-4')
                      if "lenovo" in notebook.query_selector('.title').text_content().lower()]
    return notebook_links

def collect_all_notebooks_data(browser):
    notebook_links = extract_lenovo_notebook_links(browser)
    collect_notebook_data_with_browser = partial(collect_notebook_data, browser)
    notebook_data = list(map(collect_notebook_data_with_browser, notebook_links))
    return notebook_data
