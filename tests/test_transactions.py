from finances import Transaction, settings
from datetime import datetime

DEFAULT_AMOUNT = 100.0 
DEFAULT_CATEGORY = settings.CAT_CASA
DEFAULT_DESCRIPTION = "Transação de teste"

def get_transaction() -> Transaction:
    """Gera uma transação de testes com valores pré definidos.

    Returns:
        Transaction: Transação de teste
    """
    return Transaction(DEFAULT_AMOUNT, DEFAULT_CATEGORY, DEFAULT_DESCRIPTION)

def test_transaction_instance():
    """Confere se os objetos são instanciados corretamente."""
    tr = get_transaction()
    assert isinstance(tr, Transaction)

def test_transaction_attributes():
    """Confere os valores e tipos dos atributos."""
    before = datetime.now() 
    tr = get_transaction()
    # Confere os valores
    assert tr.amount == DEFAULT_AMOUNT, "O valor da transação está incorreto."
    assert tr.category == DEFAULT_CATEGORY, "O valor da categoria está incorreto."
    assert tr.description == DEFAULT_DESCRIPTION, "A descrição está incorreta."
    assert tr.date <= datetime.now(), "A data de uma transação não pode estar no futuro."
    assert tr.date >= before, "A data da transação tem que ser de agora."
    # Confere os tipos
    assert type(tr.amount) is float, "O valor da transação não é float."
    assert type(tr.category) is int, "O valor da categoria não é int."
    assert type(tr.description) is str, "A descrição não é string."
    assert type(tr.date) is datetime, "O tipo da data está incorreto."

def test_transaction_print():
    """Confere se a descrição da transação está correta"""
    tr = get_transaction()
    assert str(tr) == f"Transação: {DEFAULT_DESCRIPTION} R$ {DEFAULT_AMOUNT:.2f} ({settings.CAT_STRING[DEFAULT_CATEGORY]})"

def test_transaction_update():
    """Testa as atualizações de atributos."""
    tr = get_transaction()
    
    # Testa a atualização do amount
    tr.update(amount=200.0)
    assert tr.amount == 200.0, "Não atualizou o valor."
    
    # Testa a atualização do category
    tr.update(category=settings.CAT_EDUCACAO)
    assert tr.category == settings.CAT_EDUCACAO, "Não atualizou a categoria."
    
    # Testa a atualização do description
    tr.update(description="Nova descrição")
    assert tr.description == "Nova descrição", "Não atualizou a descrição."
    
    # Testa a atualização do date
    tr.update(date=datetime(2020, 10, 15))
    assert tr.date == datetime(2020, 10, 15), "Não atualizou a data."