from flask import Flask, render_template
import os

application = Flask(__name__, template_folder='templateFiles', static_folder='static')


def get_sorted_gallery(folder):
    gallery = ""
    artworks = os.listdir(folder)
    valid_images = [".jpg", ".gif", ".png", ".tga"]
    ordered_artworks = []
    for art in artworks:
        ext = os.path.splitext(art)[1]
        if ext.lower() in valid_images:
            ordered_artworks.append(int(os.path.splitext(art)[0]))
    ordered_artworks.sort(key=int)
    for i in range(0, len(ordered_artworks)):
        ordered_artworks[i] = f'{ordered_artworks[i]}' + ".jpg"
    for art in ordered_artworks:
        ext = os.path.splitext(art)[1]
        if ext.lower() not in valid_images:
            continue
        src = '/%s/%s' % (folder, art)
        gallery += "<li><img src='%s' alt='a'></li>" % src
    return gallery


def get_dinamic_gallery(folder):
    gallery = get_sorted_gallery(folder)


@application.route("/")
def home():
    return render_template('index.html', homegallery=get_sorted_gallery("static/css/img/homegallery"))


@application.route("/portfolio")
def portfolio():
    return render_template('portfolio.html',
                           the_way_of_the_haze=get_sorted_gallery("static/css/img/portfolio/the way of the haze"),
                           apotheosis=get_sorted_gallery("static/css/img/portfolio/apotheosis"),
                           kredolis=get_sorted_gallery("static/css/img/portfolio/kredolis"),
                           amindsight=get_sorted_gallery("static/css/img/portfolio/amindsight"))


@application.route("/about")
def about():
    return render_template('about.html')


if __name__ == "__main__":
    application.run(debug=True)
