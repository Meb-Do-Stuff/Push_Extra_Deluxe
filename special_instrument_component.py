from pushbase.instrument_component import NoteLayout


class SpecialNoteLayout(NoteLayout):
    def __init__(self, *a, **k):
        super(SpecialNoteLayout, self).__init__(*a, **k)
