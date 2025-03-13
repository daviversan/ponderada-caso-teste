# ponderada-caso-teste
## Descrição:
&emsp;A proposta dessa atividade é criar um código que automatize um caso de teste de software relacionado ao projeto do módulo 5 de Engenharia de Software. A seguir estão descritos os critérios solicitados pela ponderada:

## Objetivo
&emsp;O objetivo deste caso de teste é verificar se os inputs inseridos na função `nome_valido` correspondem apenas a caracteres válidos, que se restringem a letras ou letras com espaços entre si. Esse caso de teste se relaciona com o projeto pois iremos implementar uma feature em que o usuário deverá inserir o nome de um profissional para cadastrá-lo no sistema, e portanto, faz-se necessário uma verificação para que o nome esteja conforme os padrões aceitos (caracteres alfabéticos)

## Pré-condição
&emsp;As seguintes pré-configurações devem ser feitas para que os testes possam ser efetuados:
- Ambiente Python instalado
- Arquivo Python para função criado (`app.py`)
- Função nome_valido definida em `app.py`
- Arquivo de testes criado (`tests.py`)
- Importação da biblioteca `unittest`

&emsp;Em seguida, espera-se as seguintes entradas para a função:

### 1. Entrada: Nome não nulo 
A função `nome_valido()` espera uma entrada do tipo `str`. A entrada não pode ser `None` (valor nulo). Caso contrário, o comportamento da função seria indefinido.

### 2. Entrada: Nome do tipo `str`
A função assume que o parâmetro passado é uma string (str). Isso significa que qualquer outra entrada (como números, listas ou dicionários) deve ser evitada, ou um erro será gerado, já que a função foi escrita para lidar com strings.

### 3. Entrada: O nome pode ter espaços
A função espera que o nome possa ter espaços entre palavras, como em "Carlos Silva", mas, para ser válido, ele não pode ser composto apenas por espaços ou conter caracteres não alfanuméricos.

## Procedimento de teste:
Dentro da classe de teste (`TestNomeValido`), foram criados métodos para verificar os diferentes cenários mencionados. Cada método de teste possui uma asserção para validar se a função se comporta da maneira esperada.

### `test_nome_apenas_letras:`

- Este teste verifica se o nome composto apenas por letras é aceito como válido.
- Objetivo: Verificar que nomes como "Carlos" retornem True.
- A asserção `self.assertTrue(nome_valido("Carlos"))` verifica se o retorno da função é True.
  
### `test_nome_com_espaco:`


- Este teste verifica se um nome com espaço entre as palavras é aceito.
- Objetivo: Verificar que nomes como "Carlos Silva" retornem True.
- A asserção `self.assertTrue(nome_valido("Carlos Silva"))` verifica se o nome com espaços entre palavras é válido.
  
### `test_nome_letras_espacos`:


- Este teste verifica se o nome com múltiplos espaços entre as palavras é aceito.
- Objetivo: Verificar que nomes como "Carlos Silva Junior" retornem True.
- A asserção `self.assertTrue(nome_valido("Carlos Silva Junior"))` valida que nomes compostos por letras e espaços são válidos.
  
### `test_nome_com_numeros`:


- Este teste verifica se a função rejeita nomes com números.
- Objetivo: Verificar que nomes como "Carlos123" retornem False.
- A asserção `self.assertFalse(nome_valido("Carlos123"))` valida que números são rejeitados.

### `test_nome_com_caracteres_especiais`:


- Este teste verifica se a função rejeita caracteres especiais.
- Objetivo: Verificar que nomes como "Carlos@Silva" retornem False.
- A asserção `self.assertFalse(nome_valido("Carlos@Silva"))` valida que caracteres especiais são rejeitados.

### `test_nome_vazio`:


- Este teste verifica se um nome vazio é rejeitado.
- Objetivo: Verificar que uma string vazia como "" retorne False.
- A asserção `self.assertFalse(nome_valido(""))` valida que um nome vazio seja inválido.

### `test_nome_apenas_espacos`:


- Este teste verifica se um nome composto apenas por espaços é rejeitado.
- Objetivo: Verificar que um nome como " " (apenas espaços) retorne False.
- A asserção `self.assertFalse(nome_valido(" "))` valida que nomes com apenas espaços são inválidos.


&emsp;Por fim,  comando `unittest.main()` no final do código inicia os testes. Isso permite que o Python execute automaticamente todos os métodos que começam com `test_` dentro da classe de teste. Ao rodar o script, o framework unittest executa cada teste e gera um relatório mostrando se os testes passaram ou falharam.

## Resultado esperado
&emsp;Cada caso de teste deve retornar um valor booleano definido, como descrito na etapa de procedimento:
- `test_nome_apenas_letra` retorna TRUE
- `test_nome_com_espaco` retorna TRUE
- `test_nome_letras_espacos` retorna TRUE
- `test_nome_com_numero` retorna FALSE
- `test_nome_com_caracteres_especiais` retorna FALSE
- `test_nome_vazio` retorna FALSE

## Resultado obtido
&emsp;Os resultados obtidos condizem com o que foi planejado para cada caso esperado:
<img>

## Pós-condição
### 1. Se o nome contiver apenas letras e espaços:

- O retorno da função deve ser True.
- O nome não pode conter caracteres não alfanuméricos ou espaços extras no início ou fim, e não deve estar vazio.
  
### 2. Se o nome contiver números:

- O retorno da função deve ser False, já que números não são permitidos.

### 3. Se o nome contiver caracteres especiais:

- O retorno da função deve ser False, pois caracteres especiais não são permitidos.
  
### 4. Se o nome for vazio ou composto apenas por espaços:

- O retorno da função deve ser False, pois não queremos aceitar nomes vazios ou apenas espaços.


