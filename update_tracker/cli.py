import click, pdb
from update_tracker.local import get_current_package_info, get_updated_package_info, compare_current_and_updated_package_info, make_output

@click.command()
@click.option("--verbose", is_flag=True, help="상세 정보 출력 옵션")
@click.option("--level", default="MICRO", help="지정된 단계까지 출력할 수 있도록 하는 옵션. MAJOR, MINOR, MICRO 가능. default는 MICRO")
def track(verbose, level):
    """현재 PC에 설치된 파이썬 패키지의 업데이트 정보를 출력하는 명령어"""
    current_package_info = get_current_package_info()
    updated_package_info = get_updated_package_info(current_package_info, verbose)
    result = compare_current_and_updated_package_info(current_package_info, updated_package_info, level, verbose)
    # pdb.set_trace()
    make_output(result, verbose, level)
    
