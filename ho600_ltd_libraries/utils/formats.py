def customize_hex_from_integer(number, base='0123456789abcdef'):
    """ convert integer to string in any base, example:
        convert int(31) with binary-string(01) will be '11111'
        convert int(31) with digit-string(0-9) will be '31'
        convert int(31) with hex-string(0-9a-f) will be '1f'
        convert int(31) with base-string(a-fg-v0-5) will be '5'
        convert int(63) with base-string(abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.,) will be ','
        convert int(16777215) with base-string(abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.,) will be ',,,,'
        convert int(16777216) with base-string(abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ.,) will be 'baaaa'
    """
    base_len = len(base)
    if number < base_len:
        return base[number]
    else:
        return customize_hex_from_integer(number//base_len, base) + base[number%base_len]