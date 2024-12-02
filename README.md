# TrabalhoA3_Matem-tica
Este repositório contém o código-fonte e a documentação para um sistema que otimiza o uso de energia solar em pequenos hospitais. O projeto prevê a geração solar baseada em dados climáticos, garantindo operação eficiente de geradores em quedas de energia. Desenvolvido com Python e APIs meteorológicas, facilita decisões energéticas sustentáveis.


O objetivo principal é prever a geração de energia solar a partir das condições climáticas e estimar o tempo de operação de geradores, garantindo que hospitais em áreas com frequentes quedas de energia possam manter seus serviços funcionando de forma eficiente e sustentável. O sistema visa integrar dados meteorológicos em tempo real com cálculos precisos para fornecer previsões energéticas e relatórios visuais claros, ajudando os gestores hospitalares a tomar decisões informadas.

Funcionalidades Principais
Previsão de Geração Solar
Utiliza dados meteorológicos em tempo real para calcular a energia solar gerada, considerando variáveis como irradiância, temperatura, umidade, vento e cobertura de nuvens.

Cálculo de Autonomia de Geradores
Estima o tempo de funcionamento dos geradores com base na energia solar disponível e no consumo energético hospitalar.

Relatórios Automatizados
Gera relatórios em formato Excel detalhando as previsões e cálculos, facilitando a análise e o planejamento energético.

Tecnologias Utilizadas
Python: Linguagem principal para desenvolvimento do sistema.
APIs Meteorológicas: Integração com ClimaTempo para obter dados climáticos em tempo real.
Pandas: Manipulação e análise de dados.
Matplotlib: Criação de visualizações para validações.
Excel (via Pandas): Exportação de resultados para planilhas.

Estrutura do Repositório
gerador_de_relatorios_clima_geradores.py: Script principal do sistema.
previsao_energia.xlsx: Exemplo de saída gerada com previsões e autonomia de geradores.
Relatório Panéis, Geradores e Clima.pbix: Relatório em Power BI para análises visuais avançadas.


Como Rodar o Projeto
Pré-requisitos
Python 3.8 ou superior instalado.

Bibliotecas necessárias:
pip install requests pandas matplotlib openpyxl
Conta e token na ClimaTempo API.


Configuração
Edite o arquivo gerador_de_relatorios_clima_geradores.py para incluir seu token de API e o ID da cidade desejada.
Execução

Rode o script principal:
python gerador_de_relatorios_clima_geradores.py

Saída

O sistema salvará os resultados no arquivo previsao_energia.xlsx.
Informações detalhadas serão exibidas no console.


Referências:
ClimaTempo API: Disponível em: https://advisor.climatempo.com.br/
EDP – Desafios da Eficiência Energética nos Hospitais. Disponível em: https://solucoes.edp.com.br/desafios-da-eficiencia-energetica-nos-hospitais​
ANEEL – Eficiência Energética em Hospitais. Disponível em: https://www.gov.br/aneel​
