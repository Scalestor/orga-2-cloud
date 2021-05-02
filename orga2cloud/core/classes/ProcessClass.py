# Idea for the Base Process Object
# What does it need?
# Properties
# - Name
# - Id
# - Datetime
# - Version
# - Author


# Additional ideas
# - Derive it from a general base classe
# - This object needs to be stored somehow

class BaseProcess():

    def __init__(self, id, name):
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
        if len(value) > 20:
            raise ValueError("Name cannot exceed 20 characters.")
        self._name = value



class BaseProcessDefinition():
    def __init__(self):
        owner=None # What object own the ProcessDefinition
        legitimation_group =  [] # Permitted User - for the future



class BaseActiveProcess(BaseProcess):
    def __init__(self):
        pass





