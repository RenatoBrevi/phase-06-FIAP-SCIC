# 1 ATIVIDADE INTEGRADORA - SISTEMA DE COMUNICAÇÃO INTERPLANETÁRIA DA COLÔNIA (SCIC)

Nessa fase, cada equipe deverá desenvolver um protótipo chamado de Sistema de Comunicação Interplanetária da Colônia (SCIC). O objetivo será organizar dados operacionais e de comunicação da Aurora Siger, avaliar a confiabilidade de previsões simples, priorizar alertas críticos, permitir consultas eficientes e gerar um relatório técnico de apoio à decisão.

A atividade deverá utilizar somente os conteúdos estudados até essa fase. Não será obrigatório integrar sensores físicos, APIs externas, hardware real, sistemas de supervisão e telemetria, sistemas avançados de gerenciamento de rede, dashboards web ou redes neurais profundas. Esses recursos podem ser simulados, desde que estejam relacionados aos conteúdos trabalhados nas disciplinas.

Conteúdos e tópicos abordados até aqui:

- NumPy, Pandas, Matplotlib, Seaborn e scikit-learn;
- Divisão de dados, treino, teste e validação;
- Métricas MAE, MSE, RMSE e R²;
- AIC, BIC, Grid Search e Random Search, quando aplicável;
- Erro absoluto, erro relativo, ponto flutuante e precisão numérica;
- Métodos iterativos, ponto fixo, Newton e Euler, apenas quando forem úteis à simulação;
- Heaps, heapify-up, heapify-down e filas de prioridade;
- Tries para armazenamento e busca de palavras ou códigos;
- Dispositivos de entrada e saída, sensores e interfaces;
- Bases numéricas, conversão binário/decimal/hexadecimal e representação de valores;
- Tensão, corrente, potência, resistores, lei de Ohm e circuitos simples;
- Sistemas inteligentes de gerenciamento da comunicação, IoT, redes inteligentes de comunicação, telemetria avançada, sistemas de supervisão e telemetria, sistemas avançados de gerenciamento de rede, redundância, monitoramento e manutenção preditiva;

Diversidade, cultura afro-brasileira e indígena, sustentabilidade e responsabilidade social.

### Figura 1 - Fluxo sugerido para desenvolvimento do protótipo do SCIC

Fluxo sugerido para desenvolvimento do protótipo — AURORA SIGER — MISSÃO · DADOS · IMPACTO

1. Coletar dados simulados — status dos módulos, consumo, tensão, corrente e alertas
2. Organizar arquivos — CSV/TXT/JSON com Pandas, listas e dicionários
3. Calcular indicadores — potência, erro absoluto, erro relativo e métricas
4. Avaliar modelo — MAE, MSE, RMSE, R² e comparação com baseline
5. Priorizar e consultar — heap para alertas e trie para busca por prefixo
6. Gerar relatório — interpretação técnica, limites e impactos sociais

Fonte: Elaborada pelo autor (2026)

## 1.1 Organização dos dados operacionais e de comunicação

Cada equipe deverá criar ou utilizar uma base simulada com informações da Aurora Siger. Essa base poderá ser construída manualmente pela equipe, desde que seja coerente com o contexto do projeto e suficiente para as análises solicitadas.

A base deverá conter, no mínimo, registros relacionados aos módulos da colônia. Exemplos de campos possíveis:

- Nome do módulo;
- Tipo do módulo, como habitação, agricultura, comunicação, laboratório, suporte médico ou armazenamento de dados;
- Latência observada;
- Latência prevista ou estimada;
- Tensão, corrente, potência aproximada ou potência de transmissão;
- Status operacional, como ativo, manutenção ou alerta;
- Nível de prioridade;
- Código do dispositivo ou sensor;
- Mensagem resumida do alerta;
- Data ou ciclo de registro.

A equipe deverá organizar os dados utilizando arquivos CSV, TXT ou JSON, além de estruturas em Python como listas, dicionários ou DataFrames. O uso de Pandas é recomendado para leitura, limpeza, organização e análise exploratória dos dados.

