class Route:
    __id = None
    __means_id = None
    __departure_location_id = None
    __destination_location_id = None

    # Constructor
    def __init__(self, i=None, mid=None, dli=None, deli=None):
        self.__id = i
        self.__means_id = mid
        self.__departure_location_id = dli
        self.__destination_location_id = deli

    # Getters - Setters
    def get_id(self): return self.__id
    def get_means_id(self): return self.__means_id
    def get_departure_location_id(self): return self.__departure_location_id
    def get_destination_location_id(self): return self.__destination_location_id

    def set_id(self, i): self.__id = i
    def set_means_id(self, mid): self.__means_id = mid
    def set_departure_location_id(self, dli): self.__departure_location_id = dli
    def set_destination_location_id(self, deli): self.__destination_location_id = deli