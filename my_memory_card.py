#создай приложение для запоминания информации
from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QRadioButton, QLabel, QGroupBox

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(600, 400)
lbl = QLabel('Какой национальности не существует?')
btn_otv = QPushButton('Ответить')
box = QGroupBox('Варианты ответов')
btn1 = QRadioButton('Энцы')
btn2 = QRadioButton('Смурфы')
btn3 = QRadioButton('Чулымцы')
btn4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup() 
RadioGroup.addButton(btn1)
RadioGroup.addButton(btn2)
RadioGroup.addButton(btn3)
RadioGroup.addButton(btn4)

vlbox = QVBoxLayout()
hlbox1 = QHBoxLayout()
hlbox2 = QHBoxLayout()
hlbox1.addWidget(btn1)
hlbox1.addWidget(btn2)
hlbox2.addWidget(btn3)
hlbox2.addWidget(btn4)
vlbox.addLayout(hlbox1)
vlbox.addLayout(hlbox2)
box.setLayout(vlbox)
layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout()
layout_line1.addWidget(lbl, alignment=Qt.AlignCenter)
layout_line2.addWidget(box)
layout_line3.addStretch(1)
layout_line3.addWidget(btn_otv, stretch=3) 
layout_line3.addStretch(1)

box2 = QGroupBox('Результат теста')
lbl1 = QLabel('Правильно/Неправильно')
lbl2 = QLabel('Правильный ответ')
vl2 = QVBoxLayout()
vl2.addWidget(lbl1)
vl2.addWidget(lbl2, alignment = Qt.AlignCenter)
box2.setLayout(vl2)
layout_line2.addWidget(box2)
box2.hide()


vl = QVBoxLayout()
vl.addLayout(layout_line1, stretch=2)
vl.addLayout(layout_line2, stretch=8)
vl.addStretch(stretch = 1)
vl.addLayout(layout_line3, stretch=1)
vl.addStretch(stretch = 1)
main_win.setLayout(vl)

def show_question():
    box2.hide()
    box.show()
    btn_otv.setText('Ответить')
    RadioGroup.setExclusive(False)    
    btn1.setChecked(False)
    btn2.setChecked(False)
    btn3.setChecked(False)
    btn4.setChecked(False)
    RadioGroup.setExclusive(True)
def show_result():
    box.hide() 
    box2.show()
    btn_otv.setText('Следующий вопрос')
    
#def start_test():
    #if btn_otv.text() == 'Ответить':
        #show_result()
    #else:
        #show_question()
#btn_otv.clicked.connect(start_test)

answers = [btn1, btn2, btn3, btn4]

#def ask(question, right_answer, wrong1, wrong2, wrong3):
    #shuffle(answers)
    #lbl.setText(question)
    #answers[0].setText(right_answer)
    #answers[1].setText(wrong1)
    #answers[2].setText(wrong2)
    #answers[3].setText(wrong3)
    #lbl2.setText(right_answer)
    #show_question()


def ask(q: Question):
    shuffle(answers)
    lbl.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lbl2.setText(q.right_answer)
    show_question()


def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика')
        print('Всего вопросов -', main_win.total)
        print('Правильных ответов -', main_win.score)
        print('Рейтинг:', main_win.score/main_win.total*100.0, '%')
    else:
        show_correct('Неверно!')
        print('Рейтинг:', main_win.score/main_win.total*100.0, '%')
    
def show_correct(res):
    lbl1.setText(res)
    show_result()




#ask('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Испанский', 'Бразильский')
#q = Question('Государственный язык Бразилии', 'Португальский', 'Итальянский', 'Испанский', 'Бразильский')
#ask(q)
#btn_otv.clicked.connect(check_answer) 

questions_list = []
questions_list.append(
Question('Государственный язык Португалии', 
'Португальский', 'Английский', 'Испанский', 
'Французский'))
questions_list.append(
Question('Какого цвета нет на флаге России?', 
'зеленый', 'синий', 'белый', 
'красный'))
questions_list.append(
Question('Кто отсутствовал на прошлом занятии?', 
'мишка Гамми', 'Егор', 'Илья', 
'преподаватель'))

#main_win.cur_question = -1
def next_question():
    #main_win.cur_question += 1
    main_win.total += 1
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    #if main_win.cur_question >= len(questions_list):
        #main_win.cur_question = 0
    #q = questions_list[main_win.cur_question]
    
    print('Статистика')
    print('Всего вопросов -', main_win.total)
    print('Правильных ответов -', main_win.score)
    ask(q)

def click_OK():
    if btn_otv.text() == 'Следующий вопрос':
        next_question()
    else:
        check_answer()
btn_otv.clicked.connect(click_OK)
main_win.score = 0
main_win.total = 0

next_question()

main_win.show()
app.exec_()































#layout_line2.addWidget(box2)
#box.hide()
#lbl.setText('Самый сложный вопрос в мире!')


