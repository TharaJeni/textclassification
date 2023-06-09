# -*- coding: utf-8 -*-
"""2200940.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-X989Vgl9kfEAjNKTie9D4meomGsncKA

# **Register Number:** 2200940

1. Common Codes
2. Method/model 1 Specific Codes
3. Method/model 2 Specific Codes
4. Other Method/model Codes, if any

# **Installing/Importing All Required Libraries**
"""

!pip install transformers

import pandas as pd
import numpy as np
import pickle 
import os
import io 
import spacy
import re
import string
import matplotlib.pyplot as plt
import seaborn as sns
nlp = spacy.load("en_core_web_sm")
stop_words = nlp.Defaults.stop_words
punctuations = string.punctuation
from sklearn import svm
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score, classification_report, precision_score, recall_score
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

"""Assigning student id as a variable to set as seed """

student_id = 2200940
np.random.seed(student_id)

"""# **Common Codes**

Outline of this section,

* Reading all data files
* Splitting train data
* Defining Performance Matrics function
* Printing Dataset Statistics
* Data Visualization

First allowing the GDrive access and setting data and model paths
"""

# Mount Google Drive
from google.colab import drive
drive.mount('/content/gdrive', force_remount=True)

GOOGLE_DRIVE_PATH_AFTER_MYDRIVE = os.path.join('./CE807/Assignment2/',str(student_id)) # Make sure to update with your student_id and student_id is an integer
GOOGLE_DRIVE_PATH = os.path.join('gdrive', 'MyDrive', GOOGLE_DRIVE_PATH_AFTER_MYDRIVE)
print('List files: ', os.listdir(GOOGLE_DRIVE_PATH))

train_file = os.path.join(GOOGLE_DRIVE_PATH, 'train.csv') # This is 100% of data
train_25_file = os.path.join(GOOGLE_DRIVE_PATH, 'train_25.csv') # This is 25% of data
train_50_file = os.path.join(GOOGLE_DRIVE_PATH, 'train_50.csv') # This is 50% of data
train_75_file = os.path.join(GOOGLE_DRIVE_PATH, 'train_75.csv') # This is 75% of data
train_100_file = os.path.join(GOOGLE_DRIVE_PATH, 'train_100.csv') # This is also 100% of data as train.csv
  
######################################################################################3
print('-'*100)
print('Train file: ', train_file)
print('Train 25% file: ', train_25_file)
print('Train 50% file: ', train_50_file)
print('Train 75% file: ', train_75_file)
print('Train 100% file: ', train_100_file)

val_file = os.path.join(GOOGLE_DRIVE_PATH, 'valid.csv')
print('Validation file: ', val_file)

test_file = os.path.join(GOOGLE_DRIVE_PATH, 'test.csv')
print('Test file: ', test_file)

#################################################################################################################
print('-'*100)
MODEL_1_DIRECTORY = os.path.join(GOOGLE_DRIVE_PATH, 'models', '1') # Model 1 directory
print('Model 1 directory: ', MODEL_1_DIRECTORY)

MODEL_1_25_DIRECTORY = os.path.join(MODEL_1_DIRECTORY,'25') # Model 1 trained using 25% of train data directory
print('Model 1 directory with 25% data: ', MODEL_1_25_DIRECTORY)

MODEL_1_50_DIRECTORY = os.path.join(MODEL_1_DIRECTORY,'50') # Model 1 trained using 50% of train data directory
print('Model 1 directory with 50% data: ', MODEL_1_50_DIRECTORY)

MODEL_1_75_DIRECTORY = os.path.join(MODEL_1_DIRECTORY,'75') # Model 1 trained using 75% of train data directory
print('Model 1 directory with 75% data: ', MODEL_1_75_DIRECTORY)

MODEL_1_100_DIRECTORY = os.path.join(MODEL_1_DIRECTORY,'100') # Model 1 trained using 100% of train data directory
print('Model 1 directory with 100% data: ', MODEL_1_100_DIRECTORY)

#################################################################################################################
print('-'*100)
MODEL_2_DIRECTORY = os.path.join(GOOGLE_DRIVE_PATH, 'models', '2') # Model 1 directory
print('Model 2 directory: ', MODEL_2_DIRECTORY)

MODEL_2_25_DIRECTORY = os.path.join(MODEL_2_DIRECTORY,'25') # Model 1 trained using 25% of train data directory
print('Model 2 directory with 25% data: ', MODEL_2_25_DIRECTORY)

