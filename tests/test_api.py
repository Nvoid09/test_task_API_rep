import requests
import pathlib

def test_process_csv():
    """
    Test process_csv api endpoint
    """
    url = 'http://127.0.0.1:8080/process_csv'
    files = {'file': ('data_changed_2_strings.csv', open(
        'tests/data_changed_2_strings.csv', 'rb'), 'text/csv')}
    response = requests.post(url, files=files)

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0
    assert 'saddr' in data[0]
    assert 'avgDur' in data[0]
