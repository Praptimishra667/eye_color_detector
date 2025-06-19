
# 🧬 Eye Color Prediction using Genetic Data (SNPs)

This project builds a machine learning model to predict human eye color using Single Nucleotide Polymorphism (SNP) genotypes. It demonstrates how genetic data can be processed, modeled, and analyzed using Python and scikit-learn.

---

## 📁 Dataset Description

The dataset used is synthetic and contains:

- **SNP features**: Genetic markers (e.g., rs123, rs456, etc.)
- **Target**: Eye color (e.g., Brown, Blue, Green)

> 💡 SNPs are single-base variations in DNA that can influence physical traits like eye color.

---

## 🚀 Installation

Make sure you have the following Python libraries installed:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn xgboost
```

---

## 📌 Project Workflow

### 1. Data Preprocessing
- Loaded the CSV file using pandas.
- Encoded categorical SNP values using `LabelEncoder`.
- Converted eye color labels into numerical form.

### 2. Train-Test Split
- Used `train_test_split` with `stratify=y` to maintain class balance.

### 3. Model Training
- Trained three models:
  - `RandomForestClassifier` with 100 trees.
  - `XGBClassifier` using the `mlogloss` evaluation metric.
  - `SVC` with a linear kernel and probability estimates.
- Used `random_state=42` for reproducibility.

### 4. Model Evaluation
- Generated classification reports (precision, recall, F1-score).
- Plotted confusion matrix heatmaps for each model to visualize actual vs. predicted labels.

### 5. Visualization
- Count plot to show distribution of eye colors.
- Confusion matrix heatmaps for Random Forest, XGBoost, and SVM.

---

## 📊 Example Outputs

- **Confusion Matrix Heatmaps**: Show how well each model predicted eye color classes.
- **Classification Reports**: Summarize performance metrics across all classes.
- **Eye Color Distribution Plot**: Helps identify any class imbalance in the dataset.

---

## 🧠 Insights Gained

- SNPs can be predictive of traits like eye color.
- Random Forest, XGBoost, and SVM each have strengths for tabular classification problems.
- Stratified splits help maintain class proportions.
- Model comparison helps identify the most effective algorithm for this dataset.
- Visualization helps interpret prediction accuracy and areas of confusion.

### 🔍 Model Comparison Insight

- **Random Forest and XGBoost both fit the dataset perfectly.**  
  This suggests:
  - The dataset may be relatively easy to separate.
  - Or the models may be overfitting, especially if the dataset is synthetic and clean.

- **SVM performs significantly worse**, especially for the green eye class.  
  Its linear decision boundary likely fails to capture the complexity present in the SNP feature space.

---

## 📂 File Structure

```
eye-color-prediction/
├── synthetic_eye_color_dataset.csv
├── eyecolour.ipynb            # Jupyter Notebook (your main code)
└── README.md                  # This file
```

---

## 💡 Future Work

- Use real genetic datasets (e.g., 23andMe or openSNP).
- Add model accuracy comparison bar plots.
- Interpret feature importances using SHAP or other explainability tools.

---

## 👩‍💻 Author

**Prapti Mishra**  
📧 praptimishra977@gmail.com
