from examples.identifier import Identifier

import pytest

@pytest.fixture(scope='module')
def obj_identifier():
    return Identifier()

@pytest.mark.parametrize(
    'identif',
    [
        pytest.param('a', id='CT2'),
        pytest.param('ab'),
        pytest.param('abcde'),
        pytest.param('abcdef'),
        pytest.param('a1'),
    ]
)

def test_all_valid_cases(obj_identifier, identif):
    identifier = obj_identifier

    is_valid = identifier.validate_identifier(identif)

    assert is_valid is True