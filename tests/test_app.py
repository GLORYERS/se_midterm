import serverTeSt

def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hi'

def test_login(client, app):
    # login page
    assert client.get('/').status_code == 200
    # login test

    response = client.post(
        '/log', data={'Username': 'a', 'Password': 'a'}
    )
    assert 'http://localhost/room' == response.headers['Location']