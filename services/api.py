import requests
import time
def tracking(code):
    print("\x1b[2J\x1b[1;1H")
    request = requests.get('https://proxyapp.correios.com.br/v1/sro-rastro/{}'.format(code))
    address_data = request.json()
    if 'mensagem' in address_data['objetos'][0]:
        print('🔹 Mensagem: {}'.format(address_data['objetos'][0]['mensagem']))
    else:
        print("✅ Objeto rastreado\n")
        print('🔹 Código do Objeto: {}'.format(address_data['objetos'][0]['codObjeto']))
        print('🔹 Categoria de envio: {}'.format(address_data['objetos'][0]['tipoPostal']['categoria']))
        print('🔹 Descrição: {}'.format(address_data['objetos'][0]['tipoPostal']['descricao']))
        print('🔹 Sigla: {}'.format(address_data['objetos'][0]['tipoPostal']['sigla']), "\n")
        for x in address_data['objetos'][0]['eventos']:
            print("🔸 Situação:", x['descricao'])
            if 'detalhe' in x:
                print("• Detalhes:", x['detalhe'])
            if 'unidade' in x:
                if 'cidade' in x['unidade']['endereco']:
                    print("• Local:", x['unidade']['endereco']['cidade'],"/",x['unidade']['endereco']['uf'])
                elif 'nome' in x['unidade']:
                    print("• Local:", x['unidade']['nome'])
                else:
                    print("• Local:", x['unidade']['endereco'])
            if 'unidadeDestino' in x:
                if 'cidade' in x['unidadeDestino']['endereco']:
                    print("• Indo para:", x['unidadeDestino']['endereco']['cidade'],"/",x['unidadeDestino']['endereco']['uf'])
                else:
                    print("• Indo para:", x['unidadeDestino']['endereco']['uf'])
            str_date = x['dtHrCriado']
            print("• Data: " + str_date[8:10] + "/" + str_date[5:7] + "/" + str_date[0:4])
            print("• Horário: " + str_date[11:13] + ":" + str_date[14:16] + "\n")
        time.sleep(30)