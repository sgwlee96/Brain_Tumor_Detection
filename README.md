# Brain Tumor Detection with Xception Deep Learning Model

Brain tumor detection is a critical task in medical imaging analysis, facilitating early diagnosis and treatment planning for patients. In this project, we employ deep learning techniques, specifically leveraging the Xception architecture, to automate the detection process. This abstract summarizes our approach, dataset, implementation strategies, results, and further research directions.

## Overview

Brain tumors pose significant health risks, necessitating timely intervention. Deep learning models offer promising solutions for automating brain tumor detection from medical images. Leveraging the Xception architecture, renowned for its effectiveness in image classification, we aim to develop a robust tumor detection system.

The detection of brain tumors from medical images is crucial for timely medical intervention and treatment planning. Traditional methods often rely on manual inspection by radiologists, which can be time-consuming and prone to errors. In this project, we propose a deep learning-based approach using the Xception model to automate the detection process. By harnessing the power of convolutional neural networks (CNNs), we aim to achieve accurate and efficient brain tumor detection from MRI images.

## Approach

In this project, we utilize the Xception deep learning model, a state-of-the-art CNN architecture, renowned for its ability to extract intricate features from images. The Xception model offers superior performance in image classification tasks, making it well-suited for medical image analysis. We chose the Xception model for its exceptional feature extraction capabilities, essential for accurately identifying subtle patterns indicative of brain tumors.

This is the example image of the structure of Xception model
![image](https://github.com/sgwlee96/Brain_Tumor_Detection/assets/82964002/9b274171-2440-463f-b284-6e6aecee26f5)

Cited from https://www.researchgate.net/figure/Proposed-structure-of-Xception-network-used-within-each-stream-of-CNN_fig2_355098045

## Dataset

We utilized a dataset sourced from various repositories on Kaggle, comprising 155 positive brain tumor images and 98 negative brain tumor images. The dataset selection process intentionally reflects real-world challenges, where acquiring a sufficient number of medical images can be difficult. Below are random samples of positive and negative brain tumor images used for training.

The below images are random samples of positive and negative brain tumor images used for training. 

![image](https://github.com/sgwlee96/Brain_Tumor_Detection/assets/82964002/2bb41130-8c4a-48ad-b3fa-2f4fc59ed7d2)

## Implementation & Further Research

To train brain tumor images, I chose Xception model for its superior feature extraction capabilities, essential for accurate brain tumor detection. 

Our original plan involved experimenting with various regularization techniques, such as L1 and L2 penalties, data augmentation, and balancing techniques like SMOTE and ADASYN, to address the imbalance between positive and negative samples. However, due to computational constraints, we plan to optimize the training process by reducing the number of epochs and batch sizes. Additionally, we aim to explore cloud computing platforms such as Google Colab for further research.

## Results

- Train Xception without Regularization

![image](https://github.com/sgwlee96/Brain_Tumor_Detection/assets/82964002/cc68fc1e-fb75-4d87-a7b1-99cfd4e5e740)

Test Accuracy: 0.92
Test Loss: 0.85


![image](https://github.com/sgwlee96/Brain_Tumor_Detection/assets/82964002/9da3e688-b117-40e2-bc9b-ec520a3b0278)

  
- Train Xception with Regularization of L2 penalty

After training the model with 150 epochs, I could observe that the validation loss increases from around 60 epochs, which states that the model is overfitting. Thus, I reduced the size of epochs and implemented l2 penalty to solve the overfitting. 

![image](https://github.com/sgwlee96/Brain_Tumor_Detection/assets/82964002/e112ddbc-5aeb-4d9d-9426-3bbaaa2ef0a3)

After the test, I gained 

Test Accuracy : 0.61
Test Loss : 2.01

The introduction of L2 regularization negatively impacted the model's performance, as evidenced by the decrease in test accuracy and increase in test loss. Further optimization is required to improve the model's generalization capabilities.


## Conclusion

In conclusion, this project demonstrates the feasibility of using deep learning techniques, particularly the Xception model, for brain tumor detection from MRI images. By leveraging the advanced feature extraction capabilities of the Xception architecture, we achieved promising results in automating the detection process. However, our experiments revealed challenges such as overfitting, necessitating the exploration of regularization techniques to enhance model generalization.

Moving forward, further research is warranted to address the limitations observed in this study. This includes optimizing hyperparameters, exploring additional regularization techniques, and expanding the dataset to improve model robustness. Additionally, collaboration with medical professionals and domain experts is essential to ensure the clinical relevance and applicability of the developed system.

Overall, this project underscores the potential of deep learning in advancing medical image analysis and underscores the importance of ongoing research in this domain to improve patient outcomes and healthcare delivery.
