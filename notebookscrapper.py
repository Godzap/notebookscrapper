# run the flask and return the json
from flask import Flask, jsonify
from browser_utils import launch_browser
from data_collection import collect_all_notebooks_data
from playwright.sync_api import sync_playwright


app = Flask(__name__)

@app.route('/notebooks', methods=['GET'])
def get_notebooks():
    with sync_playwright() as p:
        browser = launch_browser(p)
        notebooks_data = collect_all_notebooks_data(browser)
        browser.close()
        return jsonify(notebooks_data)


if __name__ == "__main__":
    app.run(debug=True)
