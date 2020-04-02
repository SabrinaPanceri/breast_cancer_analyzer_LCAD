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
1. Todo treinamento cria uma pasta *squeezenet1_1/{numero}* dentro da caminho indicado *na variável global RUNS_FOLDER* que está no script de treino.
2. Dentro da pasta *squeezenet1_1*, são criadas pasta para cada treino realizado. Essas pastas são criadas em ordem numérica e crescente. Logo, caso você apague algum pasta e esta não seja a última, a próxima pasta receberá o número da que você apagou.
3. A pasta de cada treino contém:
   - **pasta *models*** = contém todos os pesos salvos durante o treinamento. Subir para o git o peso que tiver a maior acurácia média no conjunto de validação. Este será o peso utilizado para fazer as inferências no conjunto de teste.
   - **classification_error.txt** = Este arquivo contém o nome de todas as imagens que não foram classificadas corretamente pela rede durante o cálculo das matrizes de confusão. *É um arquivo pesado, portanto, não sincronizado para o git.*
   - **loss_log.txt** - Contém a informação, da "loss do batch" e o "step" a que ela se refere. Ao final de cada época está o valor da *Learning_Rate* impresso.
   - **results.txt** = Contém todas as matrizes de confusão calculas sobre o conjunto de validação completo. As matrizes de confusão calculas ao salvar cada modelo da rede, ou seja, a cada check point e ao final de cada época. 
   - **training_dataset.txt** - Contém o caminho absoluto das imagens na ordem em que elas foram inseridas na rede. 
   - **training_log.txt** - Contém todas as informações de acerto ou erro para cada imagem que compõe o batch. Essa informação é calculada com base na classe de cada imagem e na inferência a rede fez sobre cada imagem.
   - **treinamento_... .py** = É a cópia fiel do script que foi executado para realizar o treinamento. Dessa forma, os valores dos hiperparâmetros e demais configurações ficam salvas.
   

---

### Lembre-se, para utilizar o script é necessário:

1. Ter feito a configuração indicada no ReadMe principal do repositório [aqui](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD)
2. Acessar o ambiente virtual criado (Passo a passo [aqui](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD))
3. Baixar o arquivo manual_cropeed_dataset indicado no ReadMe principal do repositório [aqui](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD)

---

## Treinando a SqueezeNet
Os arquivos .py iniciados com *treinamento_* são os scripts para treino da rede. 

### Para utilizar o script de treinamento da SqueezeNet para analisar o manual_cropped_dataset, você precisa:

-  Entrar na pasta
   ```bash
   $ cd breast_cancer_analyzer_LCAD/src/squeezeNet
   ```
-  Com seu editor de preferência, abra o script *treinamento_cancer_tissue.py* e altere as seguintes variáveis globais:

```
RUNS_FOLDER = 'colocar, entre aspas simples, o caminho absoluto da pasta onde
você quer salvar a pasta do treino'
```

```
Exemplo: 
RUNS_FOLDER = '/home/breast_cancer_analyzer_LCAD/src/squeezeNet/runs_manual_cropped_dataset'
```
```
TRAINING = (
	'colocar, entre aspas simples, o caminho absoluto do arquivo com o 
	nome das imagens para treino. não esquecer a vírgula após a aspas',
	)
```

```
Exemplo: 
TRAINING = (
        '/home/breast_cancer_analyzer_LCAD/src/squeezeNet/aux_files/cbisddsm_train_2019_10_15.txt',
)
```
```
TRAINING_DIR = (
        'colocar, entre aspas simples, o complemento do caminho das imagens
         para treino. não esquecer a vírgula após a aspas',
)
```

```
Exemplo:
TRAINING_DIR = (
        '/home/breast_cancer_analyzer_LCAD/dataset/cancer_tissue_dataset/manual_cropped_dataset',
)
```

- O arquivo *cbisddsm_train_2019_10_15.txt* contém parte do caminho para as imagens que serão utilizadas no treino separado por um espaço da classe da imagem. 
*Ex: "augmented_malignant/Calc-Test_P_01471_RIGHT_CC_MALIGNANT_Crop_0_180D.png 1".*
Atente-se que o valor de TRAINING_DIR + a parte do caminho da imagem devem estar corretas. Para testar, tente abrir a imagem via terminal utilizando o *eog*.
```bash
$ eog /home/breast_cancer_analyzer_LCAD/dataset/cancer_tissue_dataset/manual_cropped_dataset/augmented_malignant/Calc-Test_P_01471_RIGHT_CC_MALIGNANT_Crop_0_180D.png
```
- Caso o caminho seja inválido, ajuste o valor de TRAINING_DIR.
- Não é necessário colocar a / no final do caminho indicado em TRAINING_DIR. 

```
TEST = (
         'Colocar, entre aspas simples, o caminho absoluto do arquivo com o
         nome das imagens para validação. Não esquecer a vírgula após a aspas.',
)
```

```
Exemplo:
TEST = (
         '/home/breast_cancer_analyzer_LCAD/src/squeezeNet/aux_files/cbisddsm_val_2019_10_15.txt',
)
```
```
TEST_DIR = (
        'Colocar, entre aspas simples, o complemento do caminho das imagens
         para validação. Não esquecer a vírgula após a aspas',
)
```

```
Exemplo:
TEST_DIR = (
         '/home/breast_cancer_analyzer_LCAD/dataset/cancer_tissue_dataset/manual_cropped_dataset',
)
```
	- O arquivo *cbisddsm_val_2019_10_15.txt* contém parte do caminho para as imagens que serão utilizadas para validação separadas por um espaço da classe da imagem. 
	*Ex: "good/Calc-Training_P_00991_LEFT_CC_BENIGN_WITHOUT_CALLBACK_Crop_0.png 0".*
	Atente-se que o valor de TEST_DIR + a parte do caminho da imagem devem estar corretos. Para testar, tente abrir a imagem via terminal utilizando o *eog*.
    ```bash
    $ eog /home/breast_cancer_analyzer_LCAD/dataset/cancer_tissue_dataset/manual_cropped_dataset/good/Calc-Training_P_00991_LEFT_CC_BENIGN_WITHOUT_CALLBACK_Crop_0.png
    ```
	- Caso o caminho seja inválido, ajuste o valor de TEST_DIR.
	- Não é necessário colocar a / no final do caminho indicado em TEST_DIR. 

```
BATCH_SIZE, ACCUMULATE = 128, 1
```
- 
```
EPOCHS = 500
```
```
SAVES_PER_EPOCH = 1
```
```
INITIAL_LEARNING_RATE = 0.0003
```
```
LAST_EPOCH_FOR_LEARNING_RATE_DECAY = 28
```
```
DECAY_RATE = 2
```
```
DECAY_STEP_SIZE = 3
```
```
NUM_WORKERS = 4
```


## Testando 