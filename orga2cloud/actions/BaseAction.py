


class BaseAction():
    def __init__(self, action_id, name):
        self._id = id
        self.name = name

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) ==0:
            raise ValueError("Name cannot be empty!")
        self._name = value