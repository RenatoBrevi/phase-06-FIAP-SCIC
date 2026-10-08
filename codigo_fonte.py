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
            funcionalidade_em_desenvolvimento("Calcular Indicadores e Erros")
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