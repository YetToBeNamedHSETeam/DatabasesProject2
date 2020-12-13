from PyQt5.QtGui import QTextDocument


def change_rich_label(rich_text_label, new_text):
    doc = QTextDocument()
    doc.setHtml(rich_text_label.text())
    old_text = doc.toPlainText()
    rich_text_label.setText(rich_text_label.text().replace(old_text, new_text))