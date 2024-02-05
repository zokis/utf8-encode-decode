import pytest
from utf8 import decode_rune, encode_rune


# 1 byte (ASCII)
def test_decode_ascii_character():
    assert decode_rune(b"A") == (65, 1)


# 2 bytes
def test_decode_2_byte_character():
    # 'ñ' is b'\xc3\xb1'
    assert decode_rune(b"\xc3\xb1") == (241, 2)


# 3 bytes
def test_decode_3_byte_character():
    # '€' is b'\xe2\x82\xac'
    assert decode_rune(b"\xe2\x82\xac") == (8364, 3)


# 4 bytes
def test_decode_4_byte_character():
    # '😊' is b'\xf0\x9f\x98\x8a'
    assert decode_rune(b"\xf0\x9f\x98\x8a") == (128522, 4)


def test_decode_empty_input():
    with pytest.raises(ValueError):
        decode_rune(b"")


def test_decode_incomplete_sequence():
    with pytest.raises(ValueError):
        decode_rune(b"\xe2\x82")  # incomplete sequence for '€'


# invalid byte
def test_invalid_start_byte():
    with pytest.raises(ValueError):
        decode_rune(b"\xf8\xa1\xa1\xa1")


def test_invalid_subsequent_byte():
    with pytest.raises(ValueError):
        decode_rune(b"\xc3\x28")  # second byte != 0b10xxxxxx


def test_overlong_3_byte_sequence():
    with pytest.raises(ValueError):
        #  "A" (U+0041)
        decode_rune(b"\xe0\x82\x81")


def test_encode_ascii_character():
    # ASCII 'A'
    assert encode_rune(65) == b"A"


def test_encode_2_byte_character():
    # 'ñ' Unicode U+00F1
    assert encode_rune(0x00F1) == b"\xc3\xb1"


def test_encode_3_byte_character():
    # Euro sign '€' Unicode U+20AC
    assert encode_rune(0x20AC) == b"\xe2\x82\xac"


def test_encode_4_byte_character():
    # Smiley '😊' Unicode U+1F60A
    assert encode_rune(0x1F60A) == b"\xf0\x9f\x98\x8a"


def test_encode_4_byte_character_2():
    # Smiley '😊' Unicode U+1F60A
    assert encode_rune(0x1F60A).decode("utf8") == "😊"
