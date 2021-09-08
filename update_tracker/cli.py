import click
from update_tracker.utils import Level
from update_tracker.object.update_tracker import UpdateTracker

def level_validation_check(ctx, param, value):
    if value not in Level.__members__:
        raise click.BadParameter(f"{[level.name for level in Level]} 가운데 하나를 입력하여야 합니다!")
    return value

@click.command()
@click.option("--verbose", "-v", is_flag=True, default=False, help="상세 정보 출력 옵션")
@click.option("--level", default="MICRO", callback=level_validation_check, help="지정된 단계까지 출력할 수 있도록 하는 옵션. MAJOR, MINOR, MICRO 가능. default는 MICRO")
def track(verbose, level):
    """현재 PC에 설치된 파이썬 패키지의 업데이트 정보를 출력하는 명령어"""
    update_tracker = UpdateTracker(verbose, level)
    update_tracker.report_package_info()
    
