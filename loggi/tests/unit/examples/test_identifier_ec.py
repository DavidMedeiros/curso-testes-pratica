from examples.identifier import Identifier

def test_case_01():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('ab')

    assert is_valid is True

def test_case_02():
    identifier = Identifier()

    is_invalid = identifier.validate_identifier('abcdefghij')

    assert is_invalid is False

def test_case_03():
    identifier = Identifier()

    is_invalid = identifier.validate_identifier('1ab')

    assert is_invalid is False
    
def test_case_04():
    identifier = Identifier()

    is_invalid = identifier.validate_identifier('')

    assert is_invalid is False

def test_case_05():
    identifier = Identifier()

    is_invalid = identifier.validate_identifier('açaí')    

    assert is_invalid is False

def test_case_06():
    identifier = Identifier()

    is_valid = identifier.validate_identifier('a')

    assert is_valid is True    

