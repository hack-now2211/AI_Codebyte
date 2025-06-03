# AI Codebyte Submission

This repository contains the solutions to the AI Internship Test, divided into three sections: Python & Data Manipulation, Machine Learning, and AI/ML Application & Thinking.

## Project Structure

The project is organized into three main folders, `SA`, `SB`, and `SC`, corresponding to Sections A, B, and C of the test.

```
AI_Codebyte/
├── SA/
│ ├── SA_Q1.py
│ ├── SA_Q2.py
│ └── student_scores.csv
├── SB/
│ ├── SB_Q3.py
│ ├── SB_Q4.py
│ └── simple_housing.csv
└── SC/
    ├── SC_Q5.txt
    └── SC_Q6.py
```

## How to Run the Code

To run the code, you'll need Python installed, along with the specified open-source libraries (NumPy, pandas, scikit-learn, TensorFlow, PyTorch, matplotlib, seaborn). It's recommended to set up a virtual environment.

### Prerequisites

* Python 3.x
* `pip` (Python package installer)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/hack-now2211/AI_Codebyte.git
    cd AI_Codebyte
    ```
2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    ```
3.  **Activate the virtual environment:**
    * On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    * On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
4.  **Install the required libraries:**
    ```bash
    pip install pandas numpy scikit-learn matplotlib seaborn
    ```

### Running Specific Sections

#### Section A: Python & Data Manipulation

##### Q1. Data Cleanup & Summary (`SA_Q1.py`)

This script performs data cleanup and provides a summary of `student_scores.csv`. The `student_scores.csv` file was generated for this test and includes two missing values for records "Laura" and "Hannah" to demonstrate the missing value imputation.

* **Functionality:**
    * Fills any missing numeric values with the mean of their respective columns.
    * Converts the 'Gender' column into binary values.
    * Returns a summary DataFrame showing average scores per gender.

* **To Run:**
    ```bash
    python SA/SA_Q1.py
    ```

##### Q2. Dictionary-Based Stats (`SA_Q2.py`)

This script demonstrates calculating statistics from a given dictionary.

* **Functionality:**
    * Takes a dictionary of user scores (e.g., `{"user_1": [80, 90, 85]}`).
    * Returns a new dictionary with each user's average, minimum, and maximum scores.

* **To Run:**
    ```bash
    python SA/SA_Q2.py
    ```

#### Section B: Machine Learning

This section focuses on classification and regression tasks.

##### Q3. Classifier on Iris (`SB_Q3.py`)

This script builds and evaluates a Decision Tree classifier on the Iris dataset.

* **Functionality:**
    * Loads the Iris dataset from `sklearn.datasets`.
    * Splits the data into an 80-20 train-test split.
    * Trains a Decision Tree classifier.
    * Predicts and prints accuracy on the test set.
    * Plots a confusion matrix using `matplotlib` or `seaborn`.

* **To Run:**
    ```bash
    python SB/SB_Q3.py
    ```

##### Q4. Simple Regression (`SB_Q4.py`)

This script builds and evaluates a linear regression model on the `simple_housing.csv` dataset.

* **Functionality:**
    * Uses `area` and `bedrooms` to predict `price`.
    * Evaluates the model using Mean Absolute Error (MAE).
    * Plots actual vs. predicted prices on a scatter plot.

* **To Run:**
    ```bash
    python SB/SB_Q4.py
    ```

#### Section C: AI/ML Application & Thinking

This section contains conceptual answers and a simple NLP task.

##### Q5. Conceptual (`SC_Q5.txt`)

This file contains brief answers to conceptual questions related to machine learning.

* **Questions Addressed:**
    1.  What is overfitting in machine learning? 
    2.  When would you use a decision tree over logistic regression?
    3.  Explain the train-test split and why it's important.
    4.  What's the purpose of normalization? 
    5.  What's the difference between classification and regression?

* **To View:**
    Open the `SC/SC_Q5.txt` file.

##### Q6. Simple NLP Task - Sentiment Classification (`SC_Q6.py`)

This script performs a sentiment classification task using a Logistic Regression classifier.

* **Functionality:**
    * Loads `rec.autos` and `comp.sys.mac.hardware` categories from `sklearn.datasets.fetch_20newsgroups`.
    * Uses `TfidfVectorizer` to convert text data to vectors.
    * Trains a Logistic Regression classifier.
    * Prints the accuracy and shows the 5 most important words per class.

* **To Run:**
    ```bash
    python SC/SC_Q6.py
    ```
