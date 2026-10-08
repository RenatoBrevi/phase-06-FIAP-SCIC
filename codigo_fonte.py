import pandas as pd
from pathlib import Path # Manipular caminhos com POO independenteo do SO

# Caminho da pasta onde o arquivo Python está localizado
pasta_projeto = Path(__file__).resolve().parent

# Arquivo de dados .CSV utiliazdo no projeto
arquivo_dados = pasta_projeto / "dados_aurora_siger.csv"

# Carregadi a base de dados simulados da Aurora Siger a partir do .CSV
def carregar_dados():
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

# Exibindo uma vis'ao simples da base carregada.
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
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            dados = carregar_dados() # Permite visualizar os registros no .CSV

            if dados is not None:
                visualizar_dados(dados)

        elif opcao == "2":
            funcionalidade_em_desenvolvimento("Consultar Registros")
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