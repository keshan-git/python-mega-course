from ui import BookStoreUI
from backend import BookService


def main():
    service = BookService()
    if not service.view_data():
        service.populate_data()

    ui = BookStoreUI(service)
    ui.show_ui()


if __name__ == '__main__':
    main()