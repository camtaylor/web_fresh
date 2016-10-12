from flask import Flask, request, render_template
app = Flask(__name__)
import scraper
import requests

@app.route("/", methods=["GET"])
def map():
  url = request.args.get('url')
  logo = scraper.get_logo(url)
  if "http" not in logo:
    logo = url + logo
  print logo
  return render_template("template.html", logo=logo)


if __name__ == "__main__":
  app.run()
