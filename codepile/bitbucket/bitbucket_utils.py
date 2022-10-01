import os
import json
from typing import Any, List, Dict
import requests
import json
from time import sleep

def parse_repo_files(parent_dir:str)->List[Any]:
    parsed_repos = []
    
    parent_dir = os.path.abspath(parent_dir)
    assert os.path.isdir(parent_dir), f"No directory at {parent_dir}"
    for filename in os.listdir(parent_dir):
        file_path = os.path.join(parent_dir, filename)
        with open(file_path, "r") as fp:
            parsed_repos.append(
                json.load(fp)
            )
    return parsed_repos

def query_for_json(url:str, print_on_failure: bool=False, seconds_to_pause: int=0)->Dict[str, Any]:
    headers = {
       "Accept": "application/json",
    }

    response = requests.request(
       "GET",
       url,
       headers=headers
    )
    try:
        return json.loads(response.text)
    except:
        if print_on_failure:
            try:
                print(response.text)
            except:
                print(response)
    if seconds_to_pause > 0:
        sleep(seconds_to_pause)