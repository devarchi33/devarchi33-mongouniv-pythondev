import bottle


@bottle.route("/")
def home_page():
    mythings = ['peach', 'peach', 'orange', 'banana']
    return bottle.template('hello_world', {'username': "Donghoon", 'things': mythings})


@bottle.route("/testpage")
def test_page():
    return "this is a test page."


bottle.debug(True)
bottle.run(host='localhost', port='8080')
