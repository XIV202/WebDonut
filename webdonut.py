from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class WebDonutBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://xiv202.github.io/MainPageRu/"))

        # Создаем виджет для браузера
        self.setCentralWidget(self.browser)

        # Создаем панель навигации
        navbar = QToolBar()
        self.addToolBar(navbar)

        # Кнопка "Назад"
        back_btn = QAction('Назад', self)
        back_btn.setStatusTip('Назад к предыдущей странице')
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # Кнопка "Вперед"
        forward_btn = QAction('Вперед', self)
        forward_btn.setStatusTip('Вперед к следующей странице')
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # Кнопка "Обновить"
        reload_btn = QAction('Обновить', self)
        reload_btn.setStatusTip('Обновить страницу')
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # Кнопка "Домой"
        home_btn = QAction('Домой', self)
        home_btn.setStatusTip('Перейти на домашнюю страницу')
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Поле адреса
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        # Кнопка "Перейти"
        go_btn = QAction('Перейти', self)
        go_btn.setStatusTip('Перейти по указанному адресу')
        go_btn.triggered.connect(self.navigate_to_url)
        navbar.addAction(go_btn)

        # Кнопка "Добавить в закладки"
        bookmark_btn = QAction('Добавить в закладки', self)
        bookmark_btn.setStatusTip('Добавить текущую страницу в закладки')
        bookmark_btn.triggered.connect(self.add_to_bookmarks)
        navbar.addAction(bookmark_btn)

        # Добавляем разделитель в панель навигации
        navbar.addSeparator()

        # Кнопка "Открыть внешнюю страницу"
        external_page_btn = QAction('Открыть внешнюю страницу', self)
        external_page_btn.setStatusTip('Открыть внешнюю страницу в новом окне')
        external_page_btn.triggered.connect(self.open_external_page)
        navbar.addAction(external_page_btn)

        # Устанавливаем начальный размер окна
        self.setGeometry(100, 100, 1024, 768)
        self.setWindowTitle('WebDonut Browser')

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://xiv202.github.io/MainPageRu/"))

    def navigate_to_url(self):
        q = QUrl(self.url_bar.text())
        if q.scheme() == "":
            q.setScheme("http")

        self.browser.setUrl(q)

    def add_to_bookmarks(self):
        current_url = self.browser.url().toString()
        QMessageBox.information(self, 'Добавить в закладки', f'Добавлено в закладки:\n\n{current_url}')

    def open_external_page(self):
        external_url, ok = QInputDialog.getText(self, 'Открыть внешнюю страницу', 'Введите URL:')
        if ok:
            external_browser = QWebEngineView()
            external_browser.setUrl(QUrl(external_url))
            external_browser.show()

if __name__ == '__main__':
    app = QApplication([])
    QApplication.setApplicationName("WebDonut Browser")
    window = WebDonutBrowser()
    window.show()
    app.exec_()
