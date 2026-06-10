def is_valid_ip(ip_address):
    fields = ip_address.split(".")
    if len(fields) != 4:
        return False
    else:
        for field in fields:
            if not field.isdigit():
                return False

            val = int(field)
            if not (val >= 0 and val <= 255):
                return False
        
    return True