# Image Captioning as Visual AID 
<h3>Tech stack and Tools</h3> 
<li>Intel OneAPI</li>
<li>Tensorflow</li>
<li>Streamlit</li>
<li>Intel Developer Cloud</li>
<li>Jupiter Notebook</li>
<li>numpy</li>

## What is Image Captioning problem ?
<p>Image captioning is the process of generating a natural language description of an image. It is a task in the field of computer vision and natural language processing. The goal of image captioning is to generate a coherent and fluent sentence that accurately describes the image content.</p>

![image](https://github.com/viveklistenus/VisualAid_intelOneAPI/assets/28853520/681a7039-1e48-4cd3-a07a-ecf1666d1152)

An image captioning system typically consists of two main components:

<li>An image feature extractor: This component is responsible for extracting features from the input image, such as object locations, sizes, and colors.</li>

<li>A natural language generator: This component takes the image features as input and generates a natural language description of the image.</li>

## How to run this project

This project uses streamlit to demo the result of EfficentNet + Transformer (Trained with 5 epoches).

So first you will need to install streamlit and Python 3. Depend on your OS, there maybe many different ways to install it. In this project I use Windows 11 to install all of them. So I will put some video tutorial to install them here.

Python 3: https://www.youtube.com/watch?v=z3Hdewxuuoo

After completed install these things, you can do the below step.
### Clone the project

```
git clone https://github.com/viveklistenus/VisualAid_intelOneAPI.git
cd Image-Captioning-with-Transformer
```
### Create and Enter the Anaconda Environment

```
conda create --name image-captioning
conda activate image-captioning
```
### Install dependencies
```
conda install -c anaconda pip
pip install -r requirements.txt
```

### Open the streamlit file and run demo

```
streamlit run web.py
```

### Exit Anaconda Environment

```
conda deactivate
```

The model tutorial: https://keras.io/examples/vision/image_captioning/




