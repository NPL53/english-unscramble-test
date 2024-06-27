import argparse
import dataclasses
import json
import random
import re
from typing import List

import dacite


def main(): 
    argument_parser = argparse.ArgumentParser(description="문장 단어 조합 연습기.")
    argument_parser.add_argument(
        "testfile", type=str, help="json 형식의 테스트 파일 경로를 입력하세요.")
    argument_parser.add_argument("testname", type=str, help="테스트 이름을 입력하세요.")
    argument_parser.add_argument(
        "--keep-order", dest="keep_order", action="store_true", help="문제 순서를 파일의 순서로 고정합니다.")
    argument_parser.add_argument(
        "--disable-hint", dest="disable_hint", action="store_true", help="문장의 단어 보기를 비활성화합니다.")
    namespace = argument_parser.parse_args()

    @dataclasses.dataclass
    class sentence_test:
        sentence: str
        korean: str

    @dataclasses.dataclass
    class test_set:
        name: str
        sentences: List[sentence_test]

    with open(namespace.testfile, "rt", encoding="utf-8") as fp:
        json_object = json.load(fp)

    tests = [dacite.from_dict(test_set, e) for e in json_object]
    found = [tests[i]
             for i in range(len(tests)) if tests[i].name == namespace.testname]

    if len(found) != 1:
        raise Exception("대상 테스트 이름이 중복되거나 없습니다.")
    else:
        target = found[0]

        space_pattern = re.compile('\\s+')

        sentence_tests: List[sentence_test] = []
        ignored_count = 0

        for test in target.sentences:
            if (len(test.sentence) == 0 or test.sentence.isspace()) \
                or (len(test.korean) == 0 or test.korean.isspace()):
                ignored_count += 1
            else:
                test.sentence = re.sub(space_pattern, ' ', test.sentence.strip())
                test.korean = re.sub(space_pattern, ' ', test.korean.strip())
                sentence_tests.append(test)

        if not namespace.keep_order:
            random.shuffle(sentence_tests)

        test_count = len(sentence_tests)
        print("%d개의 문장을 읽었습니다." % test_count)

        if ignored_count > 0:
            print("(%d개의 문장이 비어있어 무시되었습니다.)"%ignored_count)

        checked_tests: List[sentence_test] = []
        for index, sentence_test_ in enumerate(sentence_tests):
            test_number = index + 1

            print("%d. %s" % (test_number, sentence_test_.korean))
            if not namespace.disable_hint:
                words = sentence_test_.sentence.split(' ')
                shuffled_words = words.copy()
                random.shuffle(shuffled_words)
                print(' / '.join(shuffled_words))
            answer = input("정답을 입력하세요: ")

            compared_answer = re.sub(space_pattern, ' ', answer.strip())
            if compared_answer == sentence_test_.sentence:
                print("맞았습니다.\n")
            else:
                print("틀렸습니다.\n정답: %s\n"%sentence_test_.sentence)
                checked_tests.append(sentence_test_)

        checked_count = len(checked_tests)
        print("\n요약: 맞은 개수 %d개 / 틀린 개수 %d개" %
              (test_count-checked_count, checked_count))

        print("\n틀린 문장 목록:\n")
        if checked_count > 0:
            for test_ in checked_tests:
                print("%s\n%s\n" % (test_.sentence, test_.korean))
        else:
            print("없음")
    pass


if __name__ == "__main__":
    main()
