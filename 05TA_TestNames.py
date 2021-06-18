from names import make_full_name, \
    extract_given_name, extract_family_name
import pytest

def test_make_full_name():
    assert make_full_name("Tonatiuh", "Gonzalez") == ("Gonzalez" ";" "Tonatiuh")
    assert make_full_name("Jesus", "Del Barrio") == ("Del Barrio" ";" "Jesus")
    assert make_full_name("Nayeli", "Maya") == ("Maya" ";" "Nayeli")
    assert make_full_name("Junior", "Tovar") == ("Tovar" ";" "Junior")


pytest.main(["-v", "--tb=line", "-rN", "05TA_TestNames.py"])


def test_extract_family_name():
    assert extract_family_name("Gonzalez; Tonatiuh") == ("Gonzalez")
    assert extract_family_name("Del Barrio; Jesus") == ("Del Barrio")
    assert extract_family_name("Maya; Nayeli") == ("Maya")
    assert extract_family_name("Tovar; Junior") == ("Tovar")


pytest.main(["-v", "--tb=line", "-rN", "05TA_TestNames.py"])


def test_extract_given_name():
    assert extract_given_name("Gonzalez; Tonatiuh") == ("Tonatiuh")
    assert extract_given_name("Del Barrio; Jesus") == ("Jesus")
    assert extract_given_name("Maya; Nayeli") == ("Nayeli")
    assert extract_given_name("Tovar; Junior") == ("Junior")

pytest.main(["-v", "--tb=line", "-rN", "05TA_TestNames.py"])
