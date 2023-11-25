# Import the requests module to make HTTP requests
import requests

# Specify the URL for the GitHub API endpoint to retrieve pull requests for the Kubernetes repository
url = 'https://api.github.com/repos/kubernetes/kubernetes/pulls'

# Send a GET request to the specified URL and store the response
response = requests.get(url)

# Parse the response content as JSON and store the complete details of the pull requests
complete_details = response.json()

# Print the ID and title of the first pull request in the list
print(complete_details[0]["id"])
print(complete_details[0]["title"])

# Iterate through the list of pull requests and print the login of the user who created each pull request
for i in range(len(complete_details)):
    print(complete_details[i]["user"]["login"])