class Train: 
    __id = None
    __name = ''
    __companyid = None

    # Constructor
    def __init__(self, i=None, n='', cid=None):
        self.__id = mid
        self.__name = n
        self.__companyid = cid

    # Getter - Setters
    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_companyid(self): return self.__companyid

    def set_id(self, i): self.__id = i
    def set_name(self, n): self.__name = n
    def set_companyid(self, cid): self.__companyid = cid