import subprocess, requests
import pdb
from typing import List, Dict

SEARCH_URL = "https://pypi.python.org/pypi/{}/json"

def get_current_package_info() -> List[List[str]]:
    # out = subprocess.run(['pip', 'list'], capture_output=True)
    pip_output_list = subprocess.check_output(['pip', 'list']).decode().strip().split("\n")
    # pdb.set_trace()
    return [pip_output.split()[:2] for pip_output in pip_output_list][2:]

def get_updated_package_info(current_package_info: List[List[str]], verbose: bool) -> Dict[str, Dict[str, str]]:
    updated_package_info = dict()
    for package_name, _ in current_package_info:
        result = requests.get(SEARCH_URL.format(package_name))
        # pdb.set_trace() TODO 지우기
        if result.status_code == 200:
            updated_package_info[package_name] = dict()
            result_json = result.json()
            updated_package_info[package_name]["version"] = result_json["info"]["version"]
            if verbose:
               updated_package_info[package_name]["upload_time"] = result_json["releases"][result_json["info"]["version"]]["upload_time"]
        else:
            if 'error' in updated_package_info.keys():
                updated_package_info['error'].append(package_name)
            else:
                updated_package_info['error'] = []
    
    return updated_package_info

def compare_current_and_updated_package_info(
        current_package_info, updated_package_info, level, verbose
    ) -> Dict[str, Dict[str, str]]:
    pass

def make_output(result) -> None:
    pass
