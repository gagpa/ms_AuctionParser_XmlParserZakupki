from .handlers  import add, Handler


class Lot(Handler):
    __regex = '\w*{tag}\w*'
    paths = (add('MaxPrice', 'max_price', 'maxprice', ['lot', 'maxPriceInfo'], regex=False),
             add('TotalSum', 'total_sum', 'totalSum', ['purchaseObjects']),
             add('code', 'code', 'code', ['currency']),
             )

    main_tags = ['lot', 'notificationInfo'.lower()]

    __max_price = None
    __total_sum = None
    __code = None
    __okpd = None
    __price = None
    __name_obj = None

    @property
    def max_price(self):
        return self.__max_price

    @max_price.setter
    def max_price(self, value):
        if isinstance(value, ( str, int, float)):
            self.__max_price = float(value)
        elif isinstance(value, list):
            self.__max_price = float(value[0])
        else:
            raise TypeError

    @property
    def total_sum(self):
        return self.__total_sum

    @total_sum.setter
    def total_sum(self, value):
        if isinstance(value, (str, int, float)):
            self.__total_sum = float(value)
        elif isinstance(value, list):
            self.__total_sum = float(value[0])
        else:
            raise TypeError

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        if isinstance(value, str):
            self.__code = value
        elif isinstance(value, list):
            self.__code = value[0]
        else:
            raise TypeError
