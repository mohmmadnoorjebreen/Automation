from automation import __version__

def test_version():
    assert __version__ == '0.1.0'


def test_email():
    with open('assets/emails.txt', 'r') as file:
        read_email = file.read()
    expected =  True
    actual = 'shannon27@yahoo.com' in read_email
    assert expected == actual
    
def test_phone():
    with open('assets/phone_numbers.txt', 'r') as file:
        read_phone = file.read()
    expected =  True
    actual = '206-699-3626' in read_phone
    assert expected == actual    