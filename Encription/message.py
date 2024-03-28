class Message:
    _id_next = 100

    def __init__(self, text, author, date, classification):
        self._text = text
        self._author = author
        self._date = date
        self._classification = classification
        self._id = Message._id_next
        Message._id_next += 1

    def get_id(self):
        return self._id

    def get_classification(self):
        return self._classification

    def display_properties(self):
        print(f"\t[{self._id}] {self._classification} message from {self._author} at {self._date}")

    def display_text(self):
        print(f"\tMessage: {self._text}")

    def update_text(self, new_text):
        self._text = new_text

    def clear(self):
        self._text = ""
        self._author = ""
        self._date = ""
