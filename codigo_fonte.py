import os
import pandas as pd
from pathlib import Path # Manipular caminhos com POO independenteo do SO

# Caminho da pasta onde o arquivo Python está localizado
pasta_projeto = Path(__file__).resolve().parent

# Arquivo de dados .CSV utiliazdo no projeto
arquivo_dados = pasta_projeto / "dados_aurora_siger.csv"

# Função para limpar o temrinal
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# Função para aguardar o usuário apertar "ENTER" para voltar ao menu principal
def enter():
    input("\nPressione 'ENTER' para voltar ao menu principal...")

# Carregadi a base de dados simulados da Aurora Siger a partir do .CSV
def carregar_dados(exibir_mensagem=False): # Define se o sistema mostra a informação de carregamento.
    try:
        dados = pd.read_csv(arquivo_dados)
        
        print("\nDados da Aurora Siger carregados com sucesso.")
        print(f"Registros Carregados: {len(dados)}")
        print(f"Colunas Encontradas: {len(dados.columns)}")

        return dados
    
    except FileNotFoundError:
        print("\nERRO: o arquivo 'dados_aurora_siger.csv' não foi encontrado.")
        print("Matenha o arquivo CSV na mesma posta de 'codigo_fonte.py'.")

    except pd.errors.EmptyDataError:
        print("\nERRO: o arquivo CSV está vazio.")

    except pd.errors.ParserError:
        print("\nERRO: não foi possível interpretar o conteúdo do arquivo CSV.")

    return None

# Exibindo uma vis'ao simples da base carregada - Menu 1
def visualizar_dados(dados):
    if dados is None:
        print("\nNenhum dado est[a disponível para visualização.")
        return
    
    print("\n" + "=" * 60)
    print("DADOS OPERACIONAIS E DE COMUNICAÇÃO - AURORA SIGER")
    print("=" * 60)

    # Exibindo os primeiros 10 registros para não poluir o terminal
    print("\nPrimeiros 10 registros:")
    print(dados.head(10).to_string(index=False))

    print("\nResumo da Base:")
    print(f"Total de Registros: {len(dados)}")
    print(f"Total de Módulos: {dados['modulo'].nunique()}")
    print(f"Total de Sensores: {dados['codigo_sensor'].nunique()}")

    print("\nRegistros por Status:")
    print(dados["status"].value_counts().to_string())

# Função para consultar os registros - Menu 2
def consultar_registros(dados):
    if dados is None:
        print("\nNenhum dado está disponível para consulta.")
        return
    
    while True:
        limpar_tela()

        print("\n" + "=" * 60)
        print("CONSULTAR REGISTROS - AURORA SIGER")
        print("=" * 60)

        print("1 - Pesquisar por Módulo")
        print("2 - Pesquisar por Sensor")
        print("3 - Pesquisar por Status")
        print("4 - Pesquisar por Ciclo")
        print("0 - Voltar")
        print("=" * 60)

        opcao_consulta = input("Escolha o tipo de consulta: ").strip()

        # Colunas principais que serão mostradas
        colunas_exibicao = [
            "ciclo",
            "modulo",
            "codigo_sensor",
            "latencia_prevista_ms",
            "latencia_observada_ms",
            "status",
            "prioridade",
            "criticidade",
            "mensagem_alerta"
        ]

        resultado = None

        # Consulta por módulo
        if opcao_consulta == "1":
            limpar_tela()

            print("=" * 60)
            print("CONSULTA POR MÓDULO")
            print("=" * 60)

            print("\nMódulos disponíveis:")

            for modulo in dados["modulo"].unique():
                print(f"- {modulo}")

            pesquisa = input("\nDigite o nome do módulo: ".strip())

            resultado = dados[
                dados["modulo"].str.contains(
                    pesquisa,
                    case=False,
                    na=False
                )
            ]
        
        # Consulta por sensor
        elif opcao_consulta == "2":
            limpar_tela()

            print("=" * 60)
            print("CONSULTA POR SENSOR")
            print("=" * 60)

            print("\nSensores Disponíveis:")

            for sensor in sorted(dados["codigo_sensor"].unique()):
                print(f"- {sensor}")

            pesquisa = input("\nDigite o código do sensor: ").strip()

            resultado = dados[
                dados["codigo_sensor"].str.lower() == pesquisa.lower()
            ]

        # Consulta por status
        elif opcao_consulta == "3":
            limpar_tela()

            print("=" * 60)
            print("CONSULTA POR STATUS")
            print("=" * 60)

            print("\nStatus Disponíveis:")
            print("- Ativo")
            print("- Manutenção")
            print("- Alerta")

            pesquisa = input("\nDigite o status: ").strip()

            resultado = dados[
                dados["status"].str.lower() == pesquisa.lower()
            ]

        # Colsunta por ciclo
        elif opcao_consulta == "4":
            limpar_tela()

            print("=" * 60)
            print("CONSULTA POR CICLO")
            print("=" * 60)

            try:
                ciclo = int(input("\nDigite o ciclo de 1 a 8: "))

                resultado = dados[
                    dados["ciclo"] == ciclo
                ]
            
            except ValueError:
                print("\nCiclo inválido. Digite um número inteiro.")
                return

        # Voltar sem realizar consulta
        elif opcao_consulta == "0":
            return
        else:
            print("\nOpção de consulta inválida.")
            enter()
            continue
        
        # Exibindo o resultado da pesquisa
        if resultado.empty:
            print("\nNenhum registro encontrado.")
        else:
            print("\n" + "=" * 60)
            print(f"REGISTROS ENCONTRADOS: {len(resultado)}")
            print("=" * 60)

            print(resultado[colunas_exibicao].to_string(index=False)) # Transforma tabela Pandas em texto.

        enter()
    
# Classificando o erro relativo de acordo com critérios simulados - Menu 3
def classificar_erro_relativo(erro_relativo):
    if erro_relativo <= 5:
        return "Baixo"
    elif erro_relativo <= 15:
        return "Atenção"
    else:
        return "Preocupante"
    
# Função para calcular os indicadores operacionais e erros numéricos
def calcular_indicadores_erros(dados):
    if dados is None:
        print("\nNenhum dado está dispon[ivel para análise.")
        return dados
    
    # Cria uma cópia para preservar os dados originais carregados
    dados_calculados = dados.copy()

    # Calculando a potência aproximada dos dispositivos
    dados_calculados["potencia_w"] = (
        dados_calculados["tensao_v"] * dados_calculados["corrente_a"]
    ).round(2)

    # Calculando o erro absoluto entre a latência prevista e a latência observada
    dados_calculados["erro_absoluto_ms"] = (
        dados_calculados["latencia_observada_ms"] - dados_calculados["latencia_prevista_ms"]
    ).abs()

    # Calculando o erro relativo em porcentagem
    dados_calculados["erro_relativo_pct"] = (
        (
            dados_calculados["erro_absoluto_ms"] / dados_calculados["latencia_observada_ms"]
        ) * 100
    ).round(2)

    # Classificando o erro relativo
    dados_calculados["classificacao_erro"] = (
        dados_calculados["erro_relativo_pct"].apply(classificar_erro_relativo)
    )

    limpar_tela()

    print("=" * 70)
    print("INDICADORES OPERACIONAIS E ERROS NUMÉRICOS - AURORA SIGER")
    print("=" * 70)

    # Indicadores gerais
    latencia_media = dados_calculados["latencia_observada_ms"].mean()
    potencia_media = dados_calculados["potencia_w"].mean()
    erro_absoluto_medio = dados_calculados["erro_absoluto_ms"].mean()
    erro_relativo_medio = dados_calculados["erro_relativo_pct"].mean()

    print("\nRESUMO GERAL")
    print("-" * 70)
    print(f"Registros Analisados: {len(dados_calculados)}")
    print(f"Latência Observada Média: {latencia_media:.2f}ms")
    print(f"Potência Média Aproximada: {potencia_media:.2f}W")
    print(f"Erro Absoluto Médio: {erro_absoluto_medio:.2f}ms")
    print(f"Erro Relativo Médio: {erro_relativo_medio:.2f}%")

    # Quantidade de registros por classificação
    print("\nCLASSIFICAÇÃO DOS ERROS")
    print("-" * 70)

    quantidade_baixo = (
        dados_calculados["classificacao_erro"] == "Baixo"
    ).sum()

    quantidade_atencao = (
        dados_calculados["classificacao_erro"] == "Atenção"
    ).sum()

    quantidade_preocupante = (
        dados_calculados["classificacao_erro"] == "Preocupante"
    ).sum()

    print(f"Baixo: {quantidade_baixo}")
    print(f"Atenção: {quantidade_atencao}")
    print(f"Preocupante: {quantidade_preocupante}")

    print("\nCritérios Simulados Utilizados pelo SCIC:")
    print("Até 5% ----------> Baixo")
    print("Acima de 5% -----> Atenção")
    print("Acima de 15% ----> Preocupante")

    # Mosntrando os registros com maiores erros relativos
    maiores_erros = dados_calculados.sort_values(
        by="erro_relativo_pct",
        ascending=False
    ).head(10)

    colunas_exibicao = [
        "ciclo",
        "modulo",
        "codigo_sensor",
        "latencia_prevista_ms",
        "latencia_observada_ms",
        "potencia_w",
        "erro_absoluto_ms",
        "erro_relativo_pct",
        "classificacao_erro"
    ]

    print("\n 10 REGISTROS COM MAIOR ERRO RELATIVO")
    print("-" * 70)
    print(maiores_erros[colunas_exibicao].to_string(index=False))

    # Identificando o maior erro encontrado
    indice_maior_erro = dados_calculados["erro_relativo_pct"].idxmax()
    maior_erro = dados_calculados.loc[indice_maior_erro]

    print("\nMAIOR DESVIO ENCONTRADO")
    print("-" * 70)
    print(f"Módulo: {maior_erro['modulo']}")
    print(f"Sensor: {maior_erro['codigo_sensor']}")
    print(f"Latência Prevista: {maior_erro['latencia_prevista_ms']}ms")
    print(f"Latência Observada: {maior_erro['latencia_observada_ms']}ms")
    print(f"Erro Absoluto: {maior_erro['erro_absoluto_ms']:.2f}ms")
    print(f"Erro Relativo: {maior_erro['erro_relativo_pct']:.2f}%")
    print(f"Classificação: {maior_erro['classificacao_erro']}")

    # Demonstração simples da precisão do ponto flutuante
    print("\nPRECISÃO NUMÉRICA E PONTO FLUTUANTE")
    print("-" * 70)

    exemplo_ponto_flutuante = 0.1 + 0.2

    print(f"No Python, 0.1 + 0.2 resulta em: {exemplo_ponto_flutuante}")
    print(f"Arredondando para 2 casas: {exemplo_ponto_flutuante:.2f}")

    print(
    """
Pequenas diferenças podem ocorrer por que alguns números decimais não possuem
representação binária exata. Por isso, os indicadores do SCIC são arredondados
para facilitar a apresentação e interpretação.
    """
    )

    print("\nINTERPRETAÇÃO")
    print("-" * 70)

    print(
        """
Erros baixos indicam que a latência observada permaneceu próxima da estimativa.
Erros maiores exigem atenção porque podem indicar instabilidade ou anomalias na comunicação.
Os limites usados nesta simulação são critérios internos do protótipo SCIC e não representam limites universais.
        """
    )

    return dados_calculados

