import csv

from note import Note


class View:
    def greeting(self):
        print("Приложение 'заметки'")

    def main_menu(self):
        print("Выберите желаемое действие:\n"
              "\t1. Добавить заметку\n"
              "\t2. Чтение / Изменение / Удаление заметки\n"
              "\t3. Показать список заметок\n"
              "\t4. Сохранить заметки\n"
              "\t0. Выйти из приложения")

    def show_manage_note_menu(self):
        print("Выберите необходимое:\n"
              "\t1. Прочитать заметку\n"
              "\t2. Изменить заметку\n"
              "\t3. Удалить заметку\n")

    def error(self):
        print("Ошибка ввода. Пожалуйста, попробуйте снова:")

    def not_found(self):
        print("Заметка с данным id не найдена. Пожалуйста, попробуйте снова:")

    def saved_info(self):
        print("Заметки успешно сохранены")

    def show_note(self, note):
        result = f"ID: {str(note.get_id())}|\t"
        result += f"[{str(note.get_date())}]\t"
        result += f"[{str(note.get_name())}]\n"
        result += f"{str(note.get_text())}\n"

        print(result)

    def read_all_notes(self, count):
        result = f"\tСписок заметок\n"
        match count:
            case 1:
                result = result + f"Найдено {count} заметка\n"
            case 2:
                result = result + f"Найдено {count} заметки\n"
            case 3:
                result = result + f"Найдено {count} заметки\n"
            case 4:
                result = result + f"Найдено {count} заметки\n"
            case _:
                result = result + f"Найдено {count} заметок\n"
        print(result)

    def info_note_msg(self, key):
        info = {'add': 'добавлена', 'del': 'удалена', 'edit': 'изменена'}
        print(f"Заметка успешно {info[key]}!")

    def input_note_name(self):
        return input(f"Введите заголовок заметки:")

    def input_note_text(self):
        return input(f"Введите тело заметки:")

    def edit_note(self, note):
        note.set_text(self.input_note_text())
        note.update_date()
        self.info_note_msg('edit')

    def input_number(self, limit, preset):
        presets = {'id': 'заметки', 'menu': 'пункта меню'}
        value = 0
        while True:
            try:
                value = int(input(f"Введите номер {presets[preset]}: "))
            except ValueError:
                self.error()
                continue
            if 0 <= value <= 4:
                break
            else:
                self.not_found()
        return value

    def exit_msg(self):
        print("Завершение работы")