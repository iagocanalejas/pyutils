tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
external = "XYZ"
external_map = {"X": "0", "Y": "1", "Z": "2"}
numbers = "1234567890"


def is_valid_dni(dni: str) -> bool:
    """
    :return: True if the DNI is valid
    """
    if len(dni) == 9:
        dig_control = dni[8]
        dni = dni[:8]
        if dni[0] in external:
            dni = dni.replace(dni[0], external_map[dni[0]])
        return len(dni) == len([n for n in dni if n in numbers]) and tabla[int(dni) % 23] == dig_control
    return False


class DNIValidator:
    table = "TRWAGMYFPDXBNJZSQVHLCKE"
    external = "XYZ"
    external_map = {"X": "0", "Y": "1", "Z": "2"}
    numbers = "1234567890"

    def __call__(self, value: str) -> bool:
        dni = value.upper()
        return is_valid_dni(dni)
