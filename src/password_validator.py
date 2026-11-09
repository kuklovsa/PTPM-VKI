def validate_password (password):
    schars = "!@#$%^&*"
    if type(password) != str:
        raise TypeError("Пароль должен быть строкой")
    if " " in password:
        raise ValueError("Пароль не должен содержать пробелы")
    if len(password) > 7 and len(password) < 21:
        if any(char.isupper() for char in password):
            if any(char.islower() for char in password):
                if any(char.isdigit() for char in password):
                    if any(char in schars for char in password):
                        return True
    return False