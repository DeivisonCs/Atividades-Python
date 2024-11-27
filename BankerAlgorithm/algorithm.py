# Verifica se o estado do sistema é seguro.

#  available: Lista de recursos disponíveis.
#  max_need: Matriz de máximos necessários de recursos por processo.
#  allocation: Matriz de recursos já alocados por processo.
# Booleano indicando se o estado é seguro.
def is_safe_state(available, max_need, allocation):
    n_processes = len(max_need)
    n_resources = len(available)

    work = available[:]
    finish = [False] * n_processes

    while True:
        found_process = False

        for i in range(n_processes):
            if not finish[i] and all(max_need[i][j] - allocation[i][j] <= work[j] for j in range(n_resources)):
                # Simula a liberação de recursos pelo processo i
                for j in range(n_resources):
                    work[j] += allocation[i][j]

                finish[i] = True
                found_process = True
                break

        if not found_process:
            break

    return all(finish)  


# Tenta alocar recursos para um processo baseado no pedido.
# process_id: ID do processo que solicita recursos.
# request: Lista de recursos solicitados pelo processo.
# available: Lista de recursos disponíveis.
# max_need: Matriz de máximos necessários de recursos por processo.
# allocation: Matriz de recursos já alocados por processo.
def request_resources(process_id, request, available, max_need, allocation):
    n_resources = len(available)

    # Verifica se o pedido excede o máximo necessário do processo
    if any(request[j] > max_need[process_id][j] - allocation[process_id][j] for j in range(n_resources)):
        print("Erro: O processo pediu mais do que o necessário.")
        return False

    # Verifica se o pedido pode ser atendido com os recursos disponíveis
    if any(request[j] > available[j] for j in range(n_resources)):
        print("Recursos insuficientes disponíveis para atender ao pedido.")
        return False

    # Alocação tentada (simulação)
    for j in range(n_resources):
        available[j] -= request[j]
        allocation[process_id][j] += request[j]

    # Verifica se o estado resultante é seguro
    if is_safe_state(available, max_need, allocation):
        print("Pedido atendido com sucesso.")
        return True

    # Reverte a alocação se o estado não for seguro
    for j in range(n_resources):
        available[j] += request[j]
        allocation[process_id][j] -= request[j]

    print("Pedido negado para evitar deadlock.")
    return False


# ----------------------- Exemplo de uso -----------------------

available = [3, 3, 2]  # Recursos disponíveis
max_need = [  # Máximo necessário por processo
    [7, 5, 3],
    [3, 2, 2],
    [9, 0, 2],
    [2, 2, 2],
    [4, 3, 3]
]
allocation = [  # Recursos já alocados por processo
    [0, 1, 0],
    [2, 0, 0],
    [3, 0, 2],
    [2, 1, 1],
    [0, 0, 2]
]

# Exemplo de solicitação de recursos pelo processo 1
process_id = 0
request = [1, 0, 2]

request_resources(process_id, request, available, max_need, allocation)
