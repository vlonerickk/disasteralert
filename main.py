from classes.localizacao import Localizacao
from classes.alerta import Alerta
from classes.desastre import Desastre
from classes.historico import Historico

def menu():
    print("\n--- MENU MONITORAMENTO DE DESASTRES ---")
    print("1. Cadastrar Desastre")
    print("2. Cadastrar Alerta")
    print("3. Listar Desastres")
    print("4. Listar Alertas")
    print("5. Calcular Distância entre Localizações")
    print("0. Sair")

def input_float(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número decimal.")

def input_nao_vazio(mensagem):
    while True:
        valor = input(mensagem).strip()
        if valor:
            return valor
        print("O valor não pode ser vazio.")

def main():
    historico = Historico()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n--- Cadastrar Desastre ---")
            tipo = input_nao_vazio("Tipo de desastre: ")
            data = input_nao_vazio("Data do desastre: ")
            cidade = input_nao_vazio("Cidade: ")
            estado = input_nao_vazio("Estado: ")
            latitude = input_float("Latitude: ")
            longitude = input_float("Longitude: ")
            severidade = input_nao_vazio("Severidade: ")

            local = Localizacao(cidade, estado, latitude, longitude)
            desastre = Desastre(tipo, data, local, severidade)
            historico.adicionar_desastre(desastre)

            print("\nDesastre cadastrado com sucesso!")

        elif opcao == "2":
            print("\n--- Cadastrar Alerta ---")
            tipo = input_nao_vazio("Tipo de alerta: ")
            mensagem = input_nao_vazio("Mensagem: ")
            nivel_risco = input_nao_vazio("Nível de risco: ")

            alerta = Alerta(tipo, mensagem, nivel_risco)
            historico.adicionar_alerta(alerta)

            print("\nAlerta cadastrado com sucesso!")

        elif opcao == "3":
            print("\n--- Lista de Desastres ---")
            if not historico.desastres:
                print("Nenhum desastre cadastrado.")
            for d in historico.listar_desastres():
                print(d)

        elif opcao == "4":
            print("\n--- Lista de Alertas ---")
            if not historico.alertas:
                print("Nenhum alerta cadastrado.")
            for a in historico.listar_alertas():
                print(a)

        elif opcao == "5":
            print("\n--- Calcular Distância ---")
            print("Informe os dados da primeira localização:")
            cidade1 = input_nao_vazio("Cidade: ")
            estado1 = input_nao_vazio("Estado: ")
            lat1 = input_float("Latitude: ")
            lon1 = input_float("Longitude: ")

            print("\nInforme os dados da segunda localização:")
            cidade2 = input_nao_vazio("Cidade: ")
            estado2 = input_nao_vazio("Estado: ")
            lat2 = input_float("Latitude: ")
            lon2 = input_float("Longitude: ")

            loc1 = Localizacao(cidade1, estado1, lat1, lon1)
            loc2 = Localizacao(cidade2, estado2, lat2, lon2)

            distancia = loc1.calcular_distancia(loc2)
            print(f"\nA distância entre {cidade1} e {cidade2} é de {distancia:.2f} km.")

        elif opcao == "0":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
