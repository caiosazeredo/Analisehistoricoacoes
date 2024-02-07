Funcionalidades
Carregamento de dados históricos de ações de um arquivo CSV.
Cálculo de indicadores técnicos: média móvel simples (SMA) e desvio padrão.
Identificação de sinais de compra e venda baseados na análise técnica.
Visualização gráfica dos dados de preço, indicadores e sinais.
Pré-requisitos
Para executar o QuantAnalyser, você precisa ter Python instalado em seu ambiente. Além disso, as seguintes bibliotecas Python são necessárias:

pandas
numpy
matplotlib

Você pode instalar todas as dependências necessárias executando:
pip install pandas numpy matplotlib

Configuração
Clone o repositório do QuantAnalyser para o seu ambiente local ou faça o download do código-fonte.
Certifique-se de ter instalado todos os pré-requisitos listados acima.
Prepare um arquivo CSV com os dados históricos de ações que deseja analisar. O arquivo deve ter pelo menos as colunas Date e Close, onde Date representa as datas das observações e Close representa os preços de fechamento das ações.
Uso
Para usar o QuantAnalyser, siga estes passos:

Abra o arquivo do sistema (quantanalyser.py, por exemplo) em um editor de texto ou IDE.
Modifique a variável arquivo_dados na parte inferior do script para apontar para o caminho do seu arquivo CSV de dados históricos.
Execute o script. Você pode fazer isso a partir da linha de comando ou usando sua IDE. Para executar a partir da linha de comando, navegue até o diretório onde o arquivo está localizado e execute:
python quantanalyser.py
O sistema irá processar os dados, calcular os indicadores, identificar sinais de compra e venda, e exibir uma visualização gráfica dos resultados.
Contribuições
Contribuições para o QuantAnalyser são bem-vindas. Para contribuir, por favor, faça um fork do repositório, faça suas alterações e submeta um pull request.