MODEL_2_50_DIRECTORY = os.path.join(MODEL_2_DIRECTORY,'50') # Model 1 trained using 50% of train data directory
print('Model 2 directory with 50% data: ', MODEL_2_50_DIRECTORY)

MODEL_2_75_DIRECTORY = os.path.join(MODEL_2_DIRECTORY,'75') # Model 1 trained using 75% of train data directory
print('Model 2 directory with 75% data: ', MODEL_2_75_DIRECTORY)

MODEL_2_100_DIRECTORY = os.path.join(MODEL_2_DIRECTORY,'100') # Model 1 trained using 100% of train data directory
print('Model 2 directory with 100% data: ', MODEL_2_100_DIRECTORY)

#####################################################################################################################
print('-'*100)
model_1_25_output_test_file = os.path.join(MODEL_1_25_DIRECTORY, 'output_test.csv') # Output file using Model 1 trained using 25% of train data 
print('Output file name using model 1 using 25% of train data: ',model_1_25_output_test_file)

model_1_50_output_test_file = os.path.join(MODEL_1_50_DIRECTORY, 'output_test.csv') # Output file using Model 1 trained using 50% of train data 
print('Output file name using model 1 using 50% of train data: ',model_1_50_output_test_file)

model_1_75_output_test_file = os.path.join(MODEL_1_75_DIRECTORY, 'output_test.csv') # Output file using Model 1 trained using 75% of train data 
print('Output file name using model 1 using 75% of train data: ',model_1_75_output_test_file)

model_1_100_output_test_file = os.path.join(MODEL_1_100_DIRECTORY, 'output_test.csv') # Output file using Model 1 trained using 100% of train data 
print('Output file name using model 1 using 100% of train data: ',model_1_100_output_test_file)

##########################################################################################################################
print('-'*100)
model_2_25_output_test_file = os.path.join(MODEL_2_25_DIRECTORY, 'output_test.csv') # Output file using Model 1 trained using 25% of train data 
print('Output file name using model 2 using 25% of train data: ',model_2_25_output_test_file)

model_2_50_output_test_file = os.path.join(MODEL_2_50_DIRECTORY, 'output_test.csv') # Output file using Model 1 trained using 50% of train data 
print('Output file name using model 2 using 50% of train data: ',model_2_50_output_test_file)

model_2_75_output_test_file = os.path.join(MODEL_2_75_DIRECTORY, 'output_test.csv') # Output file using Model 1 trained using 75% of train data 
print('Output file name using model 2 using 75% of train data: ',model_2_75_output_test_file)

model_2_100_output_test_file = os.path.join(MODEL_2_100_DIRECTORY, 'output_test.csv') # Output file using Model 1 trained using 100% of train data 
print('Output file name using model 2 using 100% of train data: ',model_2_100_output_test_file)

"""## Reading all data files

Here I am reading and printing the train, valid & test data files, where I am showing each data files, features and their shape.
"""

train = pd.read_csv(train_file)
valid = pd.read_csv(val_file)
test = pd.read_csv(test_file)

print("-"*70)
print("\t\t\t\tTrain Data")
print("-"*70)
print(train)
print("-"*70)
print("\t\t\t\tValid Data")
print("-"*70)
print(valid)
print("-"*70)
print("\t\t\t\tTest Data")
print("-"*70)
print(test)
print("-"*70)

"""## Splitting train data into 25%,50%,75%,100%

Firstly, I am splitting train data into four parts as each 25%. Then I am adding splitted data as required 25%, 50%,75% & 100%.
"""

#split the data into four equal parts of 25% each
split_1, split_2, split_3, split_4 = np.array_split(train, 4)

train_25 = split_1
train_50 = pd.concat((train_25, split_2))
train_75 = pd.concat((train_50, split_3))
train_100 = pd.concat((train_75, split_4)) 

print("Original Train Data Shape:",train.shape)
print("-"*45)
print("Splitting train data into four equal parts:")
print("-"*45)
#print the shapes of the resulting splits
print("Split_1 Shape:",split_1.shape)  # should be (3078, 3)
print("Split_2 Shape:",split_2.shape)  # should be (3078, 3)
print("Split_3 Shape:",split_3.shape)  # should be (3078, 3)
print("Split_4 Shape:",split_4.shape)  # should be (3078, 3)
print("-"*45)
print("Adding the splitted data as required:")
print("-"*45)
print("Train 25% Shape:",train_25.shape)  # should be (3078, 3)
print("Train 50% Shape:",train_50.shape)  # should be (3078, 3)
print("Train 75% Shape:",train_75.shape)  # should be (3078, 3)
print("Train 100% Shape:",train_100.shape)# should be (3078, 3)

