# Email-Classification

# Project UI Demo

<p float="left">
  <img src="https://github.com/alaminbhuyan/Email-Classification/blob/master/images/readme%20image/Screenshot_1.jpg" width="500px" height='300px'/>
  <img src="https://github.com/alaminbhuyan/Email-Classification/blob/master/images/readme%20image/Screenshot_2.jpg" width="500px" height='300px'/> 
  <img src="https://github.com/alaminbhuyan/Email-Classification/blob/master/images/readme%20image/Screenshot_3.jpg" width="500px" height='300px'/> 
</p>

Motive and Goal is developing a spam email classifier so that it can classify the spam email.

# Description

  ***Data Collection***<br/>
  Data collected from: https://www.kaggle.com/datasets/venky73/spam-mails-dataset </br>
  This dataset contains huge data, almost 5171 Email found here.<br>

  ***Data Cleaning and preprocessing***<br/>
  This dataset contains lots of duplicate Emails. So, I drop the duplicate Email and in the preprocessing stage I remove the numerical symbol, number etc. This process reduces training time, facilitates 
  internal computation, and increases `Accuracy`.
  
  ***FrameWork***<br/>
  For this project I use `Google Colab`, `NLTK`, `gensim` libraries. These are really helpful to implement code.
  
  ***Model selection***<br/>
  In this project I've experiment with different models. Finally, `SVC` model provides, that gave me better result than another model.
  I've tried `KNeighborsClassifier`, `DecisionTreeClassifier`, `RandomForestClassifier` and lastly `SVC`.<br>

  ***Models Comparison & Evaluation***</br>

  |   Model       | Training Accuracy|  Testing Accuracy| F1-Score| AUC Score| CV Score|
  |---------------|-------------|-------------|-------------|-------------|-------------|
  | KNeighborsClassifier	      |      83.65%    | 81.67%|   72.60|82.28|0.7999|
  | DecisionTreeClassifier      |      100%    | 77.88%|61.46|72.83|0.7864|
  | RandomForestClassifier      |      100%    | 88.40%|76.85|81.89	|0.8788|
  |SVC                          |      98.25%    | 94.28%|89.97|92.58	|0.9241|
  <br>
  

# Deployment
As I want to make an app, I have to deploy my project. So I've chosen the `Streamlit Cloud` to deploy.

You can find my work in here: https://alaminbhuyan-email-classification-main-oaiqrp.streamlit.app/

# Notes
</br>

|Index|Comment|
|:---|:---|
|1.|[Recommended IDE: PyCharm Community edition](https://www.jetbrains.com/pycharm/download/)|
