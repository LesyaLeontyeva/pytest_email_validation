import pytest

from helper_functions import valid_email, log, generate_valid_email


@pytest.mark.parametrize("email", generate_valid_email(10))
def test_validate_email_positive(email: str, log_file_name: str) -> None:
    result = valid_email(email)
    if result:
        log(log_file_name, email + ' - Correct\n')
    else:
        log(log_file_name, email + ' - Incorrect\n')
    assert result, 'Incorrect email'


@pytest.mark.parametrize("email", ['@', "test@test", "qwerty123445", '.', '@0'])
def test_validate_email_negative(email: str, log_file_name: str) -> None:
    result = valid_email(email)
    if result:
        log(log_file_name, email + ' - Correct\n')
    else:
        log(log_file_name, email + ' - Incorrect\n')
    assert not result, 'Correct email'