"""**Note:** The train data has splitted equally as each 25% and then added the splitted data as required file size.

### Saving the Splitted data

Here I am saving the different size of train data in the required directory path.
"""

train_25.to_csv('/content/gdrive/MyDrive/CE807/Assignment2/2200940/' + 'train_25.csv', index=False)
train_50.to_csv('/content/gdrive/MyDrive/CE807/Assignment2/2200940/' + 'train_50.csv', index=False)
train_75.to_csv('/content/gdrive/MyDrive/CE807/Assignment2/2200940/' + 'train_75.csv', index=False)
train_100.to_csv('/content/gdrive/MyDrive/CE807/Assignment2/2200940/' + 'train_100.csv', index=False)

"""## Performance Matrics

Here I am defining the function to compute the performance matrics of all required data files like Accuracy, Recall (macro), Precision (macro), F1 (macro) and Confusion Matrix for the performance evaluation.
"""

def compute_performance(y_true, y_pred, split='test'):
    """
    prints different performance matrics like  Accuracy, Recall (macro), Precision (macro), and F1 (macro).
    This also display Confusion Matrix with proper X & Y axis labels.
    Also, returns F1 score

    Args:
        y_true: numpy array or list
        y_pred: numpy array or list
        split: str
        

    Returns:
        float
    """

    print('Computing different preformance metrics on', split,'set of Dataset')
    f1score=f1_score(y_true, y_pred, average='macro')
    acc = accuracy_score(y_true, y_pred)
    cnf = confusion_matrix(y_true, y_pred)
    rec = recall_score(y_true, y_pred, average='macro')
    pre = precision_score(y_true, y_pred, average='macro')
    cls = classification_report(y_true, y_pred)

    print('-'*60)
    print('F1 Score(macro): ', f1score)
    print('Accuracy: ', acc)
    print('Confusion Matrix:')
    print(cnf)
    print('Precision(macro):', pre)
    print('Recall(macro):', rec)
    print('_________________________Classification Report__________________________')
    print(cls)
    print('-'*60)

    return f1score

"""## Dataset Statistics

Here, I am printing the quick summary of a data files, which includs its shape, data types, and memory usage by using **.info()**.
"""

print('-'*40)
print("\t\tTrain Data")
print('-'*40)
train.info()
print('-'*40)
print("\t\tValid Data")
print('-'*40)
valid.info()
print('-'*40)
print('\t\tTest Data')
print('-'*40)
test.info()
print('-'*40)

"""Here I am printing the summary statistics such as mean, median, mode, standard deviation, minimum, and maximum values of train,valid & test datas by using **.describe()**."""

print('-'*30)
print("\tTrain Data")
print('-'*30)
print(train.describe())
print('-'*30)
print("\tValid Data")
print('-'*30)
print(valid.describe())
print('-'*30)
print('\tTest Data')
print('-'*30)
print(test.describe())
print('-'*30)

"""**Note:** Only id feature is int type.

Here, I am displaying the frequency of each unique string value in a column of train,valid & test data files by using **.value_counts()**.
"""

print('-'*30)
print("\tTrain Data")
print('-'*30)
print(train['label'].value_counts())
print('-'*30)
print("\tValid Data")
print('-'*30)
print(valid['label'].value_counts())
print('-'*30)
print('\tTest Data')
print('-'*30)
print(test['label'].value_counts())
print('-'*30)

"""**Note:** From the above value count of label column, we can see that these data sets are imbalanced. So to balance this ,I am using the resampling method for which I have defined a function in the preprocessing part(given below in Method 1 section).

**Data Visualization**

Here, visualizing the distribution of label counts of train, valid & test datasets.
"""

# Data for the pie charts
label_counts1 = train['label'].value_counts()
label_counts2 = valid['label'].value_counts()
label_counts3 = test['label'].value_counts()

# Create a figure with 3 subplots in a single row
fig, axs = plt.subplots(1, 3, figsize=(10, 5))
clr=['c','m']
myexplode = [0.1, 0]

# Plot the first pie chart
axs[0].pie(label_counts1, labels=label_counts1.index,explode = myexplode, colors= clr, autopct='%.1f%%', startangle=90)
axs[0].set_title('Train Data')
axs[0].axis('equal')

# Plot the second pie chart
axs[1].pie(label_counts2, labels=label_counts2.index,explode = myexplode, colors= clr, autopct='%1.1f%%', startangle=90)
axs[1].set_title('Valid Data')
axs[1].axis('equal')

