import requests


url = "https://api.github.com/search/repositories"
url += "?q=language:python+stars:>10000&sort=stars"


headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url=url, headers=headers)
print(f"Status code: {r.status_code}")


response_dict = r.json()

print(f"Total Repos: {response_dict['total_count']}")
print(f"Complete Results: {not response_dict['incomplete_results']}")


repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")

repo_dict = repo_dicts[0]

print("Selcted Info about repository:")
for repo_dict in repo_dicts:
    print()
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")


# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#    print(key)
