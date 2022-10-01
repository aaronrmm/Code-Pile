from pydantic import BaseModel


class BitbucketQueryConfig(BaseModel):
    starting_url = "https://api.bitbucket.org/2.0/repositories"
    max_repos: int = 0
