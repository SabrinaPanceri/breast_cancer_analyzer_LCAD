# Breast Cancer Analyzer LCAD

Repositorio do projeto "Análise de Imagens Médicas Usando Aprendizado Profundo" que pode ser acessado em http://www.informatica.ufes.br/pt-br/pos-graduacao/PPGI/detalhes-do-projeto?id=9678.

Para mais informações, envie um e-mail para sabrina.panceri@lcad.inf.ufes.br

## Descrição dos módulos

### _Mammo_ _Marker_
 Para ter acesso ao Mammo Marker é necessário compilar o arquivo "mammo_marker.cpp". 
 Para isso, siga os passos abaixo:
 1. Abra o terminal na pasta do projeto
 2. Entre na pasta -> cd src/mammo_marker
 3. Compile o arquivo -> make
 	Será gerado um arquivo binário chamado "mammo_marker"
 4. Crie uma pasta com nome labels -> mkdir labels
 
 Para iniciar a marcação das imagens, é necessário gerar o arquivo de entrada com o caminho absoluto das mamografias. 
 Para o caso da base CBIS-DDSM, são utilizadas as mamografias completas e as mamografias segmentadas.
 Os arquivos devem apresentar as imagens dos pacientes na mesma ordem.
 É necessário baixar a pasta "original_dataset" dentro da pasta "dataset". 
 As pastas com as imagens estão disponíveis em 
 https://drive.google.com/drive/folders/1zE6C8WPYQYwQvixJ_bhkzBLocZPyeyCB?usp=sharing
 É necessário baixar os arquivos original_dataset.tar.gz e descompactar a pasta dentro da pasta "dataset"
 5. Para abrir o arquivo binário, digite -> ./mammo_marker mamografias_completas.txt mamografias_segmentadas.txt
 
### _Mammo_ _Marker_
 
 