# Plot the third pie chart
axs[2].pie(label_counts3, labels=label_counts3.index,explode = myexplode, colors= clr, autopct='%1.1f%%', startangle=90)
axs[2].set_title('Test Data')
axs[2].axis('equal')

# Add an overall title for the figure
fig.suptitle('Overall Distribution of Tweet Labels',y=1.05)

# Set the layout of the subplots
plt.tight_layout()

# Display the plot
plt.show()

"""Here, visualizing sizes of splitted train data sets"""

# Data for the bar chart
sizes = [train_25.shape[0], train_50.shape[0], train_75.shape[0], train_100.shape[0]]
labels = ['25%', '50%', '75%', '100%']

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(8, 5))
ax.barh(labels, sizes)
colors = ['salmon', 'indianred', 'firebrick', 'maroon']

#Create a horizontal bar chart
plt.barh(labels, sizes, color=colors)

# Add a title and labels to the chart
ax.set_title('Sizes of splitted train data sets')
ax.set_xlabel('Size')
ax.set_ylabel('Train Data')

# Display the plot
plt.show()

"""# Method 1

Outline of the this section:

* Data cleaning
* Handling Imbalanced data
* Converting data into Vectorization
* Model Initialization
* Training and validating a model using training and validation dataset
* Saving a trained model
* Training with different splitted data size
* Loading a model and vectorizer from disk
* Testing the model on testing set and saving the output of the model
* Testing with different splitted data size

**Data Cleaning**
"""

# Creating the function
def spacy_tokenizer1(text):
     #Creating our token object, which is used to create documents with linguistic annotations.
    doc = nlp(text)

    # Lemmatizing each token and converting each token into lowercase
    mytokens = [word.lemma_.lower().strip() for word in doc]

    # Removing stop words and punctuations
    mytokens = [word for word in mytokens if word not in stop_words and word not in punctuations]

    # Cleaning the text
    cleaned_text = re.sub(r"(@[A-Za-z0-a]+)|([^0-9A-Za-z \t])|(\w+:\/\/\s+)|^rt|http.+?","", ' '.join(mytokens))

    # Return preprocessed list of tokens
    return cleaned_text

"""Below, I am showing that how the above defined *spacy_tokenizer1* function works to clean the data. Here, I have shown only train data, similar to this, all other datas will be cleaned, which will process in *train_method1* function in training model. """

train['tokenized_tweet']=train['tweet'].apply(spacy_tokenizer1)
train.head()

"""**Handling Imbalanced data**"""

from sklearn.utils import resample
import pandas as pd

def upsample1(df, label_column):
  # convert the string into int
  label_int= {"label": {"NOT":0, "OFF":1}}
  df_int = df.replace(label_int, inplace=False)
   
  # Separate the majority and minority classes
  majority_class=df_int[df_int[label_column]==0]
  minority_class=df_int[df_int[label_column]==1]

  # Upsample the minority class to match the number of samples in the majority class
  minority_upsampled = resample(minority_class, replace=True, n_samples=len(majority_class), random_state=123)

  # Concatenate the upsampled minority class and the majority class
  upsampled_df = pd.concat([minority_upsampled, majority_class])

  label_str= {"label": {0:"NOT", 1:"OFF"}}
  df_str = upsampled_df.replace(label_str, inplace=False)
   
  return df_str

"""Below, I have given table of comparing label-counts of train data before & after resampling, to show how the above defined sampling function works."""

train_25_bln=upsample1(train_25,'label')
train_50_bln=upsample1(train_50,'label')
train_75_bln=upsample1(train_75,'label')
train_100_bln=upsample1(train_100,'label') 
# table
from tabulate import tabulate
table_data = [['Sizes', 'Before Resampling', 'After Resampling' ],
            ['train 25%' , train_25['label'].value_counts(), train_25_bln['label'].value_counts() ],
            ['train 50%', train_50['label'].value_counts(),  train_50_bln['label'].value_counts()],
            ['train 75%' , train_75['label'].value_counts(), train_75_bln['label'].value_counts() ],
            ['train 100%',  train_100['label'].value_counts(),  train_100_bln['label'].value_counts()]]            
print(tabulate(table_data, headers= "firstrow", tablefmt="fancy_grid"))

"""**Converting data into Vectorization**"""

def prepare_dataset1(data, vectorizer=None, split='test'):
  if split == 'train':
    vectorizer = TfidfVectorizer() 
    values = vectorizer.fit_transform(data['tweet'].values) #TODO: This is the best way to do this, because you need to use same vectorization method
  else:
    values = vectorizer.transform(data['tweet'].values)

  if split == 'train':
    return values, vectorizer
  else:
    return values

