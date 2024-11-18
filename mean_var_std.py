import numpy as np

def calculate(input_list):
    # Verifica che la lista abbia esattamente 9 elementi
    if len(input_list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Converte la lista in un array NumPy 3x3
    matrix = np.array(input_list).reshape(3, 3)
    
    # Calcola le statistiche richieste
    mean = [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()]
    variance = [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()]
    std_dev = [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()]
    max_val = [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()]
    min_val = [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()]
    total = [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
    
    # Restituisce il dizionario con i risultati
    return {
        'mean': mean,
        'variance': variance,
        'standard deviation': std_dev,
        'max': max_val,
        'min': min_val,
        'sum': total
    }
