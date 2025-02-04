Estrutura do Código
1. FSM Class
A classe FSM implementa a máquina de estados finitos. Ela possui:

Estados: 

Cada estado é representado como uma chave em um dicionário.
Transições: Transições entre estados são definidas para cada caractere.
Estado de aceitação: O estado final onde a máquina aceita a entrada.
Trap state: Um estado para transições inválidas, garantindo que caracteres não esperados sejam tratados adequadamente.
2. PatternRecognition Class
A classe PatternRecognition usa a FSM para verificar a ocorrência de uma chave de pesquisa em palavras do arquivo. Seus métodos incluem:

create_fsm: Cria a FSM para um dado caractere de pesquisa.
fsm_check: Verifica se um caractere corresponde à FSM configurada.
check_word: Verifica se uma palavra contém a chave de pesquisa.
search_in_file: Realiza a busca pela chave no arquivo de texto, conta as ocorrências e mede o tempo de execução.
3. Execução Principal
No bloco if __name__ == "__main__":, o código chama o método search_in_file com o nome de um arquivo e a chave de pesquisa desejada, exibindo os resultados da busca.

Como Usar:

Prepare o arquivo de texto: Crie um arquivo de texto chamado sample.txt (ou altere o nome do arquivo no código) contendo o texto onde você deseja realizar a busca.
Defina a chave de pesquisa: No código, defina a variável search_key com a chave que você deseja procurar.
Execute o código: Execute o script Python. Ele realizará a busca no arquivo e exibirá o número de ocorrências e o tempo de execução.
Exemplo de Execução
Se você executar o código com um arquivo de texto que contém várias instâncias da palavra "teste", você verá a saída:

nginx
Copiar
Editar
Chave 'teste' encontrada 3 vezes
Tempo de execução: 45.23 ms
Dependências
Este código não possui dependências externas além do Python 3.x.

Como Funciona:

Criação da FSM: Para cada caractere da chave de pesquisa, o código cria uma FSM que verifica se o caractere está presente nas palavras do arquivo.
Busca no Arquivo: Para cada linha no arquivo, o código divide a linha em palavras e verifica cada uma delas em busca da chave de pesquisa utilizando a FSM.
Contagem e Resultados: A cada vez que a chave é encontrada, a contagem é incrementada e o tempo de execução é calculado.
Possíveis Melhorias
Implementação de busca mais eficiente usando algoritmos como KMP ou Aho-Corasick.
Adição de suporte para buscas insensíveis a maiúsculas/minúsculas.
Licença
Este projeto é de código aberto e pode ser utilizado conforme a licença MIT License.
