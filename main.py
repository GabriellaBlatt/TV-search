import os
from bottle import (get, post, redirect, request, route, run, static_file, template, error)
import utils
import json


# Static Routes

@get("/js/<filepath:re:.*\.js>")
def js(filepath):
    return static_file(filepath, root="./js")


@get("/css/<filepath:re:.*\.css>")
def css(filepath):
    return static_file(filepath, root="./css")


@get("/images/<filepath:re:.*\.(jpg|png|gif|ico|svg)>")
def img(filepath):
    return static_file(filepath, root="./images")

@route('/')
def index():
    sectionTemplate = "./templates/home.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@error(404)
def error404(error):
    sectionTemplate = "./templates/404.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate, sectionData={})


@route('/browse')
def index():
    sectionTemplate = "./templates/browse.tpl"
    all_of_shows = [json.loads(utils.getJsonFromFile(utils.AVAILABE_SHOWS[i])) for i in range(12)]
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData=all_of_shows)

@route('/ajax/show/<id>')
def show_page(id):
    all_of_shows = [json.loads(utils.getJsonFromFile(utils.AVAILABE_SHOWS[i])) for i in range(12)]
    wanted_show = ""
    id = int(id)
    for show in all_of_shows:
        if show["id"] == id:
            wanted_show = show
    return template("./templates/show.tpl", version=utils.getVersion(),
                    result=wanted_show)


@route('/show/<id>')
def show_page(id):
    sectionTemplate= "./templates/show.tpl"
    all_of_shows = [json.loads(utils.getJsonFromFile(utils.AVAILABE_SHOWS[i])) for i in range(12)]
    wanted_show = ""
    id = int(id)
    for show in all_of_shows:
        if show["id"] == id:
            wanted_show = show
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData=wanted_show)


@route('/ajax/show/<id>/episode/<episode>')
def show_details(id, episode):
    all_of_shows = [json.loads(utils.getJsonFromFile(utils.AVAILABE_SHOWS[i])) for i in range(12)]
    id = int(id)
    episode=int(episode)
    for show in all_of_shows:
        if show["id"] == id:
            correct_show = show
    for ep in correct_show["_embedded"]["episodes"]:
        if ep["id"]==episode:
            episode=ep
    return template('./templates/episode.tpl', version=utils.getVersion(),
                result=episode)


@route('/show/<id>/episode/<episode>')
def show_details(id, episode):
    sectionTemplate = "./templates/episode.tpl"
    all_of_shows = [json.loads(utils.getJsonFromFile(utils.AVAILABE_SHOWS[i])) for i in range(12)]
    id = int(id)
    episode=int(episode)
    for show in all_of_shows:
        if show["id"] == id:
            correct_show = show
    for ep in correct_show["_embedded"]["episodes"]:
        if ep["id"]==episode:
            episode=ep

    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
               sectionData=episode)


run(host='localhost', port=os.environ.get('PORT', 7000))