## 1.2 Análise numérica e avaliação de erros

O sistema deverá calcular indicadores numéricos que ajudem a equipe a compreender a diferença entre valores esperados e valores observados. A equipe deverá aplicar, no mínimo, os conceitos de erro absoluto e erro relativo:

- Erro absoluto entre latência prevista e latência observada;
- Erro relativo para comparar módulos com escalas diferentes de latência;
- Interpretação de possíveis diferenças numéricas causadas por aproximações, arredondamentos ou representação em ponto flutuante;
- Discussão sobre quando um erro pode ser considerado aceitável ou preocupante no contexto da colônia.

Quando fizer sentido, a equipe poderá utilizar métodos numéricos simples para simular evolução de uma variável ao longo do tempo, coma latência, estabilidade do enlace ou qualidade do sinal de um módulo. Essa simulação deve permanecer no nível estudado na disciplina, sem exigir modelos físicos avançados.

## 1.3 Modelo simples e avaliação de performance

A equipe deverá construir ou simular um modelo simples de previsão relacionado à operação da colônia. O modelo pode estimar, por exemplo, latência de comunicação, risco de alerta, carga necessária de um módulo ou demanda operacional em determinado ciclo.

O modelo deverá ser avaliado com métricas coerentes com o problema. Em problemas de regressão, a equipe deverá utilizar métricas como MAE, MSE, RMSE e R². Caso compare modelos alternativos, poderá discutir AIC, BIC, Grid Search ou Random Search.

O time deverá apresentar a interpretação das métricas, explicando que um único número não é suficiente para avaliar a qualidade da solução. Por exemplo: um R² alto não significa que o modelo é perfeito, e uma diferença grande entre MAE e RMSE pode indicar erros maiores em alguns registros.

### Figura 2 - Painel de avaliação da performance operacional

Modelo simples e avaliação de performance — AURORA SIGER

#### Métricas principais do modelo

| Métrica | Sigla | Descrição no painel |
| --- | --- | --- |
| Erro absoluto médio | MAE | média dos erros |
| Erro quadrático médio | MSE | penaliza erros maiores |
| Raiz do erro quadrático médio | RMSE | mesma unidade da variável |
| Coeficiente de determinação | R² | explicação do ajuste |

#### Interpretação dos resultados

- O modelo pode prever latência, risco de alerta ou demanda operacional.
- As métricas devem ser coerentes com o tipo de problema.
- Um único número não basta para avaliar a solução.
- R² alto não significa modelo perfeito; compare as métricas.

Fonte: Elaborada pelo autor (2026)

## 1.4 Priorização de alertas com heap

O sistema deverá possuir uma funcionalidade de priorização de alertas. Para isso, a equipe deverá utilizar o conceito de heap ou fila de prioridade. Cada alerta poderá receber uma prioridade baseada em critérios como criticidade, latência elevada, módulo essencial, risco operacional ou tempo desde o registro.

A equipe deverá demonstrar:

- Como os alertas foram representados;
- Qual critério foi utilizado para definir prioridade;
- Como a estrutura heap organiza os alertas;
- Como o sistema seleciona o alerta mais urgente;
- Qual é a vantagem dessa estrutura em relação a uma lista simples.

Não é necessário implementar um sistema complexo; o objetivo é demonstrar o uso prático da estrutura de dados estudada para resolver um problema coerente da missão.

## 1.5 Busca de registros com trie

O sistema deverá possuir uma funcionalidade de busca por prefixo utilizando o conceito de trie. Essa busca poderá ser aplicada a nomes de módulos, códigos de sensores, palavras-chave de alertas ou comandos cadastrados.

Exemplos de busca:

- Ao digitar “com”, o sistema retorna “Comunicação”, “Controle” ou “Comando”;
- Ao digitar um prefixo de código, o sistema retorna sensores compatíveis.

A equipe deverá explicar por que a trie é adequada para consultas por prefixo e como essa estrutura pode acelerar a localização de registros na colônia.

