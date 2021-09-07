import subprocess, requests, pdb
from update_tracker.utils import Level, PackageData
from update_tracker.object.printer import Printer

class UpdateTracker:
    def __init__(self, verbose: bool, level: str, printer: Printer = None) -> None:
        self.verbose = verbose
        self.level = level
        self.printer = printer or Printer(verbose, level)

        self.package_info = dict()
        self.error = dict()
    
    def report_package_info(self):
        self.get_current_package_info()
        self.get_updated_package_info()
        self.compare_current_and_updated_package_info()
        self.printer.make_output(self.result, self.error)
    
    def get_current_package_info(self):
        pip_output_list = subprocess.check_output(['pip', 'list']).decode().strip().split("\n")
        for pip_output in pip_output_list[2:]:
            package_name, package_version = pip_output.split()[:2]
            self.package_info[package_name] = {"current_version": package_version}

    def get_updated_package_info(self):
        SEARCH_URL = "https://pypi.python.org/pypi/{}/json"

        updated_package_info = dict()
        for package_name, package_data in self.package_info.items():
            result = requests.get(SEARCH_URL.format(package_name))
            
            try:
                if result.status_code != 200:
                    raise ValueError('response is not 200')
                result_json = result.json()
                updated_package_info[package_name] = PackageData(
                    **package_data,
                    updated_version = result_json["info"]["version"],
                    upload_time = result_json["releases"][result_json["info"]["version"]][0]["upload_time"]
                )
            except Exception as e:
                self.error[package_name] = str(e)

        self.package_info = updated_package_info

    def compare_current_and_updated_package_info(self):
        self.result = [{} for _ in range(Level[self.level])]
        for package_name, package_data in self.package_info.items():
            if package_data.current_version != package_data.updated_version:  
                current_package_version = package_data.current_version.split(".")
                updated_package_version = package_data.updated_version.split(".")
                for i in range(min(Level[self.level], len(current_package_version))):
                    if current_package_version[i] != updated_package_version[i]:
                        self.result[i][package_name] = package_data
                        break
        


