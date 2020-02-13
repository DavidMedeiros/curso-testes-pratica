from examples.identifier import Identifier

def test_case_01():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('')

    assert is_valid is False

def test_case_02():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('a')    

    assert is_valid is True

def test_case_03():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('ab')    

    assert is_valid is True    

def test_case_04():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('abcde')    

    assert is_valid is True

def test_case_05():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('abcdef')    

    assert is_valid is True    

def test_case_06():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('abcdefg')    

    assert is_valid is False    

def test_case_07():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('1a')    

    assert is_valid is False

def test_case_08():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('a1')    

    assert is_valid is True

def test_case_09():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('açaí')    

    assert is_valid is False            