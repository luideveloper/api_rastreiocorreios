import services.api
i = 1
while i == 1:
    print("\x1b[2J\x1b[1;1H")
    tracking_code = input("> Digite o código de rastreio do objeto: ")
    services.api.tracking(tracking_code)