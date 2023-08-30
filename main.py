from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def search_google(query, api_key, cx):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cx,
        "q": query,
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    product_links = []
    if "items" in data:
        for item in data["items"]:
            product_links.append(item["link"])

    return product_links

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        search_query = request.form["search_query"]
        search_query = search_query.replace('\n', '<br>')  # Заменяем символы новой строки на <br> теги
        google_api_key = "AIzaSyCsIY9oKC_qjd7okUSRKmtN45iH1d62RWM"
        google_cx = "503eb10dabcca4926"
        product_links = search_google(search_query, google_api_key, google_cx)
        return render_template("index.html", search_query=search_query, product_links=product_links)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
