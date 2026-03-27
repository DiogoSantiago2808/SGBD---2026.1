from tests import run_all_tests
from isam import ISAM


def main():
    isam = ISAM()

    
    isam.build_initial_structure()

    
    isam.insert(23)
    isam.insert(48)
    isam.insert(41)
    isam.insert(42)

   
    isam.delete(23)

    
    print("Busca 41:", isam.search(41))
    print("Intervalo 20-50:", isam.range_search(20, 50))

   
    isam.print_structure()
    isam.show_metrics()


if __name__ == "__main__":

    print("\nEscolha o modo:")
    print("1 - Rodar TODOS os testes")
    print("2 - Rodar execução simples")

    opcao = input("Digite 1 ou 2: ")

    if opcao == "1":
        run_all_tests()
    elif opcao == "2":
        main()
    else:
        print("Opção inválida")