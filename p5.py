def reverte_string(s):
    nova_string = ""
    for i in range(len(s) - 1, -1, -1):  # itera de trás para frente
        nova_string += s[i]
    return nova_string


def test_reverte_string():
    assert reverte_string("bom dia") == "aid mob"
    assert reverte_string("ola") == "alo"
    assert reverte_string("mundo") == "odnum"
    assert reverte_string("python") == "nohtyp"
    assert reverte_string("banana") == "ananab"
    assert reverte_string("abacaxi") == "ixacaba"


if __name__ == "__main__":
    test_reverte_string()
    print("p5.py: Todos os testes passaram")
