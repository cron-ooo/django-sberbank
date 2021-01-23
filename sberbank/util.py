def system_name(card_num):
    if not card_num:
        return None

    snum = str(card_num)
    if snum.startswith("2"):
        return "MIR"
    if snum.startswith("30") or snum.startswith("36") or snum.startswith("38"):
        return "DINERSCLUB"
    if snum.startswith("31") or snum.startswith("35"):
        return "JCB"
    if snum.startswith("34") or snum.startswith("37"):
        return "AMEX"
    if snum.startswith("4"):
        return "VISA"
    if snum.startswith("50") or snum.startswith("56") or snum.startswith("57") or snum.startswith("58"):
        return "MAESTRO"
    if snum.startswith("51") or snum.startswith("52") or snum.startswith("53") or \
            snum.startswith("54") or snum.startswith("55"):
        return "MASTERCARD"
    if snum.startswith("60"):
        return "DISCOVER"
    if snum.startswith("62"):
        return "UNIONPAY"
    if snum.startswith("63") or snum.startswith("67"):
        return "MAESTRO"
    if snum.startswith("7"):
        return "UEK"
    return "UNKNOWN"
