"""
   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
"""

_10xxxxxx = 0b10000000
_110xxxxx = 0b11000000
_1110xxxx = 0b11100000
_11110xxx = 0b11110000


def decode_rune(b: bytes) -> (int, int):
    if len(b) == 0:
        raise ValueError("empty bytes.")

    b0: int = b[0]

    if b0 < 128:
        return b0, 1
    elif b0 & _1110xxxx == _110xxxxx:
        if len(b) < 2 or not (b[1] & _110xxxxx == _10xxxxxx):
            raise ValueError("invalid 2 bytes.")
        b1: int = b[1]
        bu: int = ((b0 & 0b00011111) << 6) | (b1 & 0b00111111)
        if bu < _10xxxxxx:
            raise ValueError("overlong.")
        return bu, 2
    elif b0 & _11110xxx == _1110xxxx:
        if len(b) < 3:
            raise ValueError("invalid 3 bytes.")
        b1, b2 = b[1], b[2]
        if not (b1 & _110xxxxx == _10xxxxxx) or not (b2 & _110xxxxx == _10xxxxxx):
            raise ValueError("invalid 3 bytes.")
        bu: int = (
            ((b0 & 0b00001111) << 12) | ((b1 & 0b00111111) << 6) | (b2 & 0b00111111)
        )
        if bu < 0b100000000000:
            raise ValueError("overlong.")
        return bu, 3
    elif b0 & 0b11111000 == _11110xxx:
        if len(b) < 4:
            raise ValueError("invalid 4 bytes.")
        b1, b2, b3 = b[1], b[2], b[3]
        if (
            not (b1 & _110xxxxx == _10xxxxxx)
            or not (b2 & _110xxxxx == _10xxxxxx)
            or not (b3 & _110xxxxx == _10xxxxxx)
        ):
            raise ValueError("invalid 4 bytes.")
        bu: int = (
            ((b0 & 0b00000111) << 18)
            | ((b1 & 0b00111111) << 12)
            | ((b2 & 0b00111111) << 6)
            | (b3 & 0b00111111)
        )
        if bu < 0b10000000000000000:
            raise ValueError("overlong.")

        return bu, 4
    else:
        raise ValueError("invalid.")


def encode_rune(code_point: int) -> bytes:
    if code_point < 0 or code_point > 0b100001111111111111111:
        raise ValueError("invalid.")

    #  1 byte (ASCII)
    if code_point <= 0b1111111:
        return bytes([code_point])

    #  2 bytes
    elif code_point <= 0b11111111111:
        return bytes(
            [_110xxxxx | (code_point >> 6), _10xxxxxx | (code_point & 0b00111111)]
        )

    #  3 bytes
    elif code_point <= 0b1111111111111111:
        return bytes(
            [
                _1110xxxx | (code_point >> 12),
                _10xxxxxx | ((code_point >> 6) & 0b00111111),
                _10xxxxxx | (code_point & 0b00111111),
            ]
        )

    #  4 bytes
    else:
        return bytes(
            [
                _11110xxx | (code_point >> 18),
                0b10000000 | ((code_point >> 12) & 0b00111111),
                0b10000000 | ((code_point >> 6) & 0b00111111),
                0b10000000 | (code_point & 0b00111111),
            ]
        )
