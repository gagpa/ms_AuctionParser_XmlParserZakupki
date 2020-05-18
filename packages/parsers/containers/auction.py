from .handlers import add, Handler


class Auction(Handler):

    paths = (
        add('id', 'id', 'id', ['notification'], regex=False),
        add('purchaseNumber', 'purchase_number', 'purchasenumber', ['notification', 'commonInfo']),
        add('createDate', 'create_date', 'publishdate', ['notification', 'commonInfo']),
        add('startDate', 'start_date', 'startDate', ['collecting', 'commonInfo']),
        add('endDate', 'end_date', 'enddate', ['collecting', 'commonInfo']),
        add('htmlUrl', 'html_url', 'href', ['notification', 'commonInfo']),
        add('objectInfo', 'object_info', 'purchaseObjectInfo', ['notification', 'commonInfo']),
        add('ikz', 'ikz', 'purchaseCode', ['contractConditionsInfo', 'customerRequirement']),
        add('MaxPrice', 'max_price', 'maxprice', ['lot', 'maxPriceInfo'], regex=False),
        add('contractGuarantee', 'contract_guarantee', 'amount', ['contractGuarantee']),
        add('applicationGuarantee', 'application_guarantee', 'amount', ['applicationGuarantee']),
        add('contractGuaranteePart', 'contract_guarantee_part', 'part', ['contractGuarantee']),
        add('applicationGuaranteePart', 'application_guarantee_part', 'part', ['applicationGuarantee']),
    )
    __id = None
    __purchase_number = None
    __create_date = None
    __start_date = None
    __end_date = None
    __html_url = None
    __ikz = None
    __object_info = None
    __application_guarantee = None
    __contract_guarantee = None
    __application_guarantee_part = None
    __contract_guarantee_part = None
    __max_price = None

    def __init__(self):
        __name__ = 'Auction'

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        if isinstance(value, str) or isinstance(value, int):
            self.__id = int(value)
        elif isinstance(value, list):
            self.__id = int(value[0])
        else:
            raise TypeError

    @property
    def purchase_number(self):
        return self.__purchase_number

    @purchase_number.setter
    def purchase_number(self, value):
        if isinstance(value, (str, int)):
            self.__purchase_number = int(value)
        elif isinstance(value, list):
            self.__purchase_number = int(value[0])
        else:
            raise TypeError

    @property
    def create_date(self):
        return self.__create_date

    @create_date.setter
    def create_date(self, value):
        if isinstance(value, str):
            self.__create_date = self.handle_date(value)
        elif isinstance(value, list):
            self.__create_date = self.handle_date(value[0])
        else:
            raise TypeError

    @property
    def start_date(self):
        return self.__start_date

    @start_date.setter
    def start_date(self, value):
        if isinstance(value, str):
            self.__start_date = self.handle_date(value)
        elif isinstance(value, list):
            self.__start_date = self.handle_date(value[0])
        else:
            raise TypeError

    @property
    def end_date(self):
        return self.__end_date

    @end_date.setter
    def end_date(self, value):
        if isinstance(value, str):
            self.__end_date = self.handle_date(value)
        elif isinstance(value, list):
            self.__end_date = self.handle_date(value[0])
        else:
            raise TypeError

    @property
    def html_url(self):
        return self.__html_url

    @html_url.setter
    def html_url(self, value):
        if isinstance(value, str):
            self.__html_url = value
        elif isinstance(value, list):
            self.__html_url = value[0]
        else:
            raise TypeError

    @property
    def object_info(self):
        return self.__object_info

    @object_info.setter
    def object_info(self, value):
        if isinstance(value, str):
            self.__object_info = value
        elif isinstance(value, list):
            self.__object_info = value[0]
        else:
            raise TypeError

    @property
    def ikz(self):
        return self.__ikz

    @ikz.setter
    def ikz(self, value):
        if isinstance(value, (str, int)):
            self.__ikz = str(value)
        elif isinstance(value, list):
            self.__ikz = str(value[0])
        else:
            raise TypeError

    @property
    def contract_guarantee(self):
        return self.__contract_guarantee

    @contract_guarantee.setter
    def contract_guarantee(self, value):
        if isinstance(value, (str, int, float)):
            self.__contract_guarantee = float(value)
        elif isinstance(value, list):
            self.__contract_guarantee = float(value[0])
        else:
            raise TypeError

    @property
    def application_guarantee(self):
        return self.__application_guarantee

    @application_guarantee.setter
    def application_guarantee(self, value):
        if isinstance(value, (str, int, float)):
            self.__application_guarantee = float(value)
        elif isinstance(value, list):
            self.__application_guarantee = float(value[0])
        else:
            raise TypeError

    @property
    def contract_guarantee_part(self):
        return self.__contract_guarantee_part

    @contract_guarantee_part.setter
    def contract_guarantee_part(self, value):
        if isinstance(value, (str, int, float)):
            self.__contract_guarantee_part = float(value)
        elif isinstance(value, list):
            self.__contract_guarantee_part = float(value[0])
        else:
            raise TypeError
        if self.max_price:
            self.contract_guarantee = self.max_price * self.__contract_guarantee_part / 100

    @property
    def application_guarantee_part(self):
        return self.__application_guarantee_part

    @application_guarantee_part.setter
    def application_guarantee_part(self, value):
        if isinstance(value, (str, int, float)):
            self.__application_guarantee_part = float(value)
        elif isinstance(value, list):
            self.__application_guarantee_part = float(value[0])
        else:
            raise TypeError
        if self.max_price:
            self.application_guarantee = self.max_price // self.__application_guarantee_part

    @property
    def max_price(self):
        return self.__max_price

    @max_price.setter
    def max_price(self, value):
        if isinstance(value, (str, int, float)):
            self.__max_price = float(value)
        elif isinstance(value, list):
            self.__max_price = float(value[0])
        else:
            raise TypeError
