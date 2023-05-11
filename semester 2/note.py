class Note:
    def __init__(self, name, ton):
        self._name = name
        self._ton = ton
    def __setattr__ (self, name, value):
        if name == '_ton':
            if value in range(-1, 2):
                super().__setattr__(name, value)
            else: raise IndexError('недопустимый индекс')
        elif name == '_name':
            if f'_{value}' in Notes.__slots__:
                super().__setattr__(name, value)
            else: raise ValueError('недопустимое значение аргумента')
        else: super().__setattr__(name, value)

    
class Notes:
    __slots__ = ['_do', '_re', '_mi', '_fa', '_solt', '_la', '_si']
    def __init__(self) -> None:
        for note in self.__slots__:
            setattr(self, note, Note(note[1:], 0))
    def __getitem__(self, key):
        if key in range(0, 7):
            return getattr(self, self.__slots__[key])
        else: raise IndexError('недопустимый индекс')
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Notes, cls).__new__(cls)
        return cls.instance
    
# notes = Notes()
# note7 = notes[6]
# note7._ton = -2

