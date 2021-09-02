import subprocess, requests, click
from typing import List, Dict
from update_tracker.utils import Level

def get_current_package_info() -> Dict[str, Dict[str, str]]:
    current_package_info = dict()
    pip_output_list = subprocess.check_output(['pip', 'list']).decode().strip().split("\n")
    for pip_output in pip_output_list[2:]:
        package_name, package_version = pip_output.split()[:2]
        current_package_info[package_name] = {"current_version": package_version}
    return current_package_info


def get_updated_package_info(current_package_info: Dict[str, Dict[str, str]]) -> Dict[str, Dict[str, str]]:
    SEARCH_URL = "https://pypi.python.org/pypi/{}/json"

    updated_package_info = dict(error=[])
    for package_name, package_data in current_package_info.items():
        result = requests.get(SEARCH_URL.format(package_name))
        if result.status_code == 200:
            try:
                result_json = result.json()
                updated_package_info[package_name] = dict(**package_data)
                updated_package_info[package_name]["updated_version"] = result_json["info"]["version"]
                updated_package_info[package_name]["upload_time"] = result_json["releases"][result_json["info"]["version"]][0]["upload_time"]
            except Exception as e:
                updated_package_info['error'].append(package_name)
        else:
            updated_package_info['error'].append(package_name)

    return updated_package_info

def compare_current_and_updated_package_info(updated_package_info: Dict[str, Dict[str, str]], level) -> Dict[str, Dict[str, str]]:
    result = [{} for _ in range(Level[level])]
    for package_name, package_data in updated_package_info.items():
        if package_name != 'error':
            if package_data["current_version"] != package_data["updated_version"]:  
                current_package_version = package_data["current_version"].split(".")
                updated_package_version = package_data["updated_version"].split(".")
                for i in range(min(Level[level], len(current_package_version))):
                    if current_package_version[i] != updated_package_version[i]:
                        result[i][package_name] = package_data
                        break
    
    result.append(updated_package_info["error"])
    return result

def make_output(result: Dict[str, Dict[str, str]], verbose, level) -> None:
    for l in Level:
        click.echo(f"{l.name}: {result[l.value - 1].keys()}")
        if level == l.name:
            break
    click.echo(f"error package: {result[-1]}")
