#создай приложение для запоминания 
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QGroupBox, QVBoxLayout, QButtonGroup
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
    

def check_answer(res):
    RadioGroupBox.hide()

    if res == 'Правильно':
        answer.setText('Правильно!')

    elif res == 'Неверно':
        answer.setText('Неправильно!')

    name_button = 'Следующий вопрос'
    button.setText(name_button)
    line_Box.addWidget(AnsGroupBox)
    AnsGroupBox.show()
    
def next_question():
    main_win.total += 1
    AnsGroupBox.hide()
    name_button = 'Ответить'
    button.setText(name_button)
    RadioGroup.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    RadioGroup.setExclusive(True)
    RadioGroupBox.show()

def click_OK():

    if button.text() == 'Следующий вопрос':
        if len(list_question) != 0:
            list_question.pop(main_win.cur_question)
            if len(list_question) != 0:
                main_win.cur_question = randint(0, (len(list_question) - 1))
                next_question()
                ask(list_question[main_win.cur_question])
            else:
                reit = main_win.score/main_win.total * 100
                print('Опрос завершён')
                print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
                print('Рейтинг:', reit, '%')
                exit


    else:
        if answers[0].isChecked():
            check_answer('Правильно')
            main_win.score += 1
            reit = main_win.score/main_win.total * 100
            print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
            print('Рейтинг:', reit, '%')

        elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            check_answer('Неверно')
            print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
            reit = main_win.score/main_win.total * 100
            print('Рейтинг:', reit, '%')
         
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    
    question.setText(q.question)
    right_answer.setText(q.right_answer)

    RadioGroupBox.show()


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400, 200)

question = QLabel('Какой национальности не существует?')
name_button = 'Ответить'
button = QPushButton(name_button)

RadioGroupBox = QGroupBox('Варианты ответов')
AnsGroupBox = QGroupBox('Результаты теста')


button1 = QRadioButton('Энцы')
button2 = QRadioButton('Смурфы')
button3 = QRadioButton('Чулымцы')
button4 = QRadioButton('Алеуты')

RadioGroup= QButtonGroup()
RadioGroup.addButton(button1)
RadioGroup.addButton(button2)
RadioGroup.addButton(button3)
RadioGroup.addButton(button4)

line_main = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()
line_Box = QHBoxLayout()
line_question = QHBoxLayout()
line_Button = QHBoxLayout()


line2.addWidget(button1, alignment = Qt.AlignVCenter)
line2.addWidget(button2, alignment = Qt.AlignVCenter)
line3.addWidget(button3, alignment = Qt.AlignVCenter)
line3.addWidget(button4, alignment = Qt.AlignVCenter)

line1.addLayout(line2)
line1.addLayout(line3)

RadioGroupBox.setLayout(line1)
line_Box.addWidget(RadioGroupBox, alignment = Qt.AlignVCenter)


line_question.addWidget(question, alignment = (Qt.AlignHCenter|Qt.AlignVCenter))
line_Button.addStretch(1)
line_Button.addWidget(button, stretch = 2)
line_Button.addStretch(1)

answer = QLabel('Правильно/Неправильно')
right_answer = QLabel('Правильный ответ')

lineAns = QVBoxLayout()
lineAns_answer = QHBoxLayout()
lineAns_right_answer = QHBoxLayout()

lineAns_answer.addWidget(answer, alignment = Qt.AlignVCenter)
lineAns_right_answer.addWidget(right_answer, alignment = Qt.AlignCenter)

lineAns.addLayout(lineAns_answer)
lineAns.addLayout(lineAns_right_answer)

AnsGroupBox.setLayout(lineAns)
AnsGroupBox.hide()

line_main.addLayout(line_question)
line_main.setSpacing(5)
line_main.addLayout(line_Box)
line_main.setSpacing(5)
line_main.addLayout(line_Button)
line_main.setSpacing(5)

answers = [button1, button2, button3, button4]
list_question = list()
q1 = Question('Какой национальности большая часть Республики Адыгея?', 'Черкесы', 'Карачаевцы', 'Русские', 'Балкарцы')
q2 = Question('Государственный язык ОАЭ', 'Арабский', 'Испанский', 'Итальянский', 'Бразильский')
q3 = Question('Какого цвета нет на флаге Франции?', 'Зеленого', 'Белого', 'Синего', 'Красного')
q4 = Question('Сколько месяцев имеют 28 дней?', '12', '0', '10', '1')
q5 = Question('площадь прямоугольника равен', 'a * b ', 'a + b + c', 'a * b * с', 'a + b')
q6 = Question('Столица России', 'Москва', 'Джакарта', 'Бангладеш', 'Пекин')
q7 = Question('Какой процесс протекает в листе растения?', 'Фотосинтез', 'Терморегуляция', 'Энергообмен', 'Газообмен')
q8 = Question('Какая планета является третьей по удаленности от Солнца?', 'Земля', 'Марс', 'Венера', 'Юпитер')
q9 = Question('Как обозначается сила тока в физике?', 'I', 'F', 'V', 'P')
q10 = Question('Когда начинается месяц Рамадан?', '22 марта', '17 марта', '23 марта', '18 марта')

list_question.append(q1)
list_question.append(q2)
list_question.append(q3)
list_question.append(q4)
list_question.append(q5)
list_question.append(q6)
list_question.append(q7)
list_question.append(q8)
list_question.append(q9)
list_question.append(q10)

main_win.cur_question = randint(0, (len(list_question) - 1))
main_win.total = 1
main_win.score = 0

ask(list_question[main_win.cur_question])
button.clicked.connect(click_OK)
main_win.setLayout(line_main)
main_win.show()
app.exec_()