"""Below, I have shown that how the above defined *prepare_dataset1* function works"""

train_values, vectorizer = prepare_dataset1(train, split='train')
train_values, vectorizer

"""**Model Initialization**

RBF SVM (Radial Basis Function Support Vector Machine)
"""

def train_model1(text_vector,label):
  print('Let\'s start training Radial Basis Function Support Vector Machine')
  classifier = svm.SVC(kernel='rbf')
  classifier.fit(text_vector, label)
  #kernel = RBF(length_scale=1.0)
  #classifier = GaussianProcessRegressor()
  #classifier.fit(text_vector, label)

  return classifier

"""**Training and validating a model using training and validation dataset**

Here, the train_method1 function followed a standard ML pipeline:
* Data reading
* Data clearning
* Convert data to vector/tokenization/vectorization
* Model Declaration/Initialization/building
* Training and validation of the model using training and validation dataset
* Save the trained model
* Load and Test the model on testing set
* Save the output of the model
"""

def train_method1(train_file, val_file, model_dir):
    """
     Takes train_file, val_file and model_dir as input.
     It trained on the train_file datapoints, and validate on the val_file datapoints.
     While training and validating, it print different evaluataion metrics and losses, wheverever necessary.
     After finishing the training, it saved the best model in the model_dir.

     ADD Other arguments, if needed.

    Args:
        train_file: Train file name
        val_file: Validation file name
        model_dir: Model output Directory
    
    """
    train_df = pd.read_csv(train_file)
    val_df = pd.read_csv(val_file)
    print("-----------------Data Shape before sampling-----------------")
    print("Train Data Shape:", train_df.shape)
    print("Valid Data Shape:", val_df.shape)

    train_df['tweet']=train_df['tweet'].apply(spacy_tokenizer1)
    val_df['tweet']=val_df['tweet'].apply(spacy_tokenizer1)
    
    train_df = upsample1(train_df, 'label')
    val_df = upsample1(val_df, 'label')
    print("-----------------Data Shape after sampling------------------")

    print("Train Data Shape:", train_df.shape)
    print("Valid Data Shape:", val_df.shape)
    print("-"*60)

    train_label = train_df['label']
    val_label = val_df['label']
    
    train_values, vectorizer = prepare_dataset1(train_df, split='train') 
    val_values= prepare_dataset1(val_df,vectorizer)

    model = train_model1(train_values,train_label)

    model_file, vectorizer_file = save_model1(model, vectorizer, model_dir)

    train_pred_label = model.predict(train_values)
    val_pred_label = model.predict(val_values)

    # print('Train Split')
    train_f1_score = compute_performance(train_label, train_pred_label, split='train')

    # print('Validation Split')
    val_f1_score = compute_performance(val_label, val_pred_label, split='valid')


    return model_file, vectorizer_file

"""**Saving a trained model**"""

def save_model1(model, vectorizer, model_dir):
    # save the model to disk
    model_file = os.path.join(model_dir, 'model.sav')
    pickle.dump(model, open(model_file, 'wb'))

    print('Saved model to ', model_file)

    vectorizer_file = os.path.join(model_dir, 'vectorizer.sav') 
    pickle.dump(vectorizer, open(vectorizer_file, 'wb'))

    print('Saved Vectorizer to ', vectorizer_file)
    print('-'*60)

    return model_file, vectorizer_file

"""### **Training with different splitted data size**"""

print('Train using of 25% of data')
model_25_file, vectorizer_25_file = train_method1(train_25_file, val_file, MODEL_1_25_DIRECTORY)

print('Train using of 50% of data')
model_50_file, vectorizer_50_file = train_method1(train_50_file, val_file, MODEL_1_50_DIRECTORY)

print('Train using of 75% of data')
model_75_file, vectorizer_75_file = train_method1(train_75_file, val_file, MODEL_1_75_DIRECTORY)

print('Train using of 100% of data')
model_100_file, vectorizer_100_file = train_method1(train_100_file, val_file, MODEL_1_100_DIRECTORY)

"""**Loading a model and vectorizer from disk**"""

def load_model1(model_file, vectorizer_file):
    # load model and vectorizer from disk

    model = pickle.load(open(model_file, 'rb'))

    print('Loaded model from ', model_file)

    vectorizer = pickle.load(open(vectorizer_file, 'rb'))

    print('Loaded Vectorizer from ', vectorizer_file)
    print('-'*60)


    return model, vectorizer

"""**Testing the model on testing set and saving the output of the model**


"""

