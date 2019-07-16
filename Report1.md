# RPLab_DL_Report1

(1) 문자열 자료형은 그 요소값을 변경할 수 없다.

    Immutable, str objects

(2) "".join(x)를 사용하면 리스트 내의 string1과 string2를 연결할 수 있다.
    *3으로 문장을 세 번 반복한다.

    def expand(x):
       a="".join(x)
       b=a*3
       return b

(3) \를 사용하면 line continuaiton이 가능하다.

    s='a'+'b' \
     +'c'+'d' \
     +'e'+'f'
     
(4) 딕셔너리 {'foo':1, 'bar':2, 'baz':3}에 'bar'가 있으므로 1과 2를 출력한다.
    문자열 'qux'에 'a'가 없으므로 3을 출력하지 않는다.
   
    1
    2
   
(5) d={'a':0,'b':1,'c':0}에서 d['a']=0이므로 >0이 성립하지 않아 다음 문장으로 넘어가고 d['b']=1이므로 >0이 성립하여 'ok'가 출력되고
    프로그램이 종료된다.
   
    F
   
(7) /는 나눗셈의 값을 실수형으로 반환한다.

    4.0
   
(8) 숫자 사이의 and 연산은 더 큰 값을 반환한다.

    200
  
(10) reference는 변수를 의미하고(m,n) object는 변수가 가리키는 실질적인 값을 의미한다(300). 

     One object, two references
