# Basic_Sentiment_Analysis---ML-project---classification

## Acknowledgements

I would like to extend my deepest thanks to the YouTube channel **[CodePro LK](https://www.youtube.com/@codeprolk)** for their motivation and knowledge sharing. Their tutorials and insights have played a crucial role in helping me understand and implement various techniques for this project.

## Project Overview

This project is focused on **Text Classification and Machine Learning**. The primary goal is to build a model capable of classifying text data into categories such as **positive** or **negative** using various classification algorithms.

### Technologies Used:

- **Python**: The main programming language used for implementing the machine learning models.
- **Flask**: A web framework for building the web service to serve the machine learning model.
- **Jupyter Notebook**: Used for model development, data exploration, and analysis.
- **Scikit-learn**: A machine learning library used for various classification algorithms like Logistic Regression, Naive Bayes, Decision Tree, Random Forest, and Support Vector Machine (SVM).
- **Natural Language Processing (NLP)**: Techniques such as text preprocessing, tokenization, stemming, and vectorization were used to prepare the text data for training.

### Machine Learning Models

I have used the following classifiers to predict whether a given text is positive or negative:

1. **Logistic Regression**  
2. **Multinomial Naive Bayes (MNB)**  
3. **Decision Tree Classifier (DT)**  
4. **Random Forest Classifier (RF)**  
5. **Support Vector Machine (SVM)**  

For each classifier, I performed training and evaluation on the dataset. Here are the training and testing scores for each model:

#### Logistic Regression:
- **Training Scores**:
    - Accuracy: 0.939
    - Precision: 0.915
    - Recall: 0.969
    - F1-Score: 0.941
- **Testing Scores**:
    - Accuracy: 0.872
    - Precision: 0.716
    - Recall: 0.842
    - F1-Score: 0.774

#### Multinomial Naive Bayes:
- **Training Scores**:
    - Accuracy: 0.907
    - Precision: 0.869
    - Recall: 0.957
    - F1-Score: 0.911
- **Testing Scores**:
    - Accuracy: 0.869
    - Precision: 0.684
    - Recall: 0.92
    - F1-Score: 0.784

#### Decision Tree Classifier:
- **Training Scores**:
    - Accuracy: 1.0
    - Precision: 1.0
    - Recall: 0.999
    - F1-Score: 1.0
- **Testing Scores**:
    - Accuracy: 0.836
    - Precision: 0.691
    - Recall: 0.664
    - F1-Score: 0.677

#### Random Forest Classifier:
- **Training Scores**:
    - Accuracy: 1.0
    - Precision: 1.0
    - Recall: 1.0
    - F1-Score: 1.0
- **Testing Scores**:
    - Accuracy: 0.867
    - Precision: 0.76
    - Recall: 0.71
    - F1-Score: 0.735

#### Support Vector Machine:
- **Training Scores**:
    - Accuracy: 0.977
    - Precision: 0.96
    - Recall: 0.994
    - F1-Score: 0.977
- **Testing Scores**:
    - Accuracy: 0.883
    - Precision: 0.755
    - Recall: 0.815
    - F1-Score: 0.784

### Machine Learning Workflow

1. **Text Preprocessing**:
   - Removed punctuation and digits from the text.
   - Tokenized and stemmed the text using the **Porter Stemmer**.
   - Removed stopwords and URLs.

2. **Vectorization**:
   - The text data was transformed into vectors using a custom vectorizer, which converts text into numerical representation based on vocabulary.

3. **Model Training and Evaluation**:
   - The machine learning models were trained using the processed data.
   - For evaluation, metrics such as **Accuracy**, **Precision**, **Recall**, and **F1-Score** were calculated for both training and testing datasets.

### Machine Learning Techniques

The **Machine Learning (ML) part** is the core of this project, where I used various classification algorithms to predict the sentiment of text data. I trained each model on the **preprocessed text data**, and evaluated their performance using different scoring metrics.

- **Training and Testing Scores**: These metrics were crucial in evaluating how well the models performed, and I have included the performance results for each model.
  
## Conclusion

Through this project, I have learned a lot about machine learning algorithms, text preprocessing, and model evaluation. The process of implementing and evaluating multiple classifiers has helped me better understand the strengths and weaknesses of each algorithm when applied to sentiment analysis tasks.

---

### References

- [CodePro LK - YouTube Channel](https://www.youtube.com/@codeprolk)
