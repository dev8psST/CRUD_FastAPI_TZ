import requests
# Define the API endpoint URL

url = 'http://localhost:8000/posts/1'
url2 = 'http://localhost:8000/authors/1'
# Make a GET request to the API endpoint
def rr(url,param=''):
    response = requests.get(url)
# Check the response status code
    if response.status_code == 200:
    # Print the response content
        print(response.json())
        data = response.json()
        print(data[f'{param}'])
    else:
        # Handle the error
        print('Error: {0}'.format(response.status_code)) 
    return data

def test_author_name():
    data = rr('http://localhost:8000/authors/1', 'name')
    assert data['name'] == 'Arthur'
