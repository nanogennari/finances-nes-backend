from datetime import datetime
from . import settings

class Transaction:
    def __init__(self, amount: float, category: int, description: str = "") -> None:
        """Instancia um objeto Transaction.

        Args:
            amount (float): Valor da transação
            category (int): Código da categoria da transação
            description (str, optional): Descrição da transação. Defaults to "".
        """
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now()
        
    def __str__(self) -> str:
        """Gera uma string da transação.

        Returns:
            str: Descrição da transação.
        """
        return f"Transação: {self.description} R$ {self.amount:.2f} ({settings.CAT_STRING[self.category]})"
    
    def update(self, **atributes) -> None:
        """Atualiza atributos da transação.
        
        Args:
            **atributes: Keyword arguments of atributes to be updated.
        """
        for attr in atributes:
            setattr(self, attr, atributes[attr]) 
