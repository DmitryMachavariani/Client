import os

if os.path.isfile('autologin'):
    autologin = open('autologin', 'r')
    data = autologin.readlines()

    username = data[0].strip()
    password = data[1].strip()

    autologin.close()

    import package

    result = package.buildpackage("login", [username, password])

    if result == "Успешно вошли":
        import forms.chat
    else:
        import forms.login
else:
    import forms.login