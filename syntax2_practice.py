#ws_2_a

zero_list = [0]
print(zero_list)
many_zero_list = [0] * 250000
print(len(many_zero_list))
numbers = list(range(1, 11))
print(numbers)
print(numbers[3:])



#ws_2_b

title = '딕셔너리 활용하기'
# 아래에 코드를 작성하시오.

# 2) data 딕셔너리 초기화
data = {
    '과목'   : 'Python',
    '구분'   : '실습',
    '단계'   : 2,
    '문제번호': 3251,
    '이름'   : None,
    '일차'   : 22
}

# 3) 초기 상태 출력
print(data)

# 4) '단계' 값을 "2단계" 형태로 변경 (정수→문자열 변환 + 덧셈)
data['단계'] = str(data['단계']) + '단계'

# 5) '이름'에 title 변수 할당
data['이름'] = title

# 6) '일차'에서 20을 빼기 (복합 연산자 사용)
data['일차'] -= 20

# 7) 최종 상태 출력
print(data)




# title = '딕셔너리 활용하기'
# data = {
#     '과목' : 'Python',
#     '구분' : '실습',
#     '단계' : 2,
#     '문제번호' : 3251,
#     '이름' : None,
#     '일차' : 22,
# }

# print(data)
# data['단계'] = str(data['단계'])+ '단계'

# data['이름'] = title
# data['일차'] = data['일차'] - 20
# print(data)


data = [{'has_more': False,
  'next_cursor': None,
  'object': 'list',
  'page_or_database': {},
  'request_id': 'a5163fff-758f-45ea-b6fb',
  'results': [{'archived': False,
               'cover': None,
               'created_by': {'object': 'user'},
               'created_time': '2023-06-15T04:29:00.000Z',
               'icon': None,
               'last_edited_by': {'object': 'user'},
               'last_edited_time': '2023-12-12T09:19:00.000Z',
               'object': 'page',
               'parent': {'type': 'database_id'},
               'properties': {'setNum': {'id': '%7DK%40%5C',
                                         'number': 1,
                                         'type': 'number'},
                              '과목': {'id': 'YuIE',
                                     'multi_select': [{'color': 'default',
                                                       'name': 'Python'}],
                                     'type': 'multi_select'},
                              '구분': {'id': '%40%3EmR',
                                     'select': {'color': 'purple',
                                                'name': '실습'},
                                     'type': 'select'},
                              '단계': {'id': 'T%7B%7BP',
                                     'select': {'color': 'default',
                                                'name': '3'},
                                     'type': 'select'},
                              '문제번호': {'id': 'uEBt',
                                       'number': 1431,
                                       'type': 'number'},
                              '제목': {'id': 'title',
                                     'title': [{'annotations': {'bold': False,
                                                                'code': False,
                                                                'color': 'default',
                                                                'italic': False,
                                                                'strikethrough': False,
                                                                'underline': False},
                                                'href': None,
                                                'plain_text': '복잡한 자료구조',
                                                'text': {'content': '복잡한 자료구조',
                                                         'link': None},
                                                'type': 'text'}],
                                     'type': 'title'},
                              '일차': {'id': 'nWnH',
                                     'number': '2',
                                     'type': 'number'},
                              '커리큘럼': {'id': 'T%3AR_',
                                       'multi_select': [{'color': 'default',
                                                         'name': 'fundamentals-of-python'}],
                                       'type': 'multi_select'}},
               'public_url': None
            }],
  'type': 'page_or_database'}]

# 아래에 코드를 작성하시오.
item = data[0]['results'][0]
props = item['properties']

first_data = {
    '제목': props['제목']['title'][0]['plain_text'],
    '일차': props['일차']['number'],
    '단계': props['단계']['select']['name'] + '단계',
    '과목': props['과목']['multi_select'][0]['name']
}

print(first_data)


#ws_2_1
print("다음은 이형기 시인의 \"낙화\"의 한 구절이다.\n- 1연\n\t가야할 때 언제인가를\n\t분명히 알고 가는 이의\n\t모습은 얼마나 아름다운가.\n\n나는 이 시를 보며 '나는 내가 가야할 때가 언제일까?' 를 생각해 보았다.")


#ws_2_2
author_1 = '권필'
author_2 = '허균'
book_1 = '주생전'
book_2 = '홍길동전'

print(f"{book_1}의 작가는 {author_1}이고,")
print(f"{author_2}은 {book_2}을 집필하였다.")

#ws_2_3
books = ['광문자전', '유연전', '심청전', '홍길동전', '수성지']
authors = ['작자 미상', '허균', '박지원', '이항복', '임제']

print(authors[1], ":", books[3])
print(authors[3], ":", books[1])
print(authors[0], ":", books[2])
print(authors[2], ":", books[0])
print(authors[4], ":", books[4])


#ws_2_4
information = dict() # 비어있는 dict 객체 생성

authors = ['김시습', '허균', '남영로', '작자 미상', '임제', '박지원']
books = [
    ['장화홍련전', '가락국 신화', '온달 설화'],
    ['금오신화', '이생규장전', '만복자서포기'],
    ['수성지', '백호집', '원생몽유록'],
    ['홍길동전', '장생전', '도문대작'],
    ['옥루몽', '옥련몽'],
]

information = {
    authors[0] : books[1],
    authors[1] : books[3],
    authors[2] : books[4],
    authors[3] : books[0],
    authors[4] : books[2],
} # 객체를 새로 만들어서 할당한 것


for key in information:
    print(f"{key} : { information[key]}")


#ws_2_5
catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
    ['황금의 칼날', '비열한 간신', '무명의 영웅'],
    ['성공의 열쇠', '내면의 변화', '목표의 달성'],
]

import copy
backup_catalog = copy.deepcopy(catalog)

catalog[3][0] = '성공을 향한 한 걸음'
catalog[3][1] = '내 삶의 변화'
catalog[3][2] = '목표 달성의 비밀'

print('catalog와 backup_catalog를 비교한 결과')
print(catalog is backup_catalog)
print('backup_catalog :')
print(backup_catalog)
print()
print('catalog :')
print(catalog)