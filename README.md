# PASSWORD-GENERATOR
Este código Python gera senhas aleatórias com base nos critérios especificados pelo usuário.

FUNCIONAMENTO:

O código gera uma senha aleatória com base nos seguintes critérios:
- A senha deve ter um comprimento entre 8 e 20 caracteres.
- Deve conter uma combinação de letras minúsculas, letras maiúsculas, números e caracteres especiais.

O usuário é solicitado a fornecer o comprimento desejado da senha. Em seguida, a função `generate_password` é chamada para criar a senha.

PARÂMETROS:

- length (int): O comprimento desejado da senha. Deve estar entre 8 e 20 caracteres.

- Porcentagem de caracteres:
    - 50% caracteres especiais
    - 30% letras (15% minúsculas e 15% maiúsculas)
    - 20% números

FUNÇÕES:

1. generate_password(length)
    - Descrição: Gera uma senha aleatória com base no comprimento especificado e na distribuição de caracteres.
    - Parâmetros:
        - length (int): O comprimento desejado da senha.
    - Retorna:
        - str: A senha gerada.
    - Exceções:
        - ValueError: Se o comprimento estiver fora da faixa especificada.

COMO USAR:

1. Execute o código em um ambiente Python.
2. Quando solicitado, insira o comprimento desejado da senha.
3. O código gerará e imprimirá a senha aleatória.