## 1.6 Dispositivos, bases numéricas e eletricidade básica aplicada à comunicação

A equipe deverá relacionar o protótipo com conceitos de organização e arquitetura de computadores. Para isso, deverá incluir uma explicação sobre quais dispositivos de entrada e saída poderiam alimentar ou exibir as informações do sistema, como:

- Sensores ou medidores simulados como entrada de dados;
- Monitor, dashboard, relatório ou terminal como saída de dados;
- Interfaces de comunicação, como rede, USB, Wi-Fi ou Bluetooth, apenas de forma conceitual;
- Códigos de sensores representados em decimal, binário ou hexadecimal;
- Conversão simples de pelo menos um código ou valor entre bases numéricas;
- Cálculo simples envolvendo tensão, corrente, potência ou potência de transmissão, utilizando conceitos de eletricidade básica aplicada à comunicação.

A equipe poderá, por exemplo, calcular potência aproximada de um transmissor a partir de tensão e corrente ou interpretar um código hexadecimal de sensor como identificador do sistema. O foco é, portanto, conectar os conceitos estudados ao funcionamento do protótipo.

## 1.7 Gerenciamento inteligente da comunicação

A equipe deverá explicar como o SCIC se relaciona com sistemas inteligentes de gerenciamento da comunicação. A proposta não exige implementar sistemas avançados reais, mas sim compreender como esses conceitos ajudam a pensar em uma rede de comunicação inteligente.

A equipe deverá discutir:

- Como sensores e medidores inteligentes poderiam coletar dados da colônia;
- Como o monitoramento contínuo ajuda a detectar anomalias;
- Como a automação pode apoiar decisões rápidas em situações críticas;
- Como o armazenamento de dados e enlaces redundantes poderiam ajudar na estabilidade da base;
- Como manutenção preditiva poderia reduzir falhas;
- Como redes inteligentes de comunicação e microrredes se relacionam com a operação da Aurora Siger.

A discussão deve partir dos dados e resultados do SCIC, explicando como indicadores de latência, alertas, falhas e prioridades contribuem para compreender a gestão inteligente da comunicação na Aurora Siger. A equipe deve conectar esses resultados a temas como sensores, monitoramento contínuo, automação, redundância, manutenção preditiva, redes inteligentes de comunicação e microrredes, evitando explicações genéricas que não estejam relacionadas ao protótipo desenvolvido.

## 1.8 Reflexão social, cultural e sustentável

Além da parte técnica, a equipe deverá incluir uma reflexão sobre o impacto social, cultural e sustentável do sistema desenvolvido. Essa análise deverá considerar que tecnologias inteligentes são utilizadas por pessoas e comunidades, além de pensar que decisões automatizadas podem gerar efeitos positivos ou negativos.

A equipe deverá abordar pelo menos três dos seguintes pontos:

- Como o uso eficiente da comunicação contribui para a sustentabilidade;
- Como conhecimentos tradicionais e respeito à natureza, presentes em culturas indígenas, podem inspirar decisões mais responsáveis sobre recursos;
- Como a valorização da diversidade cultural ajuda a evitar sistemas excludentes ou enviesados;
- Como uma comunidade tecnológica deve garantir transparência nas decisões baseadas em dados;
- Como a equipe humana continua responsável por validar decisões automatizadas;
- Como o projeto poderia evitar linguagem discriminatória, exclusão de grupos ou interpretações injustas.

Essa reflexão deverá aparecer no relatório final de forma conectada à solução desenvolvida para a Aurora Siger, explicando como o sistema proposto pode apoiar o uso mais eficiente da comunicação, reduzir desperdícios, priorizar decisões responsáveis e evitar impactos negativos causados por análises automatizadas sem supervisão humana.

# 2 ENTREGÁVEIS

Cada equipe deverá entregar um vídeo de apresentação do projeto de no máximo 5 minutos demonstrando o funcionamento completo do projeto desenvolvido.

