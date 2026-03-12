import re


def validate_login(data):

    # username wajib
    if "username" not in data or data["username"] == "":
        return False, "Username wajib diisi"

    # password wajib
    if "password" not in data or data["password"] == "":
        return False, "Password wajib diisi"

    # panjang username
    if len(data["username"]) < 3:
        return False, "Username minimal 3 karakter"

    # panjang password
    if len(data["password"]) < 5:
        return False, "Password minimal 5 karakter"

    return True, data


def validate_create_user(data):

    # nama
    if "nama" not in data or data["nama"] == "":
        return False, "Nama wajib diisi"

    if len(data["nama"]) < 3:
        return False, "Nama minimal 3 karakter"

    # username
    if "username" not in data or data["username"] == "":
        return False, "Username wajib diisi"

    if len(data["username"]) < 3:
        return False, "Username minimal 3 karakter"

    # email
    if "email" not in data or data["email"] == "":
        return False, "Email wajib diisi"

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(pattern, data["email"]):
        return False, "Format email tidak valid"

    # password wajib
    if "password" not in data or data["password"] == "":
        return False, "Password wajib diisi"
    
    # panjang password
    if len(data["password"]) < 5:
        return False, "Password minimal 5 karakter"

    return True, data


def validate_update_user(data):

    # nama
    if "nama" not in data or data["nama"] == "":
        return False, "Nama wajib diisi"

    if len(data["nama"]) < 3:
        return False, "Nama minimal 3 karakter"

    # username
    if "username" not in data or data["username"] == "":
        return False, "Username wajib diisi"

    if len(data["username"]) < 3:
        return False, "Username minimal 3 karakter"

    # email
    if "email" not in data or data["email"] == "":
        return False, "Email wajib diisi"

    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(pattern, data["email"]):
        return False, "Format email tidak valid"

    return True, data