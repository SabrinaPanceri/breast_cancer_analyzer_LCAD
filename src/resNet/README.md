
# _ResNet_
Esta pasta contém todos os scripts utilizados para treinar, validar e testar a rede neural contendo a arquitetura ResNet, bem como os arquivos auxiliares destes processos. 

*Acesso rápido*
- [Treinamento e Validação](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD/tree/master/src/resNet#treinando-a-resnet)
- [Requerimentos Mínimos para Rodar o Script](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD/tree/master/src/resNet#requerimentos-mínimos-para-rodar-o-script)

--- 

## Requerimentos Mínimos para Rodar o Script

### Instalação do Torch

Acesse o repositório que contém o Pytorch

```
 git clone --recursive https://github.com/pytorch/pytorch
 cd pytorch
```  

```
git submodule sync
git submodule update --init --recursive
```
Intalacão do PyTorch no Linux:

```
export CMAKE_PREFIX_PATH=${CONDA_PREFIX:-"$(dirname $(which conda))/../"}
python setup.py install
```

### Instalação do Torchvision

TorchVision requer PyTorch 1.4 ou um mais novo.


Instalação pelo Pip:
  
```
pip install torchvision
```
Pelo respositório:
  
```
python setup.py install
```

### Instalação do Cuda 10.2

```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu1604/x86_64/cuda-ubuntu1604.pin

sudo mv cuda-ubuntu1604.pin /etc/apt/preferences.d/cuda-repository-pin-600

wget http://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda-repo-ubuntu1604-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb

sudo dpkg -i cuda-repo-ubuntu1604-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb

sudo apt-key add /var/cuda-repo-10-2-local-10.2.89-440.33.01/7fa2af80.pub

sudo apt-get update

sudo apt-get -y install cuda
```



## Treinando a ResNet

### Para utilizar o script é necessário seguir todas as orientações contidas no ReadMe principal do repositório [Acesse aqui](https://github.com/LCAD-UFES/breast_cancer_analyzer_LCAD#requisitos)

--- 

### Detalhamento:

1. Para treinar a SqueezeNet com o manual_cropped_dataset, acesse a pasta: 
   ```bash
   cd breast_cancer_analyzer_LCAD/src/resNet/
   ```
2. Com seu editor de preferência, abra o script ***finetuning_torchvision_models.py*** e altere as seguintes variáveis globais:

```
data_dir = (
	'colocar, entre aspas simples, o caminho absoluto da pasta aonde se encontra o dataset. A pasta deve conter duas pastas nomeadas por 'train' e 'val', dentro de cada uma dessas pastas devem conter outros diretórios com as imagens, onde o nome desses diretórios são os nomes das classes das imagens.
	)
```

```


- **As variáveis globais abaixo, representam alguns dos hiperparâmetros da rede**

  - batch_size: representa a quantidade de imagens que serão analisadas juntas. 

  - num_epochs: representa a quantidade de épocas para análise do conjunto de treino. 

  - initial_learning_rate: representa a taxa de aprendizado inicial da rede. Este valor é utilizado para atualizar o valor das sinapses e dos neurônios da rede.
  
  - last_epoch_for_learning_rate_decay representa em qual época será finalizada a diminuição do valor da taxa de aprendizado

  - decay_rate: representa o valor pelo qual a taxa de aprendizado será dividida a cada decaimento. 

  - decay_step_size: representa a quantidade de épocas necessárias para fazer a atualização da taxa de aprendizado
  

  - O ajuste destes hiperparâmetros são essenciais para melhorar o aprendizado da rede.

3. Salve o arquivo. 

4. Considerando que o ambiente virtual já está ativado, basta digitar o comando:
   ```bash
   $ python finetuning_torchvision_models.py
   ```


