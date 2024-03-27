import json
from note import Note
from view import View


class ListOfNotes:
    notes = []
    view = View()
    index = 0
    index_stack = []

    def __init__(self):
        try:
            with open('notes.json', 'r') as file:
                notes_dict = json.load(file)
                for note_dict in notes_dict:
                    note = Note()
                    note.set_name(note_dict['name'])
                    note.set_text(note_dict['text'])
                    note.set_id(note_dict['id'])
                    note.update_date()
                    self.notes.append(note)
                self.index = len(self.notes)
            with open('indexes.json', 'r') as file:
                self.index_stack = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.notes = []
            self.view = View()
            self.index = 0
            self.index_stack = []

    def add_note(self):
        note = Note()
        note.set_name(self.view.input_note_name())
        note.set_text(self.view.input_note_text())
        note.update_date()
        if len(self.index_stack) == 0:
            note.set_id(self.index)
        else:
            note.set_id(self.index_stack.pop())
        self.notes.append(note)
        self.index = len(self.notes)
        self.view.info_note_msg('add')

    def delete_note(self, note):
        self.index_stack.append(note.get_id())
        for index, n in enumerate(self.notes):
            if n.id == note.get_id():
                self.notes.pop(index)
                break
        if len(self.notes) == 0:
            self.index_stack.clear()
        self.view.info_note_msg('del')

    def read_all_notes(self):
        self.view.read_all_notes(len(self.notes))
        for note in self.notes:
            self.view.show_note(note)

    def manage_note_by_id(self):
        commands = {1: self.view.show_note,
                    2: self.view.edit_note,
                    3: self.delete_note}
        flag = False
        self.view.show_manage_note_menu()
        choice = self.view.input_number(len(commands.keys()), 'menu')
        value = self.view.input_number(self.index, 'id')
        for note in self.notes:
            if note.id == value:
                commands[choice](note)
                flag = True
        if not flag:
            self.view.not_found()

    def save_notes_to_file(self):
        note_dicts = [note.to_dict() for note in self.notes]
        with open('notes.json', 'w') as file:
            json.dump(note_dicts, file)
        with open('indexes.json', 'w') as file:
            json.dump(self.index_stack, file)
        self.view.saved_info()