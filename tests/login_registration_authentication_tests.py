"""This tests login , registration and dashboard authentication"""
from flask import url_for


def test_register_and_login(client):
    with client:
        register_response = client.post("/register", data={
            "email": "testuser1@test.com",
            "password": "test123!test",
            "confirm": "test123!test"
        },
                                        follow_redirects=True)

        assert register_response.status_code == 200
        assert register_response.request.path == url_for('auth.login')

        login_response = client.post("/login", data={
            "email": "testuser1@test.com",
            "password": "test123!test"
        },
                                     follow_redirects=True)
        assert login_response.request.path == url_for('auth.dashboard')
        assert login_response.status_code == 200


def test_dashboard_access(client):
    with client:
        register_response = client.post("/register", data={
            "email": "testuser1@test.com",
            "password": "test123!test",
            "confirm": "test123!test"
        },
                                        follow_redirects=True)

        login_response = client.post("/login", data={
            "email": "testuser1@test.com",
            "password": "test123!test"
        }, follow_redirects=True)
        assert login_response.request.path == url_for('auth.dashboard')
        assert login_response.status_code == 200


def test_dashboard_access_denied(client):
    with client:
        register_response = client.post("/register", data={
            "email": "testuser1@test.com",
            "password": "test123!test",
            "confirm": "test123!test"
        },
                                        follow_redirects=True)

        assert register_response.status_code == 200
        assert register_response.request.path == url_for('auth.login')

        login_response = client.post("/login", data={
            "email": "testuser1@test.com",
            "password": "test1234!test"
        },
                                     follow_redirects=True)
        assert login_response.request.path == url_for('auth.login')
        assert login_response.status_code == 200


def test_csv_upload_access_denied(client):
    """This tests the csv file upload denial"""
    with client:
        # Checking if
        response = client.get("/songs/upload")
        assert response.status_code == 302
        #
        response_following_redirects = client.get("/songs/upload", follow_redirects=True)
        assert response_following_redirects.request.path == url_for('auth.login')
        assert response_following_redirects.status_code == 200


