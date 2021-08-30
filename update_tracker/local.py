import subprocess, requests, click
import pdb
from typing import List, Dict
from update_tracker.utils import Level

SEARCH_URL = "https://pypi.python.org/pypi/{}/json"

def get_current_package_info() -> List[List[str]]:
    pip_output_list = subprocess.check_output(['pip', 'list']).decode().strip().split("\n")
    return [pip_output.split()[:2] for pip_output in pip_output_list][2:]

def get_updated_package_info(current_package_info: List[List[str]], verbose: bool) -> Dict[str, Dict[str, str]]:
    updated_package_info = dict()

    for package_name, _ in current_package_info:
        result = requests.get(SEARCH_URL.format(package_name))
        if result.status_code == 200:
            updated_package_info[package_name] = dict()
            result_json = result.json()
            updated_package_info[package_name]["updated_version"] = result_json["info"]["version"]
            if verbose:
               updated_package_info[package_name]["upload_time"] = result_json["releases"][result_json["info"]["version"]]["upload_time"]
        else:
            if 'error' in updated_package_info.keys():
                updated_package_info['error'].append(package_name)
            else:
                updated_package_info['error'] = [package_name]
    
    return updated_package_info

def compare_current_and_updated_package_info(
        current_package_info, updated_package_info, level, verbose
    ) -> Dict[str, Dict[str, str]]:
    result = [{} for _ in range(Level[level])]
    for package_name, current_package_version in current_package_info:
        if package_name not in updated_package_info["error"]:
            current_package_version = current_package_version.split(".")
            updated_package_version = updated_package_info[package_name]["updated_version"].split(".")
            for i in range(min(Level[level], len(current_package_version))):
                if current_package_version[i] != updated_package_version[i]:
                    result[i][package_name] = updated_package_info[package_name]
                    # if verbose:
                    result[i][package_name]["current_version"] = current_package_version
                    break
    
    result.append(updated_package_info["error"])
    return result

def make_output(result, verbose, level) -> None:
    for level in Level:
        click.echo(f"{level.name}: {result[level.value - 1].keys()}")
    click.echo(f"error package: {result[-1]}")
