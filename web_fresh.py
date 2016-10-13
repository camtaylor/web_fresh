from flask import Flask, request, render_template
app = Flask(__name__)
import scraper
import requests
from PIL import Image
from StringIO import StringIO


@app.route("/", methods=["GET"])
def map():
  url = request.args.get('url')
  logo = scraper.get_logo(url)
  if "http" not in logo:
    logo = url + logo
  navbar_links = scraper.get_navbar_links(url)
  colors = scraper.get_colors(logo)
  return render_template("template.html", logo=logo, navbar_links=navbar_links, colors=colors)


if __name__ == "__main__":
  app.run()