O vídeo deverá ser publicado no YouTube como “Não listado” e o link deverá ser entregue juntamente com uma pasta compactada .zip contendo todos os arquivos do projeto.

Durante o vídeo, a equipe precisará apresentar:

- Descrição da comunicação interplanetária da Aurora Siger;
- Explicação dos dados operacionais e de comunicação utilizados;
- Demonstração da leitura, organização e análise dos dados;
- Explicação dos indicadores de comunicação calculados;
- Apresentação dos erros numéricos analisados, como erro absoluto e erro relativo;
- Explicação do modelo simples utilizado para previsão ou estimativa;
- Interpretação das métricas de avaliação de performance, como MAE, MSE, RMSE e R²;
- Demonstração da priorização de alertas utilizando heap;
- Demonstração da busca de registros utilizando trie;
- Explicação da relação do sistema com dispositivos, bases numéricas e eletricidade básica aplicada à comunicação;
- Demonstração prática do funcionamento do sistema em Python;
- Discussão sobre gerenciamento inteligente da comunicação.

Durante a apresentação, a equipe deverá demonstrar o funcionamento real do protótipo, explicando as principais decisões técnicas adotadas e mostrando como a solução apoia a análise de dados operacionais e de comunicação da Aurora Siger.

## 2.1 Requisitos do sistema desenvolvido

O sistema entregue pela equipe deverá conter:

- Código em Python;
- Organização de dados simulados da Aurora Siger;
- Uso de arquivo .csv, .txt ou .json para armazenar ou carregar dados;
- Manipulação dos dados com estruturas em Python, NumPy ou Pandas;
- Cálculo de pelo menos um indicador operacional ou de comunicação;
- Cálculo e interpretação de erro absoluto e erro relativo;
- Construção ou simulação de um modelo simples de previsão;
- Avaliação de performance com métricas estudadas na fase, como MAE, MSE, RMSE ou R²;
- Uso de heap ou fila de prioridade para organizar alertas críticos;
- Uso de trie para busca de prefixo em registros, códigos, módulos ou comandos;
- Relação com dispositivos de entrada e saída, bases numéricas e eletricidade básica aplicada à comunicação;
- Discussão sobre sistemas inteligentes de gerenciamento da comunicação;

Além disso, o sistema deverá apresentar:

- Menu simples de navegação no terminal ou execução organizada em Notebook;
- Dados organizados de forma clara;
- Mensagens de entrada e saída compreensíveis;
- Comentários no código explicando as principais etapas;
- Exemplos de execução das funcionalidades implementadas.

As funcionalidades implementadas deverão permitir:

- Carregar ou cadastrar dados da colônia;
- Consultar registros operacionais ou de comunicação;
- Calcular indicadores e erros numéricos;
- Executar ou simular uma previsão simples;
- Avaliar o desempenho da previsão com métricas;
- Priorizar alertas com heap;
- Realizar busca por prefixo com trie;
- Exibir uma análise final dos resultados.

Exemplo de funcionalidade esperada: ao selecionar a opção “Analisar alertas de comunicação”, o sistema poderá carregar uma base de dados simulada, identificar módulos com latência acima do previsto, calcular o erro entre latência estimada e latência real, priorizar os alertas mais críticos com heap e permitir a busca de registros por prefixo utilizando trie.

Durante a apresentação em vídeo, a equipe deverá demonstrar o funcionamento real do sistema.

## 2.2 Arquivos obrigatórios na entrega (.zip)

A pasta compactada .zip deverá conter, obrigatoriamente, os seguintes arquivos, com os respectivos formatos e nomes padronizados:

