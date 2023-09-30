from PyQt5.QtCore import Qt 
from PyQt5.OtWidget import( 
    QApplication, QWidget, QTableWidget, QListWidget, 
     QLineEdit, QFormLoyout, QHBoxLayout, 
      QVBoxLayout, QGroupBox, QButtonGroup, 
      QPushButton, QLabel, QRadioButton, QSpinBox) 
from logika import*

list_question = QListView()
widget_add = QWidget()
widget.setLayout(layout_form)
btn_add = QPushButton('нове питання') 
btn_del = QPushButton('Видалити питання')
btn_start = QPushButton("Початок тесту")

qst_col = QVBoxLayout #Question collume(стовпчик з питанням)
qst_col.addWidget(list_question)
qst_col.addWidget(btn_add)

ans_col = QVBoxLayout
ans_col.addWidget(widget_ans)
ans_col.addWidget(btn_del)

btn_line = QHBoxLayout()
btn_line.addLayout(qst_col)
btn_line.addLayout(ans_col)

test_line = QHBoxLayout
test_line.addStretch(1)
test_line.addWidgebtn(btn_start, stretch = 2)
test_line.addStretch(1)

layout_screen = QVBoxLayout()
layout_screen.addLayout(test_line)















