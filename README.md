# MinhaAPI <br/> 
![GitHub top language](https://img.shields.io/github/languages/top/Micheleregina2022/MinhaAPI?color=pink)



### API de Manipulação de Dados
Esta é uma API desenvolvida no Replit para treinar a manipulação de dados utilizando a biblioteca Pandas em conjunto com o framework Flask. O objetivo desta API é fornecer informações estatísticas sobre um conjunto de dados contidos em um arquivo CSV.






<br/> <br/> 
## Configuração
Certifique-se de ter instalado o Python em sua máquina. Você também precisará das bibliotecas Pandas e Flask para executar esta API. Você pode instalá-las usando o seguinte comando: <br/><br/> 
*pip install pandas flask*
<br/> <br/> 
## Uso
* Faça o download do arquivo CSV contendo os dados que você deseja analisar e salve-o com o nome "tabela.csv" no mesmo diretório do arquivo principal da API.

* Execute o arquivo da API usando o seguinte comando:  <br/>

  *python <nome_do_arquivo>.py*

* A API estará disponível localmente no endereço http://localhost:5000/. </br>

## Rotas
A API possui as seguintes rotas: </br>
### /homepage </br>
Descrição: Retorna todas as linhas e colunas do conjunto de dados. </br>
Método: GET </br>
URL: /   </br>
Resposta: Um objeto JSON contendo as linhas e colunas do conjunto de dados. </br></br>

### /vendas </br>
Descrição: Retorna estatísticas de vendas, incluindo o total de vendas, a média, o valor máximo e o valor mínimo. </br>
Método: GET  </br>
URL: /vendas </br>
Resposta: Um objeto JSON contendo as estatísticas de vendas.</br></br>


### /TV </br>
Descrição: Retorna a quantidade total de TV vendida e estatísticas adicionais sobre o atributo "TV" do conjunto de dados. </br>
Método: GET  </br>
URL: /TV  </br>
Resposta: Um objeto JSON contendo a quantidade total de TV vendida e estatísticas adicionais sobre o atributo "TV".</br></br>


### /radio </br>
Descrição: Retorna a quantidade de ocorrências do atributo "Radio" e a quantidade de valores únicos presentes neste atributo.</br>
Método: GET </br>
URL: /radio </br>
Resposta: Um objeto JSON contendo a quantidade de ocorrências do atributo "Radio" e a quantidade de valores únicos. </br></br>


### /jornal </br>
Descrição: Retorna a mediana do atributo "Jornal", a moda (valores mais frequentes) e a contagem de cada valor presente neste atributo.</br>
Método: GET </br>
URL: /jornal </br>
Resposta: Um objeto JSON contendo a mediana do atributo "Jornal", a moda e a contagem de valores. </br></br>


## Exemplo de Uso </br>
Você pode acessar a API localmente usando uma ferramenta como o cURL ou o Postman. </br>
Aqui está um exemplo de como você pode fazer uma solicitação usando o cURL: </br>

*curl http://localhost:5000/*
</br> 
Isso retornará todas as linhas e colunas do conjunto de dados. </br></br>

### Observações </br>
* Certifique-se de ter o arquivo "tabela.csv" no mesmo diretório da API. </br>
* Esta API foi desenvolvida com fins educacionais para treinar a manipulação de dados e não é recomendada para uso em produção.</br>
* Certifique-se de verificar se as bibliotecas Pandas e Flask estão instaladas corretamente em seu ambiente antes de executar a API.</br>

