class Message:
    # Static variable for the next id
    _id_next = 100

    def __init__(self, text, author, date, classification):
        self._text = text
        self._author = author
        self._date = date
        self._classification = classification
        self._id = Message._id_next
        Message._id_next += 1
        self._empty = False

    def get_id(self):
        return self._id

    def display_properties(self):
        if self._empty:
            return
        print(f"\t[{self._id}] Message from {self._author} at {self._date}")

    def display_text(self):
        print(f"\tMessage: {self._text}")

    def update_text(self, new_text):
        self._text = new_text

    def clear(self):
        self._text = "Empty"
        self._author = ""
        self._date = ""
        self._empty = True

    def get_classification(self):
        return self._classification


class Messages:
    def __init__(self, filename):
        self._messages = []
        self._read_messages(filename)

    def display(self):
        for m in self._messages:
            m.display_properties()

    def show(self, id):
        for m in self._messages:
            if m.get_id() == id:
                m.display_text()
                return True
        return False

    def update(self, id, text):
        for m in self._messages:
            if m.get_id() == id:
                m.update_text(text)

    def remove(self, id):
        for m in self._messages:
            if m.get_id() == id:
                m.clear()

    def add(self, text, author, date, classification):
        m = Message(text, author, date, classification)
        self._messages.append(m)

    def _read_messages(self, filename):
        try:
            with open(filename, "r") as f:
                for line in f:
                    text_control, author, date, text, classification = line.split('|')
                    self.add(text.rstrip('\r\n'), author, date, classification)

        except FileNotFoundError:
            print(f"ERROR! Unable to open file \"{filename}\"")
            return

    def get_message_classification(self, message_id):
        for message in self._messages:
            if message.get_id() == message_id:
                return message.get_classification()
        return None
