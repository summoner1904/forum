from .crystalpay import CrystalPAY, InvoiceType

shop = "summoner16"
token = "d7e5c81b9f0ac706ef13a2614227f45771f0f49e"
salt = "c37d19746f7597f9c13862c111fb32d4df3cd75f"

payment = CrystalPAY(shop, token, salt)


def create_bill(amount):
    bill = payment.Invoice.create(
        amount=amount, type_=InvoiceType.purchase, lifetime=60 * 24
    )
    return bill


def check_state(id):
    state = payment.Invoice.getinfo(id)
    if state["state"] == "payed":
        return True