def test_method1(test_file, model_file, vectorizer_file, output_dir):
    """
     take test_file, model_file and output_dir as input.
     It loads model and test of the examples in the test_file.
     It prints different evaluation metrics, and saves the output in output directory

     ADD Other arguments, if needed

    Args:
        test_file: Test file name
        model_file: Model file name
        vectorizer_file: Vectorizer file name
        output_dir: Output Directory
    
    """

    test_df = pd.read_csv(test_file)

    test_df['tweet']=test_df['tweet'].apply(spacy_tokenizer1)
    
    test_df = upsample1(test_df, 'label')
    
    test_label = test_df['label']

    model, vectorizer = load_model1(model_file, vectorizer_file) 

    test_values= prepare_dataset1(test_df,vectorizer)

    test_pred_label = model.predict(test_values)

    test_df['out_label']  = test_pred_label # Note how this is saved 

    test_f1_score = compute_performance(test_label, test_pred_label, split='test')

    out_file = os.path.join(output_dir, 'output_test.csv')

    print('Saving model output to', out_file)
    test_df.to_csv(out_file)

    
    # return

"""### **Testing with different splitted data size**"""

print('Testing using model trained on 25% data')
test_method1(test_file, model_25_file, vectorizer_25_file, MODEL_1_25_DIRECTORY)

print('Testing using model trained on 50% data')
test_method1(test_file, model_50_file, vectorizer_50_file, MODEL_1_50_DIRECTORY)

print('Testing using model trained on 75% data')
test_method1(test_file, model_75_file, vectorizer_75_file, MODEL_1_75_DIRECTORY)

print('Testing using model trained on 100% data')
test_method1(test_file, model_100_file, vectorizer_100_file, MODEL_1_100_DIRECTORY)

"""# **Method 2**

Outline of this section:

* Data cleaning
* Handling Imbalanced data
* Converting data into Vectorization
* Model Initialization
* Training and validating a model using training and validation dataset
* Saving a trained model
* Training with different splitted data size
* Loading a model and vectorizer from disk
* Testing the model on testing set and saving the output of the model
* Testing with different splitted data size

**Note:** In this section, pre-processing will be done similar to Method 1 section, i.e., Data cleaning, Handling Imbalanced data, converting data into vectorization,etc..

**Data Cleaning**
"""

# Creating the function
def spacy_tokenizer2(text):
    # Creating our token object, which is used to create documents with linguistic annotations.
    doc = nlp(text)

    # Lemmatizing each token and converting each token into lowercase
    mytokens = [word.lemma_.lower().strip() for word in doc]

    # Removing stop words and punctuations
    mytokens = [word for word in mytokens if word not in stop_words and word not in punctuations]

    # Cleaning the text
    cleaned_text = re.sub(r"(@[A-Za-z0-a]+)|([^0-9A-Za-z \t])|(\w+:\/\/\s+)|^rt|http.+?","", ' '.join(mytokens))

    # Return preprocessed list of tokens
    return cleaned_text

"""**Handling Imbalanced data**"""

from sklearn.utils import resample
import pandas as pd

def upsample2(df, label_column):
   
   # convert the string into int
   label_int= {"label": {"NOT":0, "OFF":1}}
   df_int = df.replace(label_int, inplace=False)
   
   # Separate the majority and minority classes
   majority_class=df_int[df_int[label_column]==0]
   minority_class=df_int[df_int[label_column]==1]

   # Upsample the minority class to match the number of samples in the majority class
   minority_upsampled = resample(minority_class, replace=True, n_samples=len(majority_class), random_state=123)

   # Concatenate the upsampled minority class and the majority class
   upsampled_df = pd.concat([minority_upsampled, majority_class])

   label_str= {"label": {0:"NOT", 1:"OFF"}}
   df_str = upsampled_df.replace(label_str, inplace=False)
   
   return df_str

"""**Converting data into Vectorization**"""

def prepare_dataset2(data, vectorizer=None, split='test'):
  if split == 'train':
      vectorizer = TfidfVectorizer() 
      values = vectorizer.fit_transform(data['tweet'].values) #TODO: This is the best way to do this, because you need to use same vectorization method
  else:
      values = vectorizer.transform(data['tweet'].values)

  if split == 'train':
      return values, vectorizer
  else:
      return values

"""**Model Initialization**"""

def train_model2(text_vector,label):

    print('Let\'s start training Extra Trees Classifier')
    classifier = ExtraTreesClassifier(n_estimators=100)
    classifier.fit(text_vector, label)

    return classifier