- codigo_fonte.py ou notebook_projeto.ipynb - arquivo principal do sistema, contendo o código-fonte em Python ou o Notebook com a solução desenvolvida;
- dados_aurora_siger.csv, dados_aurora_siger.json ou dados_aurora_siger.txt - arquivo contendo a base de dados simulada utilizada pelo sistema;
- relatorio_tecnico.pdf ou relatorio_tecnico.md - arquivo contendo a explicação técnica do projeto, incluindo contexto da solução, descrição dos dados, métricas utilizadas, análise dos erros, modelo simples, heap, trie, gerenciamento inteligente da comunicação, reflexão social, cultural e sustentável, limitações e possíveis melhorias;
- README.md - arquivo explicando o objetivo do projeto, os arquivos presentes na entrega, as dependências utilizadas e o modo de execução do sistema;
- link_video.txt - arquivo de texto contendo o link do vídeo da apresentação publicado no YouTube como “Não listado”;
- graficos_ou_imagens, se houver - pasta opcional contendo prints, gráficos ou imagens geradas durante a execução do projeto.

Importante:

- Todos os arquivos devem estar organizados de forma clara dentro da pasta .zip;
- Caso o projeto possua mais de um arquivo Python, a equipe deverá manter nomes organizados e intuitivos;
- O arquivo principal do sistema deverá estar identificado de forma clara para facilitar a correção;
- O relatório técnico deverá estar completo e conectado ao funcionamento do protótipo;
- O link do vídeo deverá estar funcionando no momento da correção.

## 2.3 REGRAS TÉCNICAS

Leve em consideração as seguintes regras técnicas:

- O código deverá executar sem a necessidade de bibliotecas, integrações ou ferramentas que não tenham sido trabalhadas até essa fase;
- A atividade deverá utilizar somente os conteúdos estudados na fase. Não será obrigatório integrar sensores físicos, APIs externas, hardware real, sistemas de supervisão e telemetria, sistemas avançados de gerenciamento de rede ou telemetria avançada reais, dashboards web ou redes neurais profundas. Esses recursos poderão ser citados ou simulados de forma conceitual, desde que estejam relacionados aos conteúdos estudados nas disciplinas e ao funcionamento do protótipo;
- O uso de Python, NumPy, Pandas, Matplotlib, Seaborn e scikit-learn será permitido, desde que aplicado de forma coerente com o projeto. A solução deverá ser simples, funcional e compatível com o nível da atividade;
- Caso a equipe utilize alguma biblioteca adicional, deverá explicar no README qual foi utilizada, por que ela foi necessária e como instalar a dependência;
- O sistema deverá apresentar comentários no código, organização dos arquivos e mensagens claras para o usuário. A entrega deverá permitir que o avaliador compreenda a proposta, execute o projeto e identifique as funcionalidades solicitadas.

# 3 CRITÉRIOS DE AVALIAÇÃO

### Tabela 1 – Critérios de avaliação

| Critério | Descrição | Peso |
| --- | --- | --- |
| Organização dos dados e coerência do contexto | Base simulada coerente com a Aurora Siger, uso adequado de arquivos e estruturas de dados e clareza na organização das informações. | 1,5 |
| Análise numérica e avaliação de erros | Cálculo e interpretação de erro absoluto, erro relativo, aproximações, precisão numérica e limites dos resultados. | 1,5 |
| Modelo simples e avaliação de performance | Uso coerente de modelos simples, divisão de dados quando aplicável e cálculo e interpretação de MAE, MSE, RMSE, R² ou métricas equivalentes. | 1,5 |
| Estruturas avançadas: heap e trie | Aplicação prática de heap para priorização e trie para busca por prefixo, com explicação clara das escolhas. | 1,5 |
| Relação com COA e eletricidade básica aplicada à comunicação | Conexão com dispositivos de entrada/saída, bases numéricas, códigos, tensão, corrente, potência ou lei de Ohm. | 1,5 |
| Gerenciamento inteligente da comunicação | Relação consistente com sensores, monitoramento, redes inteligentes de comunicação, redundância, monitoramento e manutenção preditiva e eficiência de comunicação. | 1,5 |
| Clareza da entrega, código e apresentação | Repositório organizado, README claro, código comentado, relatório estruturado e vídeo demonstrativo objetivo. | 1,0 |
| Total | | 10,0 |

Fonte: Elaborada pelo autor (2026)
