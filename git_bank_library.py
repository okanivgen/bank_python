

class Bank:
    """
    Banka hesap sınıfı
    """
    def __init__(self, account_number, account_name, account_surname, card_password):
        self.name = account_name
        self.number= account_number
        self.password = card_password
        self.balance = [] # Bakiye listesi
        self.surname = account_surname


    def add_balance(self, amount):
        """
        Bakiyeye para ekleme işlemi
        """
        self.balance.append(amount)

    def get_total_balance(self):
        """
        Toplam bakiyeyi hesaplar
        """
        return sum(self.balance)

    def __str__(self):
        """
        Hesap sahibinin adı ve soyadı ile merhaba mesajı döndürür
        """
        return f"Merhaba {self.name} {self.surname}"