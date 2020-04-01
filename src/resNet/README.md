#resNet

### Install Torch

Get the PyTorch Source

```
 git clone --recursive https://github.com/pytorch/pytorch
 cd pytorch
```  
//if you are updating an existing checkout

```
git submodule sync
git submodule update --init --recursive
```
Install PyTorch on Linux:

```
export CMAKE_PREFIX_PATH=${CONDA_PREFIX:-"$(dirname $(which conda))/../"}
python setup.py install
```

### Install Torchvision

TorchVision requires PyTorch 1.4 or newer.

Anaconda install:

```
conda install torchvision -c pytorch
```

Pip install:
  
```
pip install torchvision
```
From source:
  
```
python setup.py install
```
// or, for OSX
// MACOSX_DEPLOYMENT_TARGET=10.9 CC=clang CXX=clang++ python setup.py install



### Install C++ API

TorchVision also offers a C++ API that contains C++ equivalent of python models.

Installation From source:

mkdir build
cd build
// Add -DWITH_CUDA=on support for the CUDA if needed

```
cmake ..
make
make install
```


