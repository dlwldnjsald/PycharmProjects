
def using_range():
    """
    range 객체 :범위 객체
    - 범위 정보만 가지고 있다가 요청할 때 조건의 계산한 후 결과를 반환
    - 큰 범위 데이터를 생성해도 메모리가 증가하지 않음 : generator
    :syntax: range([start=0, ] end [, stop=1])
    """
    #인자값이 1개 -> 끝값
    seq = range(10) #10은 범위에 포함되지 않음
    print("seq:", seq, type(seq))
    print("seq_list:", list(seq)) #확인용// 굳이 리스트화할필요X

    #인자값이 2개 -> 시작값, 끝값
    seq2 = range(2,10) #2이상, 10미만
    print("seq2:", seq2)
    print("seq2_list:", list(seq2))

    #인자값이 3개 -> 시작값, 끝값, 간격값
    seq3 = range(0, 10, 2) #2이상, 10미만, 2간격
    print("seq3:", seq3)
    print("seq3_list:", list(seq3))

    # 큰수 -> 작은수 : 간격값을 음수로
    seq4 = range(0, -10, -1) #0이하, -10초과, -1간격(역순출력)
    print("seq4:", seq4)
    print("seq4_list:", list(seq4))

    # range도 순차 자료형 : len, 인덱싱, 슬라이싱, in, not in 가능
    print("seq:", seq, "LENGTH:", len(seq))
    print("5 in seq:", 5 in seq) #포함여부 확인
    print(seq[-3], seq[-2], seq[-1], #역방향 인덱스
          seq[0], seq[1], seq[2], seq[3]) #정방향 인덱스

    # range는 변경 불가
    # seq[0] = 10 # 슬라이싱 가능, 치환은X

    # loop
    # ex) 1-10까지 2간격 루프돌릴때
    for i in range(1,11,2):
        print(i,end="\t")
    else:
        print()

    # 로또
    import itertools
    it = itertools.combinations(range(1, 46), 6)
    for num in it:
        print(num)


def using_enumerate():
    """
    enumerate 함수
    : 순차 자료형을 인덱스와 함께 튜플로 출력해주는 함수: generator
    : 순차 자료형에서 아이템과 함께 아이템의 인덱스를 함꼐 활용하고자 할 때 활용/
    """

    # 루프를 돌리면서 인덱스와 함께 출력하고자 할때
    colors = ["red", "yellow", "blue", "green", "white", "black", "gray"]
    i = 0  # index위한
    for color in colors:
        print("COLOR {0}:{1}".format(i,color))
        i += 1

    print("=====enumerate 1=====")
    for index, color in enumerate(colors):  # (인덱스정보, 요소값)
        print(f"COLOR {index}:{color}")

    # 다른 방법 : enumerate 함수를 사용했을 때
    print("=====enumerate 2=====")
    for i, color in enumerate(colors):
        print("COLOR {0}:{1}".format(i,color))


def using_zip():
    """
    zip: 여러 시퀀스 자료를 동시에 루프시켜 튜플로 생성해주는 Generator
    """
    eng = ["Sunday", "Monday", "Tuesday", "Wednesday"]
    kor = ["일요일", "월요일", "화요일", "수요일", "목요일"]

    engkor = zip(eng, kor)
    print(engkor, type(engkor))

    # 기본 순회
    for pair in engkor:
        #print("pair:", pair, type(pair))
        print(f"영어 {pair[0]} -> 한국어 {pair[1]}")

    print("=============unpacking======")
    engkor = zip(eng,kor)
    #unpacking
    for eng, kor in engkor:
        print(f"영어 {eng} -> 한국어 {kor}")






if __name__ == "__main__":
    #using_range()
    #using_enumerate()
    using_zip()