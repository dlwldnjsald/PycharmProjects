evens = { 0, 2, 4, 6, 8, 10 } # 짝수 집합
odds = { 1, 3, 5, 7, 9 } # 홀수 집합
numbers = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 } # 전체 집합
mthree = { 0, 3, 6, 9 } # 3의 배수 집합


def define_set():
    """
    집합 정의 연습
    SET : 순서 X, 중복 허용 X,
            len, in, not in 확인 가능
    """

    empty = set() # 빈 set
    print(type(empty), type({}))

    # 길이, 포함 여부는 확인 가능
    print(numbers, "LENGTH:", len(numbers))
    print("2 in numbers:", 2 in numbers, "/ 2 in evens:", 2 in evens, "/ 2 in odds:", 2 in odds)

    # 다른 순차형으로 set 만들기
    s = "Python Programming"
    chars = set(s.upper())
    print(s, chars)

    # list 등 순차자료형의 중복값을 제거할 때 유용
    lst = "Python Programming Java Programming HTML Programming".split()
    print("lst:", lst)
    # 리스트에서 중복 요소를 제거한 요소 갯수는 ?
    s = set(lst)
    print("to_set:", s, len(s))
    lst2 = list(s)
    print("to_lst2:", lst2)


def set_methods():
    """
    set의 메서드들
    """















if __name__ == "__main__":
     define_set()
     #set_methods()