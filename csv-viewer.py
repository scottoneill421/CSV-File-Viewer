from flask import Flask, render_template
import glob
from pathlib import Path
import csv

app = Flask(__name__)

@app.route("/")
def home_page():

    csv_files = glob.glob("./csv-files/*.csv")
    csv_filenames = []

    for file in csv_files:
        file = file[12:-4]
        csv_filenames.append(file)

    return render_template("index.html", content=csv_filenames)

@app.route("/<filename>/")
def csv_detail_view(filename):

    csv_display = []

    csv_file = Path(f'csv-files/{filename}.csv')
    csv_file = open(csv_file, 'r')
    csv_file = csv_file.read().splitlines()
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        csv_display.append(row)


    return render_template("csv-detail.html", content=csv_display)

if __name__ == "__main__":
    app.run(debug=True)
