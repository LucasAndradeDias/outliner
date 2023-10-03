def numberToIp(number: str):
    # convert it to bynary
    ba = format(int(number), "08b")

    # split it in 4 bytes
    bytes = [ba[byte : byte + 8] for byte in range(0, 4)]

    final_number = ""

    for i in bytes:
        final_number = final_number + str(int(i, 2)) + "."

    # remove the last dot
    final_number = final_number[:-1]

    return final_number
