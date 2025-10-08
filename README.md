Projeto de Zeros de Funções Reais (Métodos Numéricos)

Este é um script de Métodos Numéricos em Python que desenvolvi para encontrar raízes de funções (f(x)=0). Ele pega as tarefas de um arquivo de entrada (dados.txt), executa o método que você pediu e joga os resultados em um arquivo de saída (resultados_metodos.txt).

Como Fazer Rodar (Passo a Passo)

Criar o dados.txt: Este arquivo de entrada é OBRIGATÓRIO e define todas as tarefas (veja o formato abaixo).

Executar: Abra o terminal na pasta do projeto e rode:

python metodos_numericos.py

Conferir: O script gera automaticamente o arquivo resultados_metodos.txt com todas as tabelas e a raiz final.

 Métodos Implementados
Implementamos os clássicos, todos seguindo a Dupla Verificação de Parada para garantir a convergência:

Categoria

Método

Tag no dados.txt

Por Intervalo

Bissecção

Bissecção

Por Intervalo

Regula Falsi

Regula Falsi

Ponto Fixo

Iterativo Linear (MIL)

MIL

Ponto Fixo

Newton-Raphson

Newton

Ponto Fixo

Secante

Secante


 Formato do Arquivo dados.txt (O Coração do Projeto)
O arquivo de entrada deve ter 7 colunas separadas por pipes (|). Mantenha a ordem!

Coluna

Descrição

Exemplo de Uso

Método

Nome do método (ex: Bissecção, Newton)

Bissecção

f(x)

A função principal

x**3 - 9*x + 3

phi(x)

Função de iteração (ϕ(x))

(x**3 + 3)/9

f'(x)

Derivada de f(x)

math.exp(x) - 2

Chutes Iniciais

Intervalo (a,b) ou chutes (x0 ou x0,x1)

0,1 ou 1.0

Delta (δ)

Tolerância (precisão)

1e-4

Max. Iterações

Limite de repetições

50


Exemplo do dados.txt (Tire o # para rodar!)
# Método | f(x) | phi(x) | f'(x) | Chutes Iniciais | Delta | Max. Iterações
Bissecção| x**3 - 9*x + 3 | x | x | 0,1 | 1e-4 | 50
MIL| x**3 - 9*x + 3 | (x**3 + 3)/9 | x | 0.5 | 1e-6 | 100
Newton| math.exp(x) - 2*x - 1 | x | math.exp(x) - 2 | 1.0 | 1e-5 | 30
Secante| math.log(x) - 2 | x | x | 7.0,8.0 | 1e-3 | 20

AVISO: Sem Segurança!
Tratamento de segurança para a entrada de dados não implementada.

Se você passar um valor de x que cause uma operação matemática inválida (tipo log(−1), divisão por zero, ou  
−4), o programa não vai avisar. Ele vai travar (crashar) com um erro padrão do Python (tipo ValueError ou ZeroDivisionError).

Moral da história: Seja responsável com seus chutes iniciais e evite domínios matemáticos proibidos, ou o script vai reclamar (e fechar). 😉

É isso aí! Se precisar de uma feature nova ou mudar algum método, só chamar. Bom trabalho!
