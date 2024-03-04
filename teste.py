def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def sort_array(arr, reverse=False):
    arr_copy = arr[:]
    if reverse:
        arr_copy.sort(reverse=True)
    else:
        selection_sort(arr_copy)
    return arr_copy

def find_max_min(arr):
    max_element = arr[0]
    min_element = arr[0]
    for num in arr:
        if num > max_element:
            max_element = num
        elif num < min_element:
            min_element = num
    return max_element, min_element

def second_smallest(arr):
    unique_sorted = sorted(set(arr))
    return unique_sorted[1]

def remove_duplicates(arr):
    return list(set(arr))

def count_even_odd(arr):
    arr.sort(reverse=True)
    even_count = sum(1 for num in arr if num % 2 == 0)
    odd_count = len(arr) - even_count
    return even_count, odd_count

def third_largest(arr):
    unique_sorted = sorted(set(arr), reverse=True)
    return unique_sorted[2]

def median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 != 0:
        return arr[n // 2]
    else:
        mid_right = arr[n // 2]
        mid_left = arr[n // 2 - 1]
        return (mid_left + mid_right) / 2

if __name__ == "__main__":
    vetor = [4, 2, 7, 1, 9, 3, 6, 5, 8]
    
    # Questão 1
    selection_sort(vetor)
    print("Questão 1 - Vetor Ordenado (Seleção):", vetor)
    
    # Questão 2
    print("Questão 2 - Vetor Ordenado (Chave Decrescente):", sort_array(vetor, reverse=True))
    
    # Questão 3
    max_element, min_element = find_max_min(vetor)
    print("Questão 3 - Máximo e Mínimo:", max_element, min_element)
    
    # Questão 4
    print("Questão 4 - Segundo Menor Elemento:", second_smallest(vetor))
    
    # Questão 5
    print("Questão 5 - Remover Duplicatas:", remove_duplicates(vetor))
    
    # Questão 6
    even_count, odd_count = count_even_odd(vetor)
    print("Questão 6 - Números Pares e Ímpares:", even_count, odd_count)
    
    # Questão 7
    print("Questão 7 - Terceiro Maior Elemento:", third_largest(vetor))
    
    # Questão 8
    print("Questão 8 - Mediana:", median(vetor))
