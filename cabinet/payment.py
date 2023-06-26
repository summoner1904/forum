from .crystalpay import CrystalPAY, InvoiceType

shop = 'summoner16'
token = '8b1d1496fb36ef7fec191a3d2bbb88d08765eea8'
salt = 'af6bef649e29474ae48fddc6638b5efe4dfcac89'

payment = CrystalPAY(shop, token, salt)


def create_bill(amount):
    bill = payment.Invoice.create(amount=amount, type_=InvoiceType.purchase, lifetime=15)
    return bill


def check_state(id):
    state = payment.Invoice.getinfo(id)
    if state['state'] == 'payed':
        return True


