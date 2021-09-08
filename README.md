### Intro
* 본인의 PC 또는 가상환경에 설치된 파이썬 패키지의 최신 버전 정보를 확인할 수 있는 CLI 프로그램

### Basic
**Install**
```shell script
$ pip install update-tracker
```

**Command**
```shell script
$ track
Fetching the latest package data...
Progress: |██████████████████████████████████████████████████| 100.0% 


[REPORT]
--------------------------------------------------------------------------------
MAJOR: ['click']
MICRO: ['prompt-toolkit']

ERROR: ['cello', 'demo-click', 'UpdateTracker']

```

**Options**
* -v, --verbose: 상세 정보 출력 옵션
```shell script
$ track -v
```
* --level: 지정된 단계까지 출력할 수 있도록 하는 옵션. MAJOR, MINOR, MICRO 가능. default는
                 MICRO
```shell script
$ track --level=MAJOR
```


### Code
* https://github.com/Independent-Dev/update_tracker