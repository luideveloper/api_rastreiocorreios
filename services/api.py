import requests

def tracking(code):
    print ("\n" * 130) 
    request = requests.get('https://proxyapp.correios.com.br/v1/sro-rastro/{}'.format(code))
    address_data = request.json()
    
    if 'mensagem' in address_data['objetos'][0]:
        print("\n❌ Objeto inválido\n")
    else:
        print("✅ Objeto rastreado\n")
        print('🔹 Código do Objeto: {}'.format(address_data['objetos'][0]['codObjeto']))
        print('🔹 Categoria de envio: {}'.format(address_data['objetos'][0]['tipoPostal']['categoria']), "\n")
        for x in address_data['objetos'][0]['eventos']:
            print("🔸 Situação: ", x['descricao'])
            print("• Local: ", x['unidade']['endereco']['cidade'], " - ", x['unidade']['endereco']['uf'])
            str_date = x['dtHrCriado']
            print("• Data: " + str_date[8:10] + "/" + str_date[5:7] + "/" + str_date[0:4])
            print("• Horário: " + str_date[11:13] + ":" + str_date[14:16] + "\n")