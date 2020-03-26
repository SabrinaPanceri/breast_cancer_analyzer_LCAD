# Breast Cancer Analyzer LCAD

### Versão em Português
- Repositório do projeto "Análise de Imagens Médicas Usando Aprendizado Profundo" que pode ser acessado em http://www.informatica.ufes.br/pt-br/pos-graduacao/PPGI/detalhes-do-projeto?id=9678.

Para mais informações envie um e-mail para sabrina.panceri@lcad.inf.ufes.br ou sabrinapanceri@gmail.com

### English version (Page under construction)
- Repository of the project "Analysis of Medical Images Using Deep Learning" which can be accessed at http://www.informatica.ufes.br/pt-br/pos-graduacao/PPGI/detalhes-do-projeto?id=9678. 

For more information, send an email to sabrina.panceri@lcad.inf.ufes.br or sabrinapanceri@gmail.com

---

## Pré-requisitos
- Ubuntu 16.04 LTS 64bits
- Python 3.5.2
- Pip3
  - Página oficial do Pip - https://pypi.org/project/pip/
- VirtualEnv
  - Aconselhamos que utilize o VirtualEnv e crie um ambiente virtual específico para rodar esse projeto.
    - Utilize o python3 para criar o ambiente virtual. 
    ```bash
    $ virtualenv -p /usr/bin/python3.5 ~/breast_cancer 
    ```
    - Aqui tem um tutorial bem legal sobre o [VirtualEnv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)
    - Página oficial do VirtualEnv - https://pypi.org/project/virtualenv/
- Git

---
1. Clone esse repositório para seu computador.
   ```bash
   $ git clone https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD.git
   ```

2. Faça o download do arquivo [CALC_CC_flipped_dataset.tar.gz](https://drive.google.com/drive/folders/1zE6C8WPYQYwQvixJ_bhkzBLocZPyeyCB?usp=sharing). 
   - Extrair a pasta PNG_CALC_CC_renamed_dataset para *breast_cancer_analyzer_LCAD/dataset/*

3. Via terminal, ative o ambiente virtual criado e acesse na pasta do projeto.
   ```bash
   $ source ~/breast_cancer/bin/activate
   $ cd breast_cancer_analyzer_LCAD
   ```
   - Utilize o pip para instalar o requisitos necessários para rodar o projeto
   ```bash
   $ pip install --no-cache -r requirements.txt
   ```
4. Acesse o README do módulo ou rede que deseja utilizar.

---


# Módulos e Redes (Readme's em construção)

#### _Mammo_ _Marker_

Módulo criado para fazer a marcação manual das áreas de interesse. 

Acesse o readme do módulo em /src/mammo_marker/README.md ou [clique aqui](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD/blob/master/src/mammo_marker/README.md)
 
#### _Mammo_ _PreProcessing_

Módulo que contém os códigos criados para realizar diversos tipos de pré-processamentos nas imagens, antes delas serem analisadas pelas redes neurais. 

Acesse o readme do módulo em /src/mammo_preprocessing/README.md ou [clique aqui](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD/blob/master/src/mammo_preprocessing/README.md)

#### _Mammo_ _Viewer_

Módulo de visualização simples, criado para apresentar os resultados iniciais obtidos através dos diversos treinos e ajustes feitos na redes neurais. 

Acesse o readme do módulo em /src/mammo_viewer/README.md ou [clique aqui](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD/blob/master/src/mammo_viewer/README.md)

#### _resNet_

Contém os scripts utilizados para treinar, validar e testar a rede neural resNet.

Acesse o readme em /src/resNet/README.md ou [clique aqui](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD/blob/master/src/resNet/README.md) 


#### _SqueezeNet_

Contém os scripts utilizados para treinar, validar e testar a rede neural SqueezeNet.

Acesse o readme em /src/squeezeNet/README.md ou [clique aqui](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD/blob/master/src/squeezeNet/README.md)

