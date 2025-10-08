Projeto de Zeros de Funções Reais (Métodos Numéricos)

Este é um script de Métodos Numéricos em Python que desenvolvi para encontrar raízes de funções (f(x)=0). Ele pega as tarefas de um arquivo de entrada (dados.txt), executa o método que você pediu e joga todos os resultados e a tabela de convergência em um arquivo de saída (resultados_metodos.txt).


*Como Rodar*

Crie o dados.txt: É o arquivo de entrada OBRIGATÓRIO (veja o formato abaixo).

Execute: Abra o terminal na pasta do projeto e use:

python metodos_numericos.py

Veja o resultado: O script vai gerar o arquivo resultados_metodos.txt com todas as tabelas.

*Os Métodos Implementados*
Implementei os clássicos, todos seguindo a Dupla Verificação de Parada:

Bissecção (Bissecção)

Método Iterativo Linear (MIL)

Newton-Raphson (Newton)

Secante (Secante)

Regula Falsi (Regula Falsi)


*Formato do dados.txt*
O arquivo de entrada (dados.txt) deve ter 7 colunas separadas por pipes (|). Se liga:

Método

f(x)

phi(x)

f'(x)

Chutes Iniciais (a,b ou x0,x1)

Delta (δ)

Max. Iterações

Regras de Preenchimento:
Funções (f(x), f 
′
 (x), ϕ(x)): Use x como a variável. Pode usar qualquer função do módulo math do Python (ex: math.sin(x), math.log(x), math.exp(x), x**3, etc.).

Colunas Vazias:

Para métodos que não usam ϕ(x) ou f 
′
 (x) (como Bissecção), preencha a coluna com um 0 ou x simples.

Chutes Iniciais:

Bissecção/Regula Falsi: Use a,b (ex: 1,2).

MIL/Newton: Use x0 (ex: 1.5).

Secante: Use x0,x1 (ex: 1,2).

Exemplo do dados.txt:
# Método | f(x) | phi(x) | f'(x) | Intervalo/Chutes | Delta | Max. Iterações
Bissecção| x**3 - 9*x + 3 | x | x | 0,1 | 1e-4 | 50
MIL| x**3 - 9*x + 3 | (x**3 + 3)/9 | x | 0.5 | 1e-6 | 100
Newton| math.exp(x) - 2*x - 1 | x | math.exp(x) - 2 | 1.0 | 1e-5 | 30
Secante| math.log(x) - 2 | x | x | 7.0,8.0 | 1e-3 | 20

AVISO: 
Tratamento de segurança para a entrada de dados não implementada.

Se você passar um valor de x que cause uma operação matemática inválida (tipo log(−1), divisão por zero, ou  
−4), o programa não vai avisar. Ele vai travar (crashar) com um erro padrão do Python (tipo ValueError ou ZeroDivisionError).

Moral da história: Seja responsável com seus chutes iniciais e evite domínios matemáticos proibidos, ou o script vai reclamar (e fechar). 😉

É isso aí! Se precisar de uma feature nova ou mudar algum método, só chamar. Bom trabalho!
