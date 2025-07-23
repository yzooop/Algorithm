import re

def solution(new_id):
    # 1: 대 -> 소
    new_id = new_id.lower()

    # 2: 알파벳 소문자, 숫자, '-', '_', '.'를 제외한 문자 제거
    new_id = re.sub(r'[^a-z0-9\-_.]', '', new_id)

    # 3: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표로 치환
    new_id = re.sub(r'\.+', '.', new_id)

    # 4: 처음이나 끝에 위치한 마침표 제거
    new_id = new_id.strip('.')

    # 5: 빈 문자열이면 a 대입
    if not new_id:
        new_id = 'a'

    # 6: 16자 이상이면 처음 15자만 남기고, 마지막 마침표 제거
    new_id = new_id[:15].rstrip('.')

    # 7: 길이가 2자 이하라면, 마지막 문자를 반복하여 길이가 3이 될 때까지 붙임
    while len(new_id) < 3:
        new_id += new_id[-1]

    return new_id
