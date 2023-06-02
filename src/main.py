import giteapy
import dotenv
import sys
import os

from giteapy.rest import ApiException
from pprint import pprint
from github import Github

dotenv.load_dotenv()

if __name__ == '__main__':
    github_user = os.getenv("GITHUB_USER", None)
    gitea_access_token = os.getenv("GITHUB_ACCESS_TOKEN", None)
    gitea_host = os.getenv("GITEA_HOST", None)

    # Configure API key authorization: AccessToken
    configuration = giteapy.Configuration()
    configuration.api_key['access_token'] = gitea_access_token
    configuration.host = gitea_host

    # create an instance of the API class
    gitea_user_api = giteapy.UserApi(giteapy.ApiClient(configuration))
    gitea_repo_api = giteapy.RepositoryApi(giteapy.ApiClient(configuration))

    try:
        # Get the authenticated user
        gitea_user = gitea_user_api.user_get_current()
        # pprint(gitea_user)
    except ApiException as e:
        print("Exception when calling UserApi->user_get_current: %s\n" % e)
        sys.exit()

    try:
        print(f"Retrieving mirrored repos from gitea.")
        # List the repos that the authenticated user owns or has access to
        gitea_mirrored_repos = gitea_user_api.user_current_list_repos()
        # pprint(gitea_mirrored_repos)
    except ApiException as e:
        print("Exception when calling UserApi->user_current_list_repos: %s\n" % e)
        sys.exit()

    mirrored_repos_names = [x.name for x in gitea_mirrored_repos]

    github_client = Github()
    for star in github_client.get_user(github_user).get_starred():
        if star.name not in mirrored_repos_names:
            body = giteapy.MigrateRepoForm(clone_addr=star.clone_url,
                                           repo_name=star.name,
                                           mirror=True,
                                           uid=gitea_user.id)
            try:
                # Migrate a remote git repository
                migrate_response = gitea_repo_api.repo_migrate(body=body)
                pprint(migrate_response)
            except ApiException as e:
                print("Exception when calling RepositoryApi->repo_migrate: %s\n" % e)
