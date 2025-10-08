import math
import sys

FUNCOES_MATEMATICAS = { 
    'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 
    'exp': math.exp, 'log': math.log, 'sqrt': math.sqrt, 
    'math': math 
}
METODOS_NUMERICOS = {} 

def validar_funcao(f_str, x): 
    dic_eval = {'x': x} 
    dic_eval.update(FUNCOES_MATEMATICAS) 
    return eval(f_str, {"__builtins__": None}, dic_eval) 


def ler_dados_entrada(arquivo_entrada):
    tarefas = [] 
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as dados:
            for linha in dados:
                linha = linha.strip()
                if not linha or linha.startswith('#'):
                    continue
                
                partes = [p.strip() for p in linha.split('|')]
                
                if len(partes) != 7:
                    print(f"Erro de formato: A linha precisa de 7 colunas. Pulando: {linha}")
                    continue
                    
                metodo, f_str, phi_str, f_linha_str, intervalo_str, delta_str, it_str = partes 
                
                intervalo = [float(p.strip()) for p in intervalo_str.split(',')]
                delta = float(delta_str)
                max_it = int(it_str)

                tarefas.append({
                        'metodo': metodo,
                        'f(x)': f_str,
                        'phi(x)': phi_str,
                        'f_linha(x)': f_linha_str, 
                        'inicial': intervalo,
                        'delta': delta,
                        'it': max_it
                })
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_entrada}' não encontrado")
        sys.exit(1)
        
    return tarefas

def metodo_bisseccao(f_str, a, b, delta, max_it):
    historico = [] 
    k = 0
    xk_anterior = (a + b) / 2
    fa = validar_funcao(f_str, a) 

    while(k < max_it):
        if abs(b - a) < delta: 
            break
            
        xk = (a + b) / 2
        f_xk = validar_funcao(f_str, xk)
        
        if abs(f_xk) < delta: 
            break
            
        erro_aproximado = abs(xk - xk_anterior) 
        
        historico.append({
            'k': k, 
            'xk': xk, 
            'fxk': f_xk,
            'erro_aproximado': erro_aproximado, 
            'a': a, 
            'b': b,
            'intervalo_parada': abs(b - a)
        })

        if fa * f_xk < 0: 
            b = xk
        else: 
            a = xk; 
            fa = validar_funcao(f_str, a)
        
        xk_anterior = xk
        k += 1 

    if not historico or historico[-1]['k'] != k:
        historico.append({
            'k': k, 
            'xk': xk, 
            'fxk': f_xk, 
            'erro_aproximado': erro_aproximado if 'erro_aproximado' in locals() else 0, 
            'a': a, 
            'b': b, 
            'intervalo_parada': abs(b - a)
        })
    
    return historico

def metodo_mil(f_str, phi_str, x0, delta, max_it):
    xk = x0
    f_xk = validar_funcao(f_str, xk)
    historico = [{'k': 0, 'xk': xk, 'fxk': f_xk, 'erro_aproximado': 0}]

    for k in range(1, max_it + 1):
        xk_anterior = xk
        xk = validar_funcao(phi_str, xk_anterior)
            
        erro_aproximado = abs(xk - xk_anterior) 
        f_xk = validar_funcao(f_str, xk)

        historico.append({
            'k': k, 
            'xk': xk, 
            'fxk': f_xk,
            'erro_aproximado': erro_aproximado,
        })

        if erro_aproximado < delta:
            break

        if abs(f_xk) < delta: 
            break

    return historico

def metodo_newton(f_str, f_linha_str, x0, delta, max_it):
    xk = x0
    historico = [{'k': 0, 'xk': xk, 'fxk': validar_funcao(f_str, xk), 'erro_aproximado': 0}]
    
    for k in range(1, max_it + 1):
        xk_anterior = xk
        
        f_xk_anterior = validar_funcao(f_str, xk_anterior)
        f_linha_xk_anterior = validar_funcao(f_linha_str, xk_anterior) 

        if f_linha_xk_anterior == 0:
            print(f"[AVISO NEWTON] Derivada nula em k={k}. Parando.")
            break

        xk = xk_anterior - (f_xk_anterior / f_linha_xk_anterior)
        
        erro_aproximado = abs(xk - xk_anterior) 
        f_xk = validar_funcao(f_str, xk)
        
        historico.append({
            'k': k, 
            'xk': xk, 
            'fxk': f_xk,
            'erro_aproximado': erro_aproximado,
        })
        
        if erro_aproximado < delta:
            break
        
        if abs(f_xk) < delta: 
            break 

    return historico

