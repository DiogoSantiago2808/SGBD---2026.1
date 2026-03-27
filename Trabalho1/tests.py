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

    for key in [10, 23, 35, 41, 60]:
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

    for key in [23, 48, 41, 42]:
        print(f"\nInserindo {key}...")
        isam.insert(key)

    isam.print_structure()


def test_overflow():
    print("\n=== TESTE 4: Overflow ===")

    isam = ISAM()
    isam.build_initial_structure()

    for key in [48, 41, 42, 43, 44, 45]:
        print(f"Inserindo {key}...")
        isam.insert(key)

    isam.print_structure()


def test_search():
    print("\n=== TESTE 5: Busca ===")

    isam = ISAM()
    isam.build_initial_structure()

    for key in [23, 48, 41, 42]:
        isam.insert(key)

    for key in [23, 41, 99]:
        print(f"\nBuscando {key}...")
        print("Resultado:", isam.search(key))


def test_range_search():
    print("\n=== TESTE 6: Intervalo ===")

    isam = ISAM()
    isam.build_initial_structure()

    for key in [23, 48, 41, 42]:
        isam.insert(key)

    print("Resultado:", isam.range_search(20, 50))


def test_delete():
    print("\n=== TESTE 7: Remoção ===")

    isam = ISAM()
    isam.build_initial_structure()

    for key in [23, 48, 41, 42]:
        isam.insert(key)

    for key in [23, 41]:
        print(f"Removendo {key}")
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


def test_simulacao_experimental():
    print("\n=== SIMULAÇÃO EXPERIMENTAL (OFICIAL) ===")

    isam = ISAM()
    isam.build_initial_structure()


    print("\n📌 Estrutura inicial:")
    isam.print_structure()

   
    print("\n📌 Inserções obrigatórias:")
    insert_keys = [23, 48, 41, 42]

    for key in insert_keys:
        print(f"Inserindo {key}...")
        isam.insert(key)

    print("\n📌 Estrutura após inserções:")
    isam.print_structure()

    
    print("\n📌 Remoções:")
    remove_keys = [23, 41]

    for key in remove_keys:
        print(f"Removendo {key}...")
        isam.delete(key)

    print("\n📌 Estrutura após remoções:")
    isam.print_structure()

  
    print("\n📌 Busca por igualdade:")

    key = 42
    leaf, path = isam.find_leaf(key)

    print(f"\nBuscando {key}...")
    print("Caminho percorrido:")
    for node in path:
        print(node.keys)

    result = isam.search(key)
    print("Encontrado:", result)

   
    print("\n📌 Busca por intervalo:")

    start, end = 20, 50
    leaf, path = isam.find_leaf(start)

    print(f"\nIntervalo {start} até {end}")
    print("Caminho inicial:")
    for node in path:
        print(node.keys)

    result = isam.range_search(start, end)
    print("Resultado:", result)

  
    print("\n📌 Métricas:")
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

    
    test_simulacao_experimental()

    print("\n=========== FIM DOS TESTES ===========")