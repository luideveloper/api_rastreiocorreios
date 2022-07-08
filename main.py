import services.api

print("\x1b[2J\x1b[1;1H")
tracking_code = input("Digite o código de rastreio do objeto: ")
services.api.tracking(tracking_code)