def metodo_secante(f_str, x0, x1, delta, max_it):
    historico = []
    
    xk_0 = x0
    xk_1 = x1
    
    historico.append({'k': 0, 'xk': xk_0, 'fxk': validar_funcao(f_str, xk_0), 'erro_aproximado': 0})
    historico.append({'k': 1, 'xk': xk_1, 'fxk': validar_funcao(f_str, xk_1), 'erro_aproximado': abs(xk_1 - xk_0)})
    
    for k in range(2, max_it + 1):
        f_xk_1 = validar_funcao(f_str, xk_1)
        f_xk_0 = validar_funcao(f_str, xk_0)

        if f_xk_1 == f_xk_0:
            print(f"[AVISO SECANTE] Denominador zero em k={k}. Parando.")
            break

        xk_2 = xk_1 - f_xk_1 * ((xk_1 - xk_0) / (f_xk_1 - f_xk_0)) 
        
        erro_aproximado = abs(xk_2 - xk_1)
        f_xk2 = validar_funcao(f_str, xk_2)

        historico.append({
            'k': k, 
            'xk': xk_2, 
            'fxk': f_xk2,
            'erro_aproximado': erro_aproximado,
        })
        
        if erro_aproximado < delta:
            break
        
        if abs(f_xk2) < delta: 
            break 

        xk_0 = xk_1
        xk_1 = xk_2

    return historico

def metodo_regula_falsi(f_str, a, b, delta, max_it):
    historico = [] 
    k = 0
    
    fa = validar_funcao(f_str, a) 
    fb = validar_funcao(f_str, b)

    if fa * fb > 0:
        print(f"[AVISO REGULA FALSI] Intervalo inicial inválido: f(a)*f(b) > 0. Tentando rodar mesmo assim.")
        
    xk_anterior = a 
    
    while(k < max_it):
        if abs(b - a) < delta: 
            break
            
        if fb == fa:
            print(f"[AVISO REGULA FALSI] Denominador zero em k={k}. Parando.")
            break
            
        xk = b - fb * ((b - a) / (fb - fa))
        f_xk = validar_funcao(f_str, xk)
        
        if abs(f_xk) < delta: 
            break 
            
        erro_aproximado = abs(xk - xk_anterior) 
        
        historico.append({
            'k': k, 
            'xk': xk, 
            'fxk': f_xk,
            'erro_aproximado': erro_aproximado, 
            'a': a, 
            'b': b,
            'intervalo_parada': abs(b - a)
        })

        if fa * f_xk < 0:
            b = xk
            fb = f_xk
        else:
            a = xk
            fa = f_xk
            
        xk_anterior = xk
        k += 1 

    if not historico or historico[-1]['k'] != k:
        historico.append({
            'k': k, 
            'xk': xk, 
            'fxk': f_xk,
            'erro_aproximado': erro_aproximado if 'erro_aproximado' in locals() else 0, 
            'a': a, 
            'b': b, 
            'intervalo_parada': abs(b - a)
        })

    return historico

