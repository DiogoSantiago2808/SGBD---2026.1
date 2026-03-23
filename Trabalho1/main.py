from isam import ISAM
from testes import run_all_tests

def main():
    isam = ISAM()

    # Estrutura fixa obrigatória
    isam.build_initial_structure()

    # Inserções do enunciado
    isam.insert(23)
    isam.insert(48)
    isam.insert(41)
    isam.insert(42)

    # Remoções (definir depois)
    isam.delete(23)

    # Buscas
    isam.search(41)
    isam.range_search(20, 50)

    # Visualização
    isam.print_structure()
    isam.show_metrics()


if __name__ == "__main__":
    run_all_tests()