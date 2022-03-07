# 파이썬의 tkinter 모듈을 이용하여 간단한 계산기를 만들어보기 

import tkinter as tk


calc = tk.Tk()

# 이름, 크기 설정
# 이름은 "Calculatir" 크기는 300 X 300
calc.title("Calculator")
calc.geometry("300x300")


# 엔터키 연결
def func(event):                    # func 함수 작성
    print('enter pressed')          # 일단 임시로 문자열 출력


# 출력창 추가 
display = tk.Entry(calc, width = 20) # display라는 이름의 출력창 추가, 폭은 20 
display.pack()                       # 위치를 정해주는 명령어  => 그럼 다른 위치 관련 명령어는?


calc.bind('<Return>', func)          # 엔터키(이벤트)를 func 함수로 연결


calc. mainloop()
