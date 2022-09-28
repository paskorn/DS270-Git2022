import requests
from plotly.graph_objs import bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
a=input("Hello")
print(a)
# Store API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

repo_names, star = [], []


print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    star.append(repo_dict['stargazers_count'])

# Make visualization.
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]

    
    #print(f"Name: {repo_dict['name']}")
    #print(f"Owner: {repo_dict['owner']['login']}")
    #print(f"Stars: {repo_dict['stargazers_count']}")
    #print(f"Repository: {repo_dict['html_url']}")
    #print(f"Created: {repo_dict['created_at']}")
    #print(f"Updated: {repo_dict['updated_at']}")
    #print(f"Description: {repo_dict['description']}")
