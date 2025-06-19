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
pip install pandas numpy scikit-learn matplotlib seaborn
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
- Trained a `RandomForestClassifier` with 100 trees (`n_estimators=100`).
- Used `random_state=42` for reproducibility.

### 4. Model Evaluation
- Generated a classification report (precision, recall, F1-score).
- Plotted a confusion matrix heatmap to visualize actual vs. predicted labels.

### 5. Visualization
- Count plot to show distribution of eye colors.
- Heatmap to display confusion matrix for model interpretation.

---

## 📊 Example Outputs

- **Confusion Matrix Heatmap**: Shows how well the model predicted each class.
- **Classification Report**: Summarizes performance metrics across all classes.
- **Eye Color Distribution Plot**: Helps identify any class imbalance.

---

## 🧠 Insights Gained

- SNPs can be predictive of traits like eye color.
- Random Forest performs well with categorical and tabular data.
- Stratified splits help maintain class proportions.
- Visualization helps diagnose model strengths and weaknesses.

---

## 📂 File Structure

```
eye-color-prediction/
├── synthetic_eye_color_dataset.csv
├── Untitled103.ipynb            # Jupyter Notebook (your main code)
└── README.md                    # This file
```

---

## 💡 Future Work

- Use real genetic datasets (e.g., 23andMe or openSNP).
- Compare performance with other models (e.g., SVM, XGBoost).
- Add SHAP or feature importance plots to interpret SNP influence.

---

## 👩‍💻 Author

**Prapti Mishra**  
📧 praptimishra977@gmail.com
