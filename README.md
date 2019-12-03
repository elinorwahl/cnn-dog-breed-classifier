[//]: # (Image References)

[image1]: ./images/sample_dog_output.png "Sample Output"
[image2]: ./images/vgg16_model.png "VGG-16 Model Keras Layers"
[image3]: ./images/vgg16_model_draw.png "VGG16 Model Figure"

# CNN Dog Breed Classifier

![Sample Output][image1]

Convolutional neural networks are exceptionally useful tools for processing and classifying image data. This project notebook is used to create a pipeline that processes photographic images; given an image of a dog, the algorithm takes a guess at the dog's breed.  If given an image of a human, the code will identify the resembling dog breed.

A Keras classifier network built from scratch and trained on the image data was able to achieve an accuracy of 25% when exposed to test images. A pre-trained VGG16 network was able to achieve an accuracy between roughly 32-49%. And a pre-trained Resnet50 network attained an accuracy of roughly 84% when identifying test images, and could correctly identify the subjects of an additional six photos as dogs, humans, or neither.

This repository consists of:

`dog_app.ipynb`: Jupyter notebook containing the body of the project

`extract_bottleneck_features.py`: Python program used to obtain bottleneck features for each pre-trained network

`bottleneck_features`: Folder used to store necessary bottleneck features for each pre-trained network

`data`: Folder for storing dog and human image data

`haarcascades`: Folder containing an XML file of a Haar feature-based cascade image detector

`images`: Folder of demonstrative image files

`my_photos`: Folder of stock images used to test the performance of the final classifier

`requirements`: Folder of software dependencies for the project

`saved_models`: Folder used to store best weights for each classifier model

![Sample Output][image1]

### Usage

- Clone the repository and navigate to the downloaded folder:
```	
git clone https://github.com/udacity/dog-project.git
cd dog-project
```

- Download the [dog dataset](https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/dogImages.zip).  Unzip the folder and place it in the repo, at location `path/to/dog-breed-classifier/data/dog_images`. 

- Download the [human dataset](https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/lfw.zip).  Unzip the folder and place it in the repo, at location `path/to/dog-breed-classifier/data/lfw`.  If you are using a Windows machine, you are encouraged to use [7zip](http://www.7-zip.org/) to extract the folder. 

- Download the [VGG-16 bottleneck features](https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/DogVGG16Data.npz) and the [Resnet50 bottleneck features](https://s3-us-west-1.amazonaws.com/udacity-aind/dog-project/DogResnet50Data.npz) for the two respective pre-trained classifiers.  Place them in the repo, at location `path/to/dog-breed-classifier/bottleneck_features`.

- Using a GPU to run this project is strongly recommended. If you plan to install TensorFlow with GPU support on your local machine, follow [this guide](https://www.tensorflow.org/install/) to install the necessary NVIDIA software on your system.  If you are using an EC2 GPU instance, you can skip this step.

- If you are running the project on your local machine (and not using AWS, Crestle or a similar GPU-enabling platform), create (and activate) a new environment.

	- __Linux__ (to install with __GPU support__, change `requirements/dog-linux.yml` to `requirements/dog-linux-gpu.yml`): 
	```
	conda env create -f requirements/dog-linux.yml
	source activate dog-project
	```  
	- __Mac__ (to install with __GPU support__, change `requirements/dog-mac.yml` to `requirements/dog-mac-gpu.yml`): 
	```
	conda env create -f requirements/dog-mac.yml
	source activate dog-project
	```  
	**NOTE:** Some Mac users may need to install a different version of OpenCV
	```
	conda install --channel https://conda.anaconda.org/menpo opencv3
	```
	- __Windows__ (to install with __GPU support__, change `requirements/dog-windows.yml` to `requirements/dog-windows-gpu.yml`):  
	```
	conda env create -f requirements/dog-windows.yml
	activate dog-project
	```

- If you are running the project on your local machine (and not using AWS, Crestle or a similar GPU-enabling platform) and Step 6 throws errors, try this __alternative__ step to create your environment.

	- __Linux__ or __Mac__ (to install with __GPU support__, change `requirements/requirements.txt` to `requirements/requirements-gpu.txt`): 
	```
	conda create --name dog-project python=3.5
	source activate dog-project
	pip install -r requirements/requirements.txt
	```
	**NOTE:** Some Mac users may need to install a different version of OpenCV
	```
	conda install --channel https://conda.anaconda.org/menpo opencv3
	```
	- __Windows__ (to install with __GPU support__, change `requirements/requirements.txt` to `requirements/requirements-gpu.txt`):  
	```
	conda create --name dog-project python=3.5
	activate dog-project
	pip install -r requirements/requirements.txt
	```
	
- (Optional) **If you are using AWS**, install Tensorflow.
```
sudo python3 -m pip install -r requirements/requirements-gpu.txt
```
	
- Switch [Keras backend](https://keras.io/backend/) to TensorFlow.
	- __Linux__ or __Mac__: 
		```
		KERAS_BACKEND=tensorflow python -c "from keras import backend"
		```
	- __Windows__: 
		```
		set KERAS_BACKEND=tensorflow
		python -c "from keras import backend"
		```

- (Optional) If you are running the project on your local machine (and not using AWS, Crestle or a similar GPU-enabling platform), create an [IPython kernel](http://ipython.readthedocs.io/en/stable/install/kernel_install.html) for the `dog-project` environment. 
```
python -m ipykernel install --user --name dog-project --display-name "dog-project"
```

- Open the notebook.
```
jupyter notebook dog_app.ipynb
```

- (Optional) If you are running the project on your local machine (and not using AWS, Crestle or a similar GPU-enabling platform), before running code, change the kernel to match the dog-project environment by using the drop-down menu (**Kernel > Change kernel > dog-project**). Then follow the instructions in the notebook.