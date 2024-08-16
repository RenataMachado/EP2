Projeto feito para a conclusão de um exercício da disciplina MAC0110-Introdução a Computação, ministrada na Universidade De São Paulo pelo professor Nelson Lago. Neste exercício eu implementei a versão do jogo Wordle ou Termo em português e inglês, que consiste em um jogo de adivinhação de palavra. Ele está dentro das seguintes condições:
1. Perguntar ao usuário em qual língua ele deseja jogar (P/I).
2. Carregar o arquivo de texto contendo um conjunto de palavras na língua escolhida
e armazenar as palavras em uma lista.
3. Sortear uma palavra da lista.
4. Repetir, no máximo seis vezes ou até o usuário ganhar o jogo, a tarefa de solicitar
uma tentativa do usuário de descobrir a palavra sorteada e exibir o “teclado” com as
letras ainda não descartadas. A cada tentativa, o programa deverá verificar:
(a) Se a palavra corresponde à palavra sorteada; em caso afirmativo, a partida
terminou e o usuário ganhou.
(b) Se a palavra possui exatamente 5 letras e pertence à lista de palavras válidas.
Caso contrário, a tentativa é inválida e não é contada.
(c) Se a palavra contém letras certas no local certo (verdes no jogo original). Nesse
caso, indicar quais são pelo caractere ‘*’.
(d) Se a palavra contém letras certas no lugar errado (amarelas no jogo original).
Nesse caso, indicar quais são pelo caractere ‘+’.
(e) Se a palavra contém letras que não aparecem na palavra sorteada. Nesse caso,
indicar quais são pelo caractere ‘_’; essas letras deverão sumir do “teclado” na
próxima iteração.
