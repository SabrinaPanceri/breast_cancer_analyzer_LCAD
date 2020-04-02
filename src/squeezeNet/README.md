# _CNN SqueezeNet_
Esta pasta contém todos os scripts utilizados para treinar, validar e testar a rede neural SqueezeNet, bem como os arquivos auxiliares destes processos. 

--- 

### Estrutura de arquivos
#### Pasta *aux_files*
- Contém todos os arquivos auxiliares utilizados como inputs para a rede.
- Estes arquivos representam os conjuntos de treino, validação e teste.
- O nome dos arquivos seguem as lógicas abaixo:
  - *cbisddsm_OF10_automatic_cropped_dataset.txt* => contém o nome das imagens que foram aleatoriamente escolhidas para compor o conjunto de treino e validação para o teste de OverFitting (OF). 
    - *cbisddsm* - nome da base originária
    - *OF* - objetivo do conjunto 
    - *10* - quantidade de imagens de cada classe (OBS: Este número consta apenas nos arquivos de OF)
    - *automatic_cropped_dataset* - nome da base de recortes
  - *cbisddsm_train_2020_02_13.txt*, *cbisddsm_val_2020_02_13.txt*, *cbisddsm_test_2020_02_13.txt* => contém o nome das imagens que foram aleatoriamente escolhidas para compor o conjunto de treino, validação e teste que serão analisadas pela rede. 
    - *cbisddsm* - nome da base originária
    - *train* ou *test* ou *val* - objetivo do conjunto 
    - *2020_02_13* - data que o arquivo foi criado
    - OBS: Alguns arquivos podem ter observações após a data.
- O arquivo *training_dataset_ijcnn.txt* contém a lista de imagens na ordem que as mesmas foram lidas pela rede para gerar os resultados descritos no artigo submetido ao IJCNN.

#### Pasta *metrics*
- Contém os scripts escritos pelo Me. [Raphael Carneiro](carneiro.raphael@lcad.inf.ufes.br), sob a orientação do Prof. Dr. [Alberto F. De Souza](alberto@lcad.inf.ufes.br), para filtrar as inferência feitas pela rede e indicar um diagnóstico de "câncer" ou "não câncer" para cada "Paciente" que está no conjunto de teste.

*Obs: Descrição em construção*

#### Pastas *runs_.../*
1. Todo treinamento cria uma pasta *squeezenet1_1/{number}* dentro da caminho indicado *na variável global RUNS_FOLDER* que está script de treino.
2. Dentro da pasta *squeezenet1_1*, são criadas pasta para cada treino realizado. Essas pastas são criadas em ordem numérica e crescente. Logo, caso você apague algum pasta já criada e esta não seja a última, a próxima pasta de treino a ser criada receberá o número da que você apagou. 
3. A pasta de cada treino contém:
   - training_dataset.txt - Contém o caminho absoluto das imagens na ordem em que elas foram inseridas na rede. 
   - training_log.txt - Contém todas as informações de acerto ou erro para cada imagem que compõe o batch. Essa informação é calculada com base na classe de cada imagem e na inferência a rede fez sobre cada imagem.
   - loss_log.txt - Contém a informação, da "loss do batch" e o "step" a que ela se refere. Ao final de cada época está o valor da *Learning_Rate* impresso.
   - results.txt = Contém todas as matrizes de confusão calculas sobre o conjunto de validação completo. As matrizes de confusão calculas ao salvar cada modelo da rede, ou seja, a cada check point e ao final de cada época. 
   - classification_error.txt = Este arquivo contém o nome de todas as imagens que não foram classificadas corretamente pela rede durante o cálculo das matrizes de confusão. *É um arquivo pesado, portanto, não sincronizado para o git.*
   - treinamento_... .py = É a cópia fiel do script que foi executado para realizar o treinamento. Dessa forma, os valores dos hiperparâmetros e demais configurações ficam salvas.
   - pasta *models* = contém todos os pesos salvos durante o treinamento. Subir para o git o peso que tiver a maior acurácia média no conjunto de validação. Este será o peso utilizado para fazer as inferências no conjunto de teste.

---

### Lembre-se, para utilizar o script é necessário:

1. Ter feito a configuração indicada no ReadMe principal do repositório [aqui](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD)
2. Acessar o ambiente virtual criado (Passo a passo [aqui](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD))
3. Baixar os arquivos indicados no ReadMe principal do repositório[aqui](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD)

## Treinando a SqueezeNet



### Para utilizar o script de treinamento da SqueezeNet, você precisa:

1. Entrar na pasta
   ```bash
   $ cd breast_cancer_analyzer_LCAD/src/squeezeNet
   ```
   - Nesta pasta estão todos os scripts utilizados para fazer os diversos experimentos realizados neste projeto.
     - Todos os scripts tem uma breve explicação nas primeiras linhas do arquivo e o nome dos arquivos são autoexplicativos

4. Para executar um treino utilizando a base marcada manualmente e disponibilizada [aqui](https://drive.google.com/open?id=1X6eZ8hrxsR7oPwYK5iiHx_21aPIRQv77)
   - Faça o download do arquivo manual_cropped_dataset.tar.gz e descompacte-o na pasta breast_cancer_analyzer_LCAD/dataset/

     ```bash
     $ cd breast_cancer_analyzer_LCAD/src/squeezeNet
     ```

	 








## Testando 