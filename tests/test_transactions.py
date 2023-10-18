from finances import Transaction

DEFAULT_AMOUNT = 100.0 
DEFAULT_CATEGORY = 1
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
    tr = get_transaction()
    # Confere os valores
    assert tr.amount == DEFAULT_AMOUNT, "O valor da transação está incorreto."
    assert tr.category == DEFAULT_CATEGORY, "O valor da categoria está incorreto."
    assert tr.description == DEFAULT_DESCRIPTION, "A descrição está incorreta."
    # Confere os tipos
    assert type(tr.amount) is float, "O valor da transação não é float."
    assert type(tr.category) is int, "O valor da categoria não é int."
    assert type(tr.description) is str, "A descrição não é string."
