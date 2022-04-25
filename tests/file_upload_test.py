from io import BytesIO
import app
# IMPORT YOU FLASK APP HERE


def test_file_upload():
    client = app.test_client() # you will need your flask app to create the test_client
    data = {
        'file': (BytesIO('Name'), 'music.csv'), # we use StringIO to simulate file object
    }
    # note in that in the previous line you can use 'file' or whatever you want.
    # flask client checks for the tuple (<FileObject>, <String>)
    res = client.post('/upload', data=data)
    assert res.status_code == 200