def destruir_petecas(num_petecas, num_amigos = 3):
    return num_petecas % num_amigos
  
print(
    destruir_petecas(91),
    destruir_petecas(91,7),
    destruir_petecas(91,7),
)