"""**Training and validating a model using training and validation dataset**

Here, the train_method2 function followed a standard ML pipeline:
* Data reading
* Data clearning
* Convert data to vector/tokenization/vectorization
* Model Declaration/Initialization/building
* Training and validation of the model using training and validation dataset
* Save the trained model
* Load and Test the model on testing set
* Save the output of the model
"""

def train_method2(train_file, val_file, model_dir):
    """
     Takes train_file, val_file and model_dir as input.
     It trained on the train_file datapoints, and validate on the val_file datapoints.
     While training and validating, it print different evaluataion metrics and losses, wheverever necessary.
     After finishing the training, it saved the best model in the model_dir.

     ADD Other arguments, if needed.

    Args:
        train_file: Train file name
        val_file: Validation file name
        model_dir: Model output Directory
    
    """
    train_df = pd.read_csv(train_file)
    val_df = pd.read_csv(val_file)
    print("-----------------Data Shape before sampling--------------")
    print("Train Data Shape:", train_df.shape)
    print("Valid Data Shape:", val_df.shape)

    train_df['tweet']=train_df['tweet'].apply(spacy_tokenizer2)
    val_df['tweet']=val_df['tweet'].apply(spacy_tokenizer2)

    train_df = upsample2(train_df, 'label')
    val_df = upsample2(val_df, 'label')
    print("-----------------Data Shape after sampling--------------")

    print("Train Data Shape:", train_df.shape)
    print("Valid Data Shape:", val_df.shape)
    print("-"*60)

    train_label = train_df['label']
    val_label = val_df['label']

    train_values, count_vectorizer = prepare_dataset2(train_df, split='train') 
    val_values= prepare_dataset2(val_df,count_vectorizer)

    model = train_model2(train_values,train_label)

    model_file, vectorizer_file = save_model2(model, count_vectorizer, model_dir)

    train_pred_label = model.predict(train_values)
    val_pred_label = model.predict(val_values)

    # print('Train Split')
    train_f1_score = compute_performance(train_label, train_pred_label, split='train')

    # print('Validation Split')
    val_f1_score = compute_performance(val_label, val_pred_label, split='valid')


    return model_file, vectorizer_file

"""**Saving a trained model**"""

def save_model2(model, vectorizer, model_dir):
    # save the model to disk
    model_file = os.path.join(model_dir, 'model.sav')
    pickle.dump(model, open(model_file, 'wb'))

    print('Saved model to ', model_file)

    vectorizer_file = os.path.join(model_dir, 'vectorizer.sav') 
    pickle.dump(vectorizer, open(vectorizer_file, 'wb'))

    print('Saved Vectorizer to ', vectorizer_file)
    print('-------------------------------------------------------------')

    return model_file, vectorizer_file

"""### **Training with different splitted data size**"""

print('Train using of 25% of data')
model_25_file, vectorizer_25_file = train_method2(train_25_file, val_file, MODEL_2_25_DIRECTORY)

print('Train using of 50% of data')
model_50_file, vectorizer_50_file = train_method2(train_50_file, val_file, MODEL_2_50_DIRECTORY)

print('Train using of 75% of data')
model_75_file, vectorizer_75_file = train_method2(train_75_file, val_file, MODEL_2_75_DIRECTORY)

print('Train using of 100% of data')
model_100_file, vectorizer_100_file = train_method2(train_100_file, val_file, MODEL_2_100_DIRECTORY)

"""### Testing code

**Loading a model and vectorizer from disk**
"""

def load_model2(model_file, vectorizer_file):
    # load model and vectorizer from disk

    model = pickle.load(open(model_file, 'rb'))

    print('Loaded model from ', model_file)

    vectorizer = pickle.load(open(vectorizer_file, 'rb'))

    print('Loaded Vectorizer from ', vectorizer_file)
    print('-'*60)


    return model, vectorizer

"""**Testing the model on testing set and saving the output of the model**"""

def test_method2(test_file, model_file, vectorizer_file, output_dir):
    """
     take test_file, model_file and output_dir as input.
     It loads model and test of the examples in the test_file.
     It prints different evaluation metrics, and saves the output in output directory

     ADD Other arguments, if needed

    Args:
        test_file: Test file name
        model_file: Model file name
        vectorizer_file: Vectorizer file name
        output_dir: Output Directory
    
    """

    test_df = pd.read_csv(test_file)
    
    test_df['tweet']=test_df['tweet'].apply(spacy_tokenizer2)
    
    test_df = upsample2(test_df, 'label')
    
    test_label = test_df['label']

    model, vectorizer = load_model2(model_file, vectorizer_file) 

    test_values= prepare_dataset2(test_df,vectorizer)

    test_pred_label = model.predict(test_values)

    test_df['out_label']  = test_pred_label # Note how this is saved 

    test_f1_score = compute_performance(test_label, test_pred_label, split='test')

    out_file = os.path.join(output_dir, 'output_test.csv')

    print('Saving model output to', out_file)
    test_df.to_csv(out_file)

    
    # return

"""**Testing with different splitted data size**"""

print('Testing using model trained on 25% data')
test_method2(test_file, model_25_file, vectorizer_25_file, MODEL_2_25_DIRECTORY)

print('Testing using model trained on 50% data')
test_method2(test_file, model_50_file, vectorizer_50_file, MODEL_2_50_DIRECTORY)

print('Testing using model trained on 75% data')
test_method2(test_file, model_75_file, vectorizer_75_file, MODEL_2_75_DIRECTORY)

print('Testing using model trained on 100% data')
test_method2(test_file, model_100_file, vectorizer_100_file, MODEL_2_100_DIRECTORY)

"""# **Model Selection**

**Note:** I have runned all these below given codes in each seperate files to select a best model by evaluating their:
* score
* training time
* prediction time
* confusion_matrix.

While running along with the above two models, my session was crashed after using all available RAM. So, I have just given below the used codes for model selection.

import pandas as pd
import seaborn as sns
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from sklearn.linear_model import SGDClassifier
!pip install -U sentence-transformers -q
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')

names = ["Nearest_Neighbors", "Linear_SVM", "Polynomial_SVM", "RBF_SVM", "Gaussian_Process",
         "Gradient_Boosting", "Decision_Tree", "Extra_Trees", "Random_Forest", "Neural_Net", "AdaBoost",
         "Naive_Bayes", "QDA", "SGD"]

classifiers = [
    KNeighborsClassifier(3),
    SVC(kernel="linear", C=0.025),
    SVC(kernel="poly", degree=3, C=0.025),
    SVC(kernel="rbf", C=1, gamma=2),
    GaussianProcessClassifier(1.0 * RBF(1.0)),
    GradientBoostingClassifier(n_estimators=100, learning_rate=1.0),
    DecisionTreeClassifier(max_depth=5),
    ExtraTreesClassifier(n_estimators=10, min_samples_split=2),
    RandomForestClassifier(max_depth=5, n_estimators=100),
    MLPClassifier(alpha=1, max_iter=1000),
    AdaBoostClassifier(n_estimators=100),
    GaussianNB(),
    QuadraticDiscriminantAnalysis(),
    SGDClassifier(loss="hinge", penalty="l2")]

# read in the train, validation, and test data sets as separate data frames
train_data = pd.read_csv(train_file)
valid_data = pd.read_csv(val_file)
test_data = pd.read_csv(test_file)

# concatenate the train and validation data frames vertically
combined_data = pd.concat([train_data, valid_data], ignore_index=True)
"

combined_data['tweet']=combined_data['tweet'].apply(spacy_tokenizer2)
combined_data

combined_data = upsample2(combined_data, 'label')
combined_data.shape

combined_data['tweet'] = combined_data['tweet'].apply(model.encode)
combined_data.head()

# convert the string into int
label_int= {"label": {"NOT":0, "OFF":1}}
combined_data_int = combined_data.replace(label_int, inplace=False)

X =combined_data_int['tweet'].to_list()
Y = combined_data_int['label'].to_list()

# split the combined data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2,stratify=Y, 
                                                    random_state=2200940)

scores = []
for name, clf in zip(names, classifiers):
    #clf.fit(x_train, y_train)
    #score = clf.score(x_test, y_test)
    #scores.append(score)

scores

head = 10
for model in classifiers[:head]:
    start = time()
    model.fit(X_train, Y_train)
    train_time = time() - start
    start = time()
    Y_pred = model.predict(X_test)
    predict_time = time()-start    
    print(model)
    print("\tTraining time: %0.3fs" % train_time)
    print("\tPrediction time: %0.3fs" % predict_time)
    print("\tAccuracy :", accuracy_score(Y_test, Y_pred))
    print("\tf1_score:", f1_score(Y_test, Y_pred))
    print("\tConfusion Matrix:", confusion_matrix(Y_test, Y_pred))
    print()

df = pd.DataFrame()
df['name'] = names
df['score'] = scores
df

cm = sns.light_palette("green", as_cmap=True)
s = df.style.background_gradient(cmap=cm)
s

sns.set(style="whitegrid")
ax = sns.barplot(y="name", x="score", data=df)
"""