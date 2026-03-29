from isam import ISAM
from tests import run_all_tests
from tests import test_simulacao_experimental


def menu():
    print("\n========= MENU ISAM =========")
    print("1 - Inserir chave")
    print("2 - Remover chave")
    print("3 - Buscar chave")
    print("4 - Buscar intervalo")
    print("5 - Mostrar árvore")
    print("6 - Mostrar métricas")
    print("7 - Rodar testes completos")
    print("8 - Rodar simulação experimental")
    print("0 - Sair")
    print("=============================")


def main():
    isam = ISAM()
    isam.build_initial_structure()

    print("\nEstrutura inicial carregada!")
    isam.print_structure()

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                key = int(input("Digite a chave: "))
                isam.insert(key)
                print(f"Chave {key} inserida.")
                isam.print_structure()
            except:
                print("Entrada inválida.")

        elif opcao == "2":
            try:
                key = int(input("Digite a chave: "))
                isam.delete(key)
                print(f"Chave {key} removida.")
                isam.print_structure()
            except:
                print("Entrada inválida.")

        elif opcao == "3":
            try:
                key = int(input("Digite a chave: "))
                result = isam.search(key)
                print("Resultado:", result)
            except:
                print("Entrada inválida.")

        elif opcao == "4":
            try:
                start = int(input("Início: "))
                end = int(input("Fim: "))
                result = isam.range_search(start, end)
                print("Resultado:", result)
            except:
                print("Entrada inválida.")

        elif opcao == "5":
            isam.print_structure()

        elif opcao == "6":
            isam.show_metrics()

        elif opcao == "7":
            run_all_tests()

        elif opcao == "8":
            test_simulacao_experimental()

        elif opcao == "0":
            print("Encerrando...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()