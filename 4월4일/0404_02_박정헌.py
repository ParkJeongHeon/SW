'''
    작성일 : 2024년 3월 29일
    작성자 : 컴퓨터공학부 202495007 박정헌
    설명 : 점수를 입력받아 학점을 출력하시오.
            90~100 : A학점
            80~89  : B학점
            70~79  : C학점
            60~69  : D학점
            0~59   : F학점

    [문제분석]
        필요한 변수 : score (점수)

        ★★★★★ 점수는 0~100점 사이이다.

    [알고리즘]
        1. 점수를 입력받는다. 
        
'''
score = int(input("점수를 입력하시오."))

if 90 <= score <= 100 :
    if score >= 90 :
        print(f"{score}점은 A학점입니다.")
elif score >= 80 :
    print(f"{score}점은 B학점입니다.")
elif score >= 70 : 
    print(f"{score}점은 C학점입니다.")
elif score >= 60 : 
    print(f"{score}점은 D학점입니다.")      
else : 
    print(f"{score}점은 F학점입니다.")