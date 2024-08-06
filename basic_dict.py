
def define_dict():
    """
    dict 사전의 정의_
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




if __name__ == "__main__":
    define_dict()