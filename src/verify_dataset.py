def check_col ( dataframe, target_collum):
    if dataframe[target_collum].isnull:
        print(f"Acoluna está vazia")
    else:
        print(f"A coluna não possui elemtnos vazisos")