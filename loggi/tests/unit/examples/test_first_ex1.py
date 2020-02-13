from base.utils.phone import format_phone_number
import pytest

@pytest.mark.parametrize(
    'phone_number', 'expected_formatted_phone',
    [
        pytest.param('11988776655', '(11) 98877-6655', id='CT1')
    ]
)

def test_valid_cases(phone_number, expected_formatted_phone):
    formatted_phone = format_phone_number(phone_number)

    assert formatted_phone == expected_formatted_phone