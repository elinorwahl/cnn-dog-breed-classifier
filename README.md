[//]: # (Image References)

[image1]: ./images/sample_dog_output.png "Sample Output"

# CNN Dog Breed Classifier

### Motivation

Convolutional neural networks are exceptionally useful tools for processing and classifying image data. The goal of this project is to create a CNN that takes in pipeline-processed photographic images of dogs, and learns to match the images with labels of dog breeds as accurately as possible. Then an algorithm is used to take new images and determine what dog breed the subject of the image most closely resembles.  If given an image of a human, the code will identify the resembling dog breed. If the subject of the image doesn't look like either a photo of a dog or a human, the algorithm will also be able to identify the subject as neither.

![Sample Output][image1]

### Results

A Keras classifier network built from scratch and trained on the image data was able to achieve an accuracy close to or exceeding 20% when exposed to test images. A pre-trained VGG16 network was able to achieve an accuracy between roughly 32-49%. And a pre-trained Resnet50 network attained an accuracy of roughly 84% when identifying test images, and could correctly identify the subjects of an additional six photos as dogs, humans, or neither.

### Libraries

This project makes use of the **cv2**, **glob**, **keras**, **matplotlib**, **numpy**, **PIL**, **random**, **sklearn**, and **tqdm** libraries.

### Files

`dog_app.ipynb`: Jupyter notebook containing the body of the project

`extract_bottleneck_features.py`: Python program used to obtain bottleneck features for each pre-trained network

`haarcascades`: Folder containing an XML file of a Haar feature-based cascade image detector

`images`: Folder of demonstrative image files

`my_photos`: Folder of stock images used to test the performance of the final classifier

`requirements`: Folder of software dependencies for the project

`saved_models`: Folder used to store best weights for each classifier model

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

### Acknowledgements

This project was done as part of Udacity's [Data Scientist Nanodegree](https://www.udacity.com/course/data-scientist-nanodegree--nd025). While this particular version of the dog breed classifier project is not available on GitHub yet, a version that functions in a very similar way may be found [here](https://github.com/udacity/dog-project).
