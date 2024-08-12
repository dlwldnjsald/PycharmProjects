def define_tuple():
    """
    튜플의 정의
    tuple: 리스트와 거의 동일, 변경 불가 자료(immutable)
            len, 인덱싱, 슬라이싱, 연결, 반복, 포함 여부
            내부 요소 변경 불가
    """
    tp1 = () # 공튜플
    tp2 = tuple() # 공튜플
    print("tp1:", tp1, type(tp1))
    print("tp2:", tp2, type(tp2))

    tp3 = (1,) # 요소가 1개일 경우 요소뒤에 반드시(,) 콤마표시
    print("tp3:", tp3, type(tp3))


def tuple_oper():
    """
    튜플 연산
    """
    tp =(1,2,3,4,5)

    # 길이를 구할 수 있다
    print("tp:", tp, "LENGTH:", len(tp))

    # 인덱싱 가능
    print("INDEX:", tp[-3], tp[-2], tp[-1], # 역방향 인덱싱
                    tp[0], tp[1], tp[2], tp[3]) # 정방향 인덱싱

    # 슬라이싱 [시작경계 : 끝경계 : 간격값]
    slice = tp[1:4]
    print("slice tp[1:4]:", slice, "type:", type(slice))
    slice = tp[:] # 처음부터 -> 생략가능, 끝까지 -> 생략가능, [:] 튜플전체 지정
    print("slice tp[:]:", slice)

    # 반복 *
    print("tp * 3:", tp * 3)

    # 연결 +
    print("tp +:", tp + (6,7,8,9,10))

    # 포함 여부 : in, not in
    print("5 in tp:", 5 in tp)
    print("1 not in tp:", 1 not in tp)


"""
    튜플의 할당
    """
def tuple_assign():
    # 튜플을 이용, 좌우변의 여러값을 동시 할당
    x,y,z = 10, 20, 30 #튜플
    print("x,y,z:", x,y,z)

    # 튜플을 이용한 스왑swap(값 교환)
    x, y = 10, 20
    print(x, y)
    x, y = y, x # 튜플 이용한 교환
    print("swap:", x, y)


def tuple_method():
    """
    튜플의 메서드들
    """
    tp = (20, 30, 10, 20)
    print("COUNT:", tp.count(20)) # 요소의 갯수
    print("INDEX:", tp.index(20)) # 요소의 인덱스
    print("INDEX:", tp.index(20,1)) # 요소의 인덱스, 범위 제한


def packing_unpacking():
    """
    튜플 패킹과 언패킹
    """
    # 튜플의 Packing/
    tp = (10, 20, 30, "Python") # 기본적으로 튜플 생성 방법
    print("tp:", tp, type(tp))
    tp = 10, 20, 30, "Python" # 괄호 안붙이고 값만 나열해도 자동 튜플로 인식
    print("tp:", tp, type(tp))

    # 튜플의 Unpacking
    a, b, c, d = tp
    print("a,b,c,d:", a, b, c, d)

    # a, b, c = tp        # 좌변의 변수 개수 적거나
    # a, b, c, d, e = tp  # 좌변의 변수 개수가 많을경우 모두 ValueError

    # 확장 Unpacking
    a, *b = tp  # 확장 언패킹 기호 *
    print("a:", a, type(a))
    print("*b:", b, type(b))

    *a, b = tp
    print("*a:", a, type(a))
    print("b:", b, type(b))

    a, *b, c = tp
    print("a:", a, type(a))
    print("*b:", b, type(b))
    print("c:", c, type(c))


    # tuple 리스트와 동일 , 불변자료형
    # 수정을 제외 모든 리스트의 기능=> 튜플에 적용 가능
    # 하나의 요소만을 가질때 (,) 필수
    # 튜플의 패킹, 언패킹 ,확장 언패킹





if __name__ == "__main__":
    #define_tuple()
    #tuple_oper()
    #tuple_assign()
    #tuple_method()
    packing_unpacking()