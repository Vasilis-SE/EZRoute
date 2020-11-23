class Company:
    __id = None
    __name = ''
    __location_id = None

    # Constructor
    def __init__(self, i=None, n='', lid=None):
        self.__id = mid
        self.__name = n
        self.__location_id = lid

    # Getter - Setters
    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_location_id(self): return self.__location_id

    def set_id(self, i): self.__id = i
    def set_name(self, n): self.__name = n
    def set_location_id(self, lid): self.__location_id = lid