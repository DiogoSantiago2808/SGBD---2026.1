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
    insert_keys = [
        (18, "R18"), (22, "R22"), (27, "R27"), (35, "R35"),
        (41, "R41"), (44, "R44"), (63, "R63"), (67, "R67"),
        (83, "R83"), (86, "R86"), (121, "R121"), (145, "R145")
    ]

    for key in insert_keys:
        chave = key[0]
        print(f"Inserindo {key}...")
        isam.insert(chave)

    print("\n📌 Estrutura após inserções:")
    isam.print_structure()

    
    print("\n📌 Remoções:")
    remove_keys = [27, 44, 67, 83, 145]

    for key in remove_keys:
        print(f"Removendo {key}...")
        isam.delete(key)

    print("\n📌 Estrutura após remoções:")
    isam.print_structure()

  
    print("\n📌 Busca por igualdade:")

    key_search = [22, 35, 44, 90]
    for key in key_search:
        leaf, path = isam.find_leaf(key)

        print(f"\n--- Analisando Busca({key}) ---")
        print("Caminho percorrido nos índices:")
        
        for node in path:
            print(f" -> Nó: {node.keys}")

        result = isam.search(key)
        print(f"Encontrado: {'Sim' if result else 'Não'}")

        custo = isam.metrics[-1] if isam.metrics else 0
        print(f"Custo total da busca: {custo} nós/páginas")

    print("\n📌 Busca por intervalo:")
    intervalos = [(20, 50), (60, 90), (120, 150)]

    for start, end in intervalos:
        leaf, path = isam.find_leaf(start)

        print(f"\n--- Analisando Intervalo({start} até {end}) ---")
        print("Caminho percorrido até o início do intervalo:")
        
        for node in path:
            print(f" -> Nó: {node.keys}")

        result = isam.range_search(start, end)
        
        print(f"Registros encontrados: {result}")
        print(f"Total de registros: {len(result)}")

        custo = isam.metrics[-1] if isam.metrics else 0
        print(f"Custo total da busca por intervalo: {custo} nós/páginas")

    result = isam.range_search(start, end)
    print("Resultado:", result)
    custo = isam.metrics[-1] if isam.metrics else 0
    print(f"Intervalo({start}, {end}): {len(result)} registros | Custo: {custo} nós")

    print("\n📌 Estrutura todas as operações:")
    isam.print_structure()

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