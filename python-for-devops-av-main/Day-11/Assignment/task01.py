# Import the requests module to make HTTP requests
import requests

# Specify the URL for the GitHub API endpoint to retrieve pull requests for the Kubernetes repository
url = 'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# Send a GET request to the specified URL and store the response
response = requests.get(url)

# Print the HTTP response status code
print(response)