def salvar_resultados(arquivo_saida, resultados): 
    
    output_content = "################################################################\n"
    output_content += "             RELATÓRIO DE CÁLCULO DE RAÍZES                     \n"
    output_content += "################################################################\n\n"

    for resultado in resultados:
        metodo = resultado['metodo']
        f_str = resultado['f(x)']
        raiz_final = resultado['raiz']
        
        delta_val = resultado['delta']
        P = int(math.ceil(-math.log10(delta_val))) if delta_val > 0 else 6 
        precision_2P = P * 2 

        format_str_resumo = f".{precision_2P}e" 
        
        it_feitas = len(resultado['iteracoes']) - 1 

        output_content += f"------------------ MÉTODO: {metodo.upper()} ({metodo.lower()}) ------------------\n" 
        output_content += f"Função de entrada f(x): {f_str}\n"
        output_content += f"Tolerância Requerida (Delta): {delta_val:{format_str_resumo}}\n"
        output_content += f"Máximo de Iterações Permitidas: {resultado['it']}\n"
        output_content += f"Iterações REALMENTE Necessárias: {it_feitas} (Pode ter parado antes ou no limite)\n"
        output_content += f"Raiz APROXIMADA Encontrada (Valor Final de xk): {raiz_final:{format_str_resumo}}\n"
        output_content += "----------------------------------------------------------------\n\n"

        if metodo in ['Bissecção', 'Regula Falsi']:
            headers = ['k', 'a', 'b', 'xk', 'f(xk)', 'erro_aprox', 'Intervalo']
            col_keys = ['k', 'a', 'b', 'xk', 'fxk', 'erro_aproximado', 'intervalo_parada']
            col_widths = [5, 20, 20, 20, 20, 20, 20] 
        else:
            headers = ['k', 'xk', 'f(xk)', 'erro_aprox']
            col_keys = ['k', 'xk', 'fxk', 'erro_aproximado']
            col_widths = [5, 20, 20, 20] 

        tabela_str = "TABELA DE CONVERGÊNCIA:\n"
    
        tabela_str += "".join(h.ljust(w) for h, w in zip(headers, col_widths)) + "\n"
        tabela_str += "=" * sum(col_widths) + "\n"

        formato_cientifico = f".{precision_2P}e"

        for row in resultado['iteracoes']:
            linha_dados = ""
            for i, key in enumerate(col_keys):
                valor = row.get(key, 0) if key == 'k' else row.get(key, 0.0) 
                w = col_widths[i]
                
                if key == 'k':
                    valor_str = str(int(valor))
                else:
                    valor_str = f"{valor:{formato_cientifico}}"
                
                linha_dados += valor_str.ljust(w)
            tabela_str += linha_dados + "\n"
        
        output_content += tabela_str
        output_content += "\n\n"

    try:
        with open(arquivo_saida, 'w', encoding='utf-8') as f:
            f.write(output_content)
        print(f"\n[SUCESSO] O Arquivo de Resultados foi SALVO com sucesso em '{arquivo_saida}'. Cheque o arquivo!")
    except Exception as e:
        print(f"\n[ERRO] Nao deu pra SALVAR o arquivo de resultados. Deu o erro: {e}")

METODOS_NUMERICOS = {
    'Bissecção': lambda f, p, fl, ini, d, m: metodo_bisseccao(f, ini[0], ini[1], d, m), 
    'MIL': lambda f, p, fl, ini, d, m: metodo_mil(f, p, ini[0], d, m),             
    'Newton': lambda f, p, fl, ini, d, m: metodo_newton(f, fl, ini[0], d, m),
    'Secante': lambda f, p, fl, ini, d, m: metodo_secante(f, ini[0], ini[1], d, m),
    'Regula Falsi': lambda f, p, fl, ini, d, m: metodo_regula_falsi(f, ini[0], ini[1], d, m),
}


def main():
    ARQUIVO_ENTRADA = "dados.txt"
    ARQUIVO_SAIDA = "resultados_metodos.txt"

    tarefas = ler_dados_entrada(ARQUIVO_ENTRADA)
    resultados_finais = []

    for tarefa in tarefas:
        metodo = tarefa['metodo']
        
        if metodo in METODOS_NUMERICOS:
            func_metodo = METODOS_NUMERICOS[metodo]
            
            f_str = tarefa['f(x)']
            phi_str = tarefa['phi(x)']
            f_linha_str = tarefa['f_linha(x)']
            delta = tarefa['delta']
            max_it = tarefa['it']
            inicial = tarefa['inicial']

            historico = []
            
            historico = func_metodo(f_str, phi_str, f_linha_str, inicial, delta, max_it)
            
            if historico:
                resultados_finais.append({
                    'metodo': metodo,
                    'f(x)': f_str,
                    'delta': delta,
                    'it': max_it,
                    'iteracoes': historico,
                    'raiz': historico[-1]['xk'] 
                })
            
        else:
            print(f"[INFO] Método '{metodo}' desconhecido. Pulando.")

    salvar_resultados(ARQUIVO_SAIDA, resultados_finais)

if __name__ == "__main__":
    main()
