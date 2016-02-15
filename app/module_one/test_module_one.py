
from flask import Flask, json
from .models import greet_user
from .controllers import module_one

class TestGreetUser(object):
    """
    Tests the greet_user model function

    This is an example of a way to test model logic.
    """

    def test_verify_greeting_for_even_length_names(self):
        for n in ["Ryan", "Martin", "Jane",]:
            assert greet_user(n) == "Nice to see you!"

    def test_verify_greeting_for_odd_length_names(self):
        for n in ["Tim", "Susan", "Francis",]:
            assert greet_user(n) == "Thanks for visiting!"

#from app import app
class TestControllers(object):

    def setup_method(self, test_method):
        #self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        #flaskr.app.config['TESTING'] = True
        app = Flask(__name__)
        app.config["DEBUG"] = True
        app.config["TESTING"] = True
        app.register_blueprint(module_one)
        self.app = app.test_client()
        #flaskr.init_db()

    def teardown_method(self, test_method):
        #os.close(self.db_fd)
        #os.unlink(flaskr.app.config['DATABASE'])
        pass

    def test_module_one_index(self):
        rv = self.app.get('/')
        assert "200 OK" == rv.status

    def test_module_one_hi(self):
        rv = self.app.get('/hi/ryan')
        assert "200 OK" == rv.status

    def test_api_say_hi_GET(self):
        rv = self.app.get('/api/say-hi')
        assert "200 OK" == rv.status
        assert "application/json" == rv.headers["Content-Type"]
        assert json.loads(rv.get_data()) == "Hi!"

    def test_api_say_hi_POST(self):
        rv = self.app.post('/api/say-hi', content_type="application/json", data='["yo"]')
        assert "200 OK" == rv.status
        assert "application/json" == rv.headers["Content-Type"]
        assert json.loads(rv.get_data()) == {"hi": "POST", "json": ["yo"]}
