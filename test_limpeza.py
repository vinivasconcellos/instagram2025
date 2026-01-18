from limpeza_dados import converter_k

def converter_k_com_nada():
    assert converter_k("") == 0

def test_converter_k_com_traco():
    assert converter_k("-") == 0