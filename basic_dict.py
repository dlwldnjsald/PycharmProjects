
def define_dict():
    """
    dict 사전의 정의_
    :  dict는 키 목록(dict_keys)과 값 목록(dict_values)이 합쳐진 복합 자료형
    """
    # 타입 함수를 이용한 생성
    dct = dict() # 빈 dict
    print("dct1:", dct, type(dct))
    # 리터럴 생성
    dct = {}    # 빈 dict
    print("dct2:", dct, type(dct))
    # 키워드 인수로 생성
    dct = dict(one=1, two=2)
    print("dct3:", dct, type(dct))
    # 키, 값 쌍튜플의 목록으로 생성
    dct = dict([("one", 1), ("two",2), ("three",3)])
    print("dct4:", dct, type(dct))

    # 키목록과 값목록이 별도로 있을때 두 목록을 합쳐서 dict 생성
    keys = ('one', 'two', 'three', 'four')
    values = (1, 2, 3)
    dct = dict(zip(keys, values))   # 키목록과 값목록을 합쳐서 dict에 전달
    print("dct5:", dct, type(dct))


def dict_oper():
    """
    dict의 연산
    : 키를 통한 접근 , 가변 자료형
        len, in, not in,
        기본적인 연산 대상은 keySet
    """

    dct = {"baseball":9, "basketball":5}

    # 키를 통한 접근
    dct['soccer'] = 11
    print("dct1:", dct, type(dct))

    # 순서가 없음: 인덱싱, 슬라이싱 불가
    # 길이, 포함 여부 확인 가능
    print("dct2:", dct, "LENGTH:", len(dct))

    print("baseball" in dct)
    print("soccer" in dct)
    print("volleyball" in dct)

    # 포함 여부를 값 목록에서 확인할 경우: values()
    print(9 in dct.values())

    # .keys() : key set를 받아올 수 있음
    # .values() : value 목록을 받아올 수 있음
    # .items() : (키,값) 목록을 받아올 수 있음

    # dict의 키 : 해싱되야 하므로 immutable 자료여야 함
    dct[True] = "true"
    dct[10] = 10
    dct["eleven"] = 11
    dct[(1,2,3)] = 6

    dct[[1, 2, 3]] = 6 #TypeError: unhashable type: 'list'


def dict_methods():
    """
    dict의 메서드들
    """
    dct = {"baseball":9, "basketball":5, "soccer":11}
    print("dct:", dct, type(dct))

    #set(key)-List(value)합쳐진 복합 자료형
    keys = dct.keys()
    print("keys:", keys, type(keys)) #dict_key

    # dict_key도 순차자료형 : set, list 타입 함수로 변환 후 순차형 사용가능
    lst_keys = list(keys)
    print("lst_keys:", lst_keys, type(lst_keys))

    # 값의 목록 : .values() # dict_values
    values = dct.values()
    print("values:", values, type(values))

    #(키, 값) 튜플의 목록: .items() # dict_items
    items = dct.items()
    print("items:", items, type(items))

    lst_items = list(items)
    print("key:", lst_items[1][0], ", value:", lst_items[1][1])

    # dict 비우기
    dct.clear()
    print(dct)


def using_dict():
    """
    dict 사용법
    """
    phones = {
        "둘리": "010-1234-5678",
        "도우너": "010-9876-5432",
        "또치": "010-2222-3333"
    }
    print("phones:", phones)

    #키 접근 vs get() 메서드
    print("둘리 전화번호:", phones["둘리"])
    # print("고길동 전화번호:", phones["고길동"]) #없는 키에 접근시 KeyError
    print("고길동 전화번호:", phones.get("고길동", "고길동키로get했지만몰라로출력해"))

    #아이템 삭제
    del phones['또치']

    # 아이템을 가져오고 동시에 삭제 : pop
    item = phones.pop("도우너")
    print("pop_item:", item)
    print("phones:", phones)


def loop():
    """
    사전의 순회(loop) : 기본적으로 keySet 대상
    """

    phones = {
        "둘리": "010-1234-5678",
        "도우너": "010-9876-5432",
        "또치": "010-2222-3333"
    }

    # 기본적인 루프
    for key in phones:
        print(f"{key}:{phones.get(key)}")

    for key in phones.keys(): #위와 동일
        print(f"{key}:{phones.get(key)}")

    print("items:", phones.items())
    for key,value in phones.items(): # (키,값) ->unpacking
        print(f"{key}:{value}")





if __name__ == "__main__":
    #define_dict()
    #dict_oper()
    #dict_methods()
    #using_dict()
    loop()