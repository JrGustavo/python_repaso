class SMS:
    def send(self):
        print("Sending SMS...")

class Saver:
    def save(self):
        print("Se guarda en una BD")

class Email:
    def send(self):
        print("Sending Email...")


class Sale(SMS, Saver, Email):
    pass

sale = Sale()
sale.send()
sale.save()