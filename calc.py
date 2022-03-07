# 파이썬의 tkinter 모듈을 이용하여 간단한 계산기를 만들어보기 

from dis import dis
import tkinter as tk


calc = tk.Tk()

# 이름, 크기 설정
# 이름은 "Calculatir" 크기는 300 X 300
calc.title("Calculator")
calc.geometry("300x300")


# 엔터키 연결
# 버튼 추가 ( = , C) 버튼
def calculate(event):                    # func 함수 작성 / func 함수 이름을 calculate로 변경
    value = tk.Entry.get(display)
    
    if value != '':
        result = eval(value)
        print(result)
        display.delete(0, tk.END)
        display.insert(0, result)

def clear(event):                        # C 버튼과 Esc 키을 위한 함수 입니다. 
    display.delete(0, tk.END)            # 내용 삭제 
    
    """# 계산하기
    result = eval(tk.Entry.get(display))  # eval() 함수로 계산
    print(result)
    display.delete(0, tk.END)       # 0번째 자리부터 끝까지 삭제하는 명령어 / 내용 삭제 의미
    display.insert(0, result)       # 0번째 자리에 result라는 변수값을 입력하는 명령어 
    # 입력창의 값 가져오기 
    print(tk.Entry.get(display))    # 입력창에 들어 있는 값을 출력해줍니다."""



# 출력창 추가 
display = tk.Entry(calc, width = 20) # display라는 이름의 출력창 추가, 폭은 20 
display.pack()                       # 위치를 정해주는 명령어  => 그럼 다른 위치 관련 명령어는?


# 버튼 추가 

button_e = tk.Button(calc, text = '=', width =5)    # '=' 버튼 추가 
button_e.bind('<Button-1>', calculate)               # 버튼에 클릭 이벤트 추가 
button_e.pack()


button_c = tk.Button(calc, text = 'C', width= 5)    # 'C' 버튼 추가, text 속성은 버튼에 표시할 문자입니다.
button_c.bind('<Button-1>', clear)                  # <Button-1> 이벤트는 마우스 왼쪽 클릭 이벤트입니다. 
button_c.pack()



calc.bind('<Return>', calculate)          # 엔터키(이벤트)를 calculate 함수로 연결
calc.bind('<Escape>', clear)              # Esc 키도 c버튼과 동일한 기능을 하도록 연결합니다. 

calc. mainloop()
