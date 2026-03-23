from isam import ISAM


def test_structure():
    print("\n=== TESTE 1: Estrutura Inicial ===")

    isam = ISAM()
    isam.build_initial_structure()

    isam.print_structure()


def test_find_leaf():
    print("\n=== TESTE 2: Navegação (find_leaf) ===")

    isam = ISAM()
    isam.build_initial_structure()

    keys_to_test = [10, 23, 35, 41, 60]

    for key in keys_to_test:
        leaf, path = isam.find_leaf(key)

        print(f"\nChave: {key}")
        print("Caminho:")
        for node in path:
            print(node.keys)

        print("Folha final:", leaf.records)


def test_insert():
    print("\n=== TESTE 3: Inserção ===")

    isam = ISAM()
    isam.build_initial_structure()

    insert_keys = [23, 48, 41, 42]

    for key in insert_keys:
        print(f"\nInserindo {key}...")
        isam.insert(key)

    isam.print_structure()


def test_overflow():
    print("\n=== TESTE 4: Overflow ===")

    isam = ISAM()
    isam.build_initial_structure()

    keys = [48, 41, 42, 43, 44, 45]

    for key in keys:
        print(f"Inserindo {key}...")
        isam.insert(key)

    isam.print_structure()


def test_search():
    print("\n=== TESTE 5: Busca ===")

    isam = ISAM()
    isam.build_initial_structure()

    # prepara dados
    for key in [23, 48, 41, 42]:
        isam.insert(key)

    search_keys = [23, 41, 99]

    for key in search_keys:
        print(f"\nBuscando {key}...")
        result = isam.search(key)
        print("Resultado:", result)


def test_range_search():
    print("\n=== TESTE 6: Busca por Intervalo ===")

    isam = ISAM()
    isam.build_initial_structure()

    for key in [23, 48, 41, 42]:
        isam.insert(key)

    start, end = 20, 50
    print(f"\nIntervalo: {start} até {end}")

    result = isam.range_search(start, end)
    print("Resultado:", result)


def test_delete():
    print("\n=== TESTE 7: Remoção ===")

    isam = ISAM()
    isam.build_initial_structure()

    for key in [23, 48, 41, 42]:
        isam.insert(key)

    delete_keys = [23, 41]

    for key in delete_keys:
        print(f"\nRemovendo {key}...")
        isam.delete(key)

    isam.print_structure()


def test_metrics():
    print("\n=== TESTE 8: Métricas ===")

    isam = ISAM()
    isam.build_initial_structure()

    for key in [23, 48, 41, 42]:
        isam.insert(key)

    isam.search(41)
    isam.range_search(20, 50)

    isam.show_metrics()


def run_all_tests():
    print("\n=========== INICIANDO TESTES ISAM ===========")

    test_structure()
    test_find_leaf()
    test_insert()
    test_overflow()
    test_search()
    test_range_search()
    test_delete()
    test_metrics()

    print("\n=========== FIM DOS TESTES ===========\n")


if __name__ == "__main__":
    run_all_tests()