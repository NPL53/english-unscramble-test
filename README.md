ENGLISH-UNSCRAMBLE-TEST
=======================


사용방법
------

### 테스트 파일 작성

프로그램을 사용하기 위해 테스트 파일이 필요합니다.
테스트 파일은 json형식으로 작성합니다.

시험 정보는 이렇게 작성합니다.
```json
{
    "name": "any_name",
    "sentences": [
        {
            "sentence": "any sentence",
            "korean": "어떤 문장"
        }
    ]
}

```
name 은 시험 이름이고, sentences 는 문장 정보 배열입니다.

sentences 배열 안의 문장 정보는 아래와 같이 작성합니다.
```json
{
    "sentence": "any sentence",
    "korean": "어떤 문장"
}
```
sentence 는 영어 문장이고, korean은 그 문장의 뜻입니다.

테스트 파일은 시험 정보의 배열로 되어있으며, 시험의 이름을 다르게 해서 여러 시험 정보를 저장할 수 있습니다.

example 디렉터리에 있는 예제 파일을 확인하세요.

### 프로그램 실행

테스트 파일 경로가 example/example1.json, 테스트 이름이 any_name이라고 한다면 아래의 명령어를 입력하면 됩니다.

```
python english-unscramble-test.py example/example1.json any_name
```

실행하면 문제가 한국어 뜻과 문장이 단어 단위로 무작위로 섞인 보기로 제공됩니다.

문제마다 보기를 참고해 답을 입력하고 결과를 확인하세요.

<image src="image/correct.png">

<image src="image/incorrect.png">

연습 시험이 끝나면 맞은 개수와 틀린 개수를 표시하고 틀린 문장을 표시한 후 프로그램이 종료됩니다.

<image src="image/result.png">

### 정답 판정
프로그램은 사용자가 입력한 답의 앞, 뒤 공백을 제거하고 단어 사이의 공백을 띄어쓰기 1개로 바꾼 후 테스트 파일의 문장과 같은지 비교합니다.

문장 부호와 대소문자가 모두 일치해야 합니다.

### 프로그램 인수
- <b>--keep-order</b>: 문제의 순서를 테스트 파일의 순서로 고정합니다.

라이브러리
------------

아래의 라이브러리가 설치되어 있어야 합니다.
- dacite