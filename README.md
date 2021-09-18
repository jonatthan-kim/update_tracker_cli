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
**MAJOR 업데이트가 이미 진행된 패키지입니다!**
package_name        current_version     updated_version     upload_time         
click               7.1.2               8.0.1               2021-05-20 06:00:32 

**MINOR 업데이트가 이미 진행된 패키지입니다!**
package_name        current_version     updated_version     upload_time         
build               0.6.0.post1         0.7.0               2021-09-17 06:20:37 
keyring             23.1.0              23.2.1              2021-09-13 02:16:33 

**PATCH 업데이트가 이미 진행된 패키지입니다!**
package_name        current_version     updated_version     upload_time         
alembic             1.7.1               1.7.3               2021-09-18 00:29:20 
charset-normalizer  2.0.4               2.0.6               2021-09-18 07:21:49 
prompt-toolkit      3.0.3               3.0.20              2021-08-20 19:44:46 
setuptools          58.0.2              58.0.4              2021-09-09 11:03:12 


**ERROR**
package_name         error_reason                            
cello                Unknown info format. Check on https://pypi.python.org/pypi/cello/json
UpdateTracker        Package not found in PyPI               
--------------------------------------------------------------------------------
```

**Options**
* -s, --summary: 요약 정보 출력 옵션
```shell script
$ track -s
```
* --level: 지정된 단계까지 출력할 수 있도록 하는 옵션. MAJOR, MINOR, PATCH 가능. default는 PATCH
```shell script
$ track --level=MAJOR
```


### Code
* https://github.com/Independent-Dev/update_tracker