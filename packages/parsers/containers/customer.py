from .handlers  import add, Handler


class Customer(Handler):
    paths = (
        add('customerId', 'customer_id', 'regNum', ['responsibleOrg']),
        add('fullname', 'fullname', 'fullname', ['responsibleorg']),
        add('postAddress', 'post_address', 'postaddress', ['responsibleorg']),
        add('factAddress', 'fact_address', 'factaddress', ['responsibleorg']),
        add('inn', 'inn', 'inn', ['responsibleorg']),
        add('kpp', 'kpp', 'kpp', ['responsibleorg']))

    main_tags = ['purchaseResponsible'.lower(), 'responsibleOrgInfo'.lower()]

    __customer_id = None
    __fullname = None
    __post_address = None
    __fact_address = None
    __inn = None
    __kpp = None

    @property
    def customer_id(self):
        return self.__customer_id

    @customer_id.setter
    def customer_id(self, value):
        if isinstance(value, (str, int)):
            self.__customer_id = int(value)
        elif isinstance(value, list):
            self.__customer_id = int(value[0])
        else:
            raise TypeError

    @property
    def fullname(self):
        return self.__fullname

    @fullname.setter
    def fullname(self, value):
        if isinstance(value, str):
            self.__fullname = value
        elif isinstance(value, list):
            self.__fullname = value[0]
        else:
            raise TypeError

    @property
    def post_address(self):
        return self.__post_address

    @post_address.setter
    def post_address(self, value):
        if isinstance(value, str):
            self.__post_address = value
        elif isinstance(value, list):
            self.__post_address = value[0]
        else:
            raise TypeError

    @property
    def fact_address(self):
        return self.__fact_address

    @fact_address.setter
    def fact_address(self, value):
        if isinstance(value, str):
            self.__fact_address = value
        elif isinstance(value, list):
            self.__fact_address = value[0]
        else:
            raise TypeError

    @property
    def inn(self):
        return self.__inn

    @inn.setter
    def inn(self, value):
        if isinstance(value, (str, int)):
            self.__inn = value
        elif isinstance(value, list):
            self.__inn = value[0]
        else:
            raise TypeError

    @property
    def kpp(self):
        return self.__kpp

    @kpp.setter
    def kpp(self, value):
        if isinstance(value, (str, int)):
            self.__kpp = value
        elif isinstance(value, list):
            self.__kpp = value[0]
        else:
            raise TypeError
