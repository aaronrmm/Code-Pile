import json
from time import sleep
from typing import Any, Dict, List

from codepile.bitbucket.api import BitbucketQueryConfig
from codepile.bitbucket.bitbucket_utils import query_for_json
from codepile.bitbucket.types import BitbucketRepo, BitbucketQueryResult


def query_public_repos(query_config: BitbucketQueryConfig):
    repos_result = BitbucketQueryResult(starting_query=query_config.starting_url)
    next = query_config.starting_url
    try:
        for _ in range(query_config.max_repos):
            result: Dict[str, Any] = query_for_json(next, seconds_to_pause=5)
            next = result["next"]
            repos = result["values"]
            for repo_dict in repos:
                repo = BitbucketRepo(hash=repo_dict["str"], details=repo_dict)
                repos_result.repos[repo.hash] = repo
            if not next:
                break
        repos_result.is_complete = True
    except Exception as e:
        print(e)
    repos_result.next_query = next
    return repos_result