# Exibindo o menu principal SCIC
def exibir_menu():
    print("\n" + "=" * 60)
    print(" SCIC - SISTEMA DE COMUNICAÇÃO INTERPLANETÁRIA DA COLÔNIA")
    print(" AURORA SIGER")
    print("=" * 60)
    print("1 - Carregar e Visualizar Dados")
    print("2 - Consultar Registros")
    print("3 - Calcular Indicadores e Erros")
    print("4 - Executar Modelo de Previsão")
    print("5 - Analisar Alertas por Prioridade")
    print("6 - Buscar Registros por Prefixo")
    print("7 - Bases Numéricas e Dados Elétricos")
    print("8 - Análise Geral do Sistema")
    print("0 - Encerrar")
    print("=" * 60)

# Mensagem temporária para próxima etapa
def funcionalidade_em_desenvolvimento(nome):
    print(f"\n'{nome}' será implementado nas próximas etapas do projeto.")

# Função principal do sistema que carrega os dados e mantém o menu em execução.
def main():
    dados = carregar_dados() # Carregamento inicial da base

    while True:
        limpar_tela()
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()
        limpar_tela()

        if opcao == "1":
            dados = carregar_dados(exibir_mensagem=True) # Permite visualizar os registros no .CSV
            if dados is not None:
                visualizar_dados(dados)
                enter()
                limpar_tela()
        elif opcao == "2":
            consultar_registros(dados)
        elif opcao == "3":
            dados = calcular_indicadores_erros(dados)
            enter()
            limpar_tela()
        elif opcao == "4":
            funcionalidade_em_desenvolvimento("Executar Modelo de Previsão")
        elif opcao == "5":
            funcionalidade_em_desenvolvimento("Analisar Alertas por Prioridade")
        elif opcao == "6":
            funcionalidade_em_desenvolvimento("Buscar Registros por Prefixo")
        elif opcao == "7":
            funcionalidade_em_desenvolvimento("Bases Numéricas e Dados Elétricos")
        elif opcao == "8":
            funcionalidade_em_desenvolvimento("Análise Geral do Sistema")
        elif opcao == "0":
            print("\nSISTEMA ENCERRADO.")
            break
        else:
            print("\nOpção inválida. Digite um número de 0 a 8.")

if __name__ == "__main__":
    main()