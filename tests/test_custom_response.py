def test_json_response_helper(api, client):
    @api.route("/json")
    def json_handler(req, resp):
        resp.json = {"name": "bubmo"}

    response = client.get("http://testserver/json")
    json_body = response.json()

    assert response.headers["Content-Type"] == "application/json"
    assert json_body["name"] == "bubmo"


def test_html_response_helper(api, client):
    @api.route("/html")
    def html_handler(req, resp):
        resp.html = api.template("index.html", context={"title": "Best Title", "name": "Best Name"})

    response = client.get("http://testserver/html")

    assert "text/html" in response.headers["Content-Type"]
    assert "Best Title" in response.text
    assert "Best Name" in response.text


def test_text_response_helper(api, client):
    response_text = "Just Plain Text"

    @api.route("/text")
    def text_handler(req, resp):
        resp.text = response_text

    response = client.get("http://testserver/text")

    assert "text/plain" in response.headers["Content-Type"]
    assert response.text == response_text


def test_manually_setting_body(api, client):
    @api.route("/body")
    def text_handler(req, resp):
        resp.body = b"Byte Body"
        resp.content_type = "text/plain"

    response = client.get("http://testserver/body")

    assert "text/plain" in response.headers["Content-Type"]
    assert response.text == "Byte Body"
