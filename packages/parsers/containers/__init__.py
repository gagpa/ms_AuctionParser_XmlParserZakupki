from . import auction, customer, lot


class ContainerFactory:
    __containers = {'auction': auction.Auction,
                    'customer': customer.Customer,
                    'lot': lot.Lot}

    @staticmethod
    def get_container(name):
        container = ContainerFactory.__containers.get(name)
        return container()
