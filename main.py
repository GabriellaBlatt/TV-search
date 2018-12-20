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
    sectionTemplate = './templates/browse.tpl'
    all_of_shows = [json.loads(utils.getJsonFromFile(utils.AVAILABE_SHOWS[i])) for i in range(12)]
    wanted_show = ""
    id = int(id)
    for show in all_of_shows:
        if show["id"] == id:
            wanted_show = show
            return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                            sectionData=[wanted_show])
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData=[wanted_show])

@route('/show/<id>')
def show_page(id):
    sectionTemplate = './templates/browse.tpl'
    all_of_shows = [json.loads(utils.getJsonFromFile(utils.AVAILABE_SHOWS[i])) for i in range(12)]
    wanted_show = ""
    id = int(id)
    for show in all_of_shows:
        if show["id"] == id:
            wanted_show = show
            return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                            sectionData=[wanted_show])
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData=[wanted_show])

@route('/search', method='GET')
def index():
    sectionTemplate = "./templates/search.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData={})


@route('/search', method='POST')
def index():
    show_key = request.forms.get('q')
    relevant_shows = utils.find_relevant_shows(show_key)
    sectionTemplate = "./templates/search_result.tpl"
    return template("./pages/index.html", version=utils.getVersion(), sectionTemplate=sectionTemplate,
                    sectionData=relevant_shows, query=show_key)


run(host='localhost', port=os.environ.get('PORT', 7000))
