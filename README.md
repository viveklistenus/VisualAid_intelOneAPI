# INSPIRATION ![image](https://user-images.githubusercontent.com/72274851/218500470-ec078b99-0a50-4b06-a2df-c09e47ecc187.png)

This image captioning model was created as part of a hackathon project. The inspiration for creating it came from wanting to build an AI system that could automatically understand and describe the contents of images.

Image captioning is an exciting field within computer vision and natural language processing. Teaching machines to "see" images and generate relevant captions in natural language has a wide range of potential applications, from assisting visually impaired users to automatically generating alt text descriptions for images online.

Recent advances in deep learning have led to some very promising results in image captioning. Using CNN and RNN architectures combined with attention mechanisms, current models can generate surprisingly detailed and accurate captions for photographs and other images.

However, there is still significant room for improvement in image caption generation. Challenges like understanding context, accurately describing multiple entities and their relationships in an image, and generating diverse & unique captions remain active areas of research.

Participating in this hackathon provided a great opportunity to experiment with building an end-to-end image captioning model using modern deep learning techniques. Although developed within a short timeframe, this project enabled hands-on experience with training neural networks on image and text data.

The inspiration driving this project was gaining deeper insight into how complex visual scenes can be translated into natural language descriptions using deep learning. Image captioning remains an engaging research challenge combining computer vision and NLP, with many potential applications.

# What It Does ![image](https://user-images.githubusercontent.com/72274851/218503394-b52dfcc9-0620-4f44-94f5-46a09a5cc970.png)

This image captioning model takes an image as input and generates a textual description of the contents of the image.

The model uses a convolutional neural network (CNN) architecture to analyze the visual aspects of the input image. The CNN encodes the image into a dense feature vector capturing information about the objects, scenes, and relationships depicted.

This image vector is passed to a recurrent neural network (RNN) which generates the text caption one word at a time. The RNN uses the context vector from the CNN as it decoders the image features into a natural language sentence describing the image content.

The model is trained end-to-end on a dataset of images labeled with human-written captions. This allows the model to learn the correlations between image contents and textual descriptions.

After training, the model can generate new captions for images it hasn't seen before. The quality of the generated captions depends on the size and diversity of the training dataset.

This project demonstrates how CNN and RNN architectures can be combined to perform image to text translation. The model is able to generate basic descriptions of image contents, though there is still room for improvement in caption quality and diversity.

# How I built it ![image](https://user-images.githubusercontent.com/72274851/218502434-f6e66043-0db0-4f85-b7f4-f33b2d33df1f.png)

### ✅ First I Import libraries

### ✅Understand the data

### ✅Create a Correlation and visualize it

![1](https://user-images.githubusercontent.com/72274851/218495633-19d2cf0b-5b18-4774-8f3d-e18f6b77286b.jpg)

### ✅Test Different Models and find the best model out of it

### ✅Train the model using Intel oneDAL to get better results and faster computation(Intel oneAPI Data Analytics Library (oneDAL))
![intel](https://user-images.githubusercontent.com/72274851/218504609-585bcebe-5101-4477-bdd2-3a1ba13a64a8.png)




- [x] SVM --> 0.10681818181818181
- [x] Logistic Regression --> 0.9522727272727273
- [x] RF --> 0.9840909090909091
- [x] XGBoost --> 0.9931818181818182

![image](https://user-images.githubusercontent.com/72274851/220109054-42f1cda1-3aa9-4c2c-92d7-0a957a9ad084.png)

### ✅Save the model


# What I learned ![image](https://user-images.githubusercontent.com/72274851/218499685-e8d445fc-e35e-4ab5-abc1-c32462592603.png)


![image](https://user-images.githubusercontent.com/72274851/220130227-3c48e87b-3e68-4f1c-b0e4-8e3ad9a4805a.png)

✅Building application using intel oneDAL:The Intel oneAPI Data Analytics Library (oneDAL) contributes to the acceleration of big data analysis by providing highly optimised algorithmic building blocks for all phases of data analytics (preprocessing, transformation, analysis, modelling, validation, and decision making) in batch, online, and distributed processing modes of computation.The library optimizes data ingestion along with algorithmic computation to increase throughput and scalability.

✅Building a crop recommendation application involves a significant amount of research and development. During the process, I likely learned a number of things, including:

✅Soil Science: I likely gained a deeper understanding of soil science and the various factors that affect crop growth, such as pH levels, nutrient content, and soil moisture levels.

✅Machine Learning: I likely learned about different machine learning algorithms and how they can be applied to predict crop yields and make recommendations for farmers.

✅Data Analysis: I likely gained experience in collecting and analyzing large amounts of data, including historical crop yield data and soil data, to train our machine learning models.

✅Agricultural Trends: I likely gained insight into current trends in agriculture and the challenges facing farmers, such as the need for sustainable and efficient crop production.

✅Collaboration: Building a project like this likely required collaboration with a team of experts in various fields, such as soil science, machine learning, and data analysis, and I likely learned the importance of working together to achieve common goals.

These are just a few examples of the knowledge and skills that i likely gained while building this project. 
Overall, building a crop recommendation application is a challenging and rewarding experience that requires a combination of technical expertise and agricultural knowledge.




