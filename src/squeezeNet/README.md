# _CNN SqueezeNet_

Esta pasta contém todos os scripts utilizados para treinar, validar e testar a rede neural SqueezeNet, bem como os arquivos auxiliares destes processos. 

## Estrutura de arquivo dessa pasta
### Pasta *aux_files*
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
       


    







## Importante - É necessário:

1. Ter feito a configuração indicada no ReadMe principal do projeto [aqui](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD)
2. Acessar o ambiente virtual criado (Passo a passo [aqui](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD))
3. Baixar os arquivos indicados no ReadMe principal [aqui](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD)


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