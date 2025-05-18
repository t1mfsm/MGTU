import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, confusion_matrix, roc_curve, auc, classification_report
)

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

# Загружаем и обрабатываем данные
@st.cache_data
def load_data():
    df = pd.read_csv("Adidas US Sales.csv", sep=";")
    df['invoice_date'] = pd.to_datetime(df['invoice_date'], format='%d.%m.%Y')
    df['year'] = df['invoice_date'].dt.year
    df['month'] = df['invoice_date'].dt.month
    df['day'] = df['invoice_date'].dt.day
    df = pd.get_dummies(df, columns=[
        'retailer', 'region', 'state', 'city', 'product', 'sales_method'
    ])
    df['target'] = (df['operating_profit'] > 1000).astype(int)
    X = df.drop(['sales_id', 'invoice_date', 'operating_profit', 'target'], axis=1)
    y = df['target']
    return train_test_split(X, y, test_size=0.2, random_state=42), X.columns

# Интерфейс
st.set_page_config("Классификация Adidas Sales", layout="wide")
st.title("🎓 Демонстрация моделей классификации")
# 📊 Анализ датасета
st.header("📂 Анализ датасета Adidas US Sales")

df = pd.read_csv("Adidas US Sales.csv", sep=";")
df['invoice_date'] = pd.to_datetime(df['invoice_date'], format='%d.%m.%Y')
df['year'] = df['invoice_date'].dt.year
df['month'] = df['invoice_date'].dt.month
df['day'] = df['invoice_date'].dt.day
df['target'] = (df['operating_profit'] > 1000).astype(int)

with st.expander("🧾 Общая информация"):
    st.write(df.describe())
    st.write("Размер:", df.shape)
    st.write("Пропущенные значения:")
    st.write(df.isnull().sum())

with st.expander("📈 Распределения числовых признаков"):
    numeric_cols = ['price_per_unit', 'units_sold', 'total_sales', 'operating_profit']
    fig, axs = plt.subplots(2, 2, figsize=(12, 6))
    for i, col in enumerate(numeric_cols):
        sns.histplot(df[col], ax=axs[i // 2][i % 2], kde=True, color='teal')
        axs[i // 2][i % 2].set_title(col)
    st.pyplot(fig)

with st.expander("📊 Категориальные признаки"):
    cat_col = st.selectbox("Выберите категориальный признак", ['retailer', 'region', 'state', 'product', 'sales_method'])
    fig_cat, ax_cat = plt.subplots()
    sns.countplot(data=df, x=cat_col, order=df[cat_col].value_counts().index, palette="viridis", ax=ax_cat)
    plt.xticks(rotation=45)
    st.pyplot(fig_cat)

with st.expander("🧠 Распределение целевой переменной (прибыль > 1000)"):
    fig_target, ax_target = plt.subplots()
    sns.countplot(x='target', data=df, ax=ax_target, palette="Set2")
    ax_target.set_xticklabels(["0: Низкая прибыль", "1: Высокая прибыль"])
    st.pyplot(fig_target)

with st.expander("🔗 Корреляция числовых признаков"):
    corr = df[['price_per_unit', 'units_sold', 'total_sales', 'operating_profit']].corr()
    fig_corr, ax_corr = plt.subplots()
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax_corr)
    st.pyplot(fig_corr)

(X_train, X_test, y_train, y_test), feature_names = load_data()

# Выбор модели
model_type = st.sidebar.selectbox("Выберите модель", [
    "Logistic Regression", "K-Nearest Neighbors", "Decision Tree", "Random Forest", "Gradient Boosting"
])

# Гиперпараметры
if model_type == "Logistic Regression":
    C = st.sidebar.slider("Регуляризация (C)", 0.01, 10.0, 1.0)
    model = LogisticRegression(C=C, max_iter=1000)
elif model_type == "K-Nearest Neighbors":
    n_neighbors = st.sidebar.slider("Количество соседей", 1, 20, 5)
    model = KNeighborsClassifier(n_neighbors=n_neighbors)
elif model_type == "Decision Tree":
    max_depth = st.sidebar.slider("Максимальная глубина", 1, 20, 5)
    model = DecisionTreeClassifier(max_depth=max_depth)
elif model_type == "Random Forest":
    n_estimators = st.sidebar.slider("Количество деревьев", 10, 200, 100)
    model = RandomForestClassifier(n_estimators=n_estimators)
elif model_type == "Gradient Boosting":
    n_estimators = st.sidebar.slider("Количество деревьев", 10, 200, 100)
    learning_rate = st.sidebar.slider("Скорость обучения", 0.01, 1.0, 0.1)
    model = GradientBoostingClassifier(n_estimators=n_estimators, learning_rate=learning_rate)

# Масштабирование
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Обучение
model.fit(X_train_scaled, y_train)
y_pred = model.predict(X_test_scaled)
y_proba = model.predict_proba(X_test_scaled)[:, 1] if hasattr(model, "predict_proba") else None

# Метрики
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, output_dict=True)

# Отображение
st.subheader("📊 Результаты модели")
col1, col2 = st.columns(2)

with col1:
    st.metric("Точность", f"{accuracy:.2%}")
    st.text("Классификационный отчёт:")
    st.dataframe(pd.DataFrame(report).transpose())

with col2:
    st.text("Матрица ошибок:")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    ax.set_xlabel("Предсказано")
    ax.set_ylabel("Истинное")
    st.pyplot(fig)

# ROC-кривая
if y_proba is not None:
    st.subheader("📈 ROC-кривая")
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)
    fig_roc, ax_roc = plt.subplots()
    ax_roc.plot(fpr, tpr, color='blue', label=f'AUC = {roc_auc:.2f}')
    ax_roc.plot([0, 1], [0, 1], 'k--')
    ax_roc.set_xlabel("False Positive Rate")
    ax_roc.set_ylabel("True Positive Rate")
    ax_roc.legend()
    st.pyplot(fig_roc)

# Важность признаков
if hasattr(model, "feature_importances_"):
    st.subheader("🔎 Важность признаков")
    importances = model.feature_importances_
    imp_df = pd.DataFrame({"feature": feature_names, "importance": importances})
    imp_df = imp_df.sort_values("importance", ascending=False).head(10)

    fig_imp, ax_imp = plt.subplots()
    sns.barplot(x="importance", y="feature", data=imp_df, ax=ax_imp, palette="viridis")
    ax_imp.set_title("Топ-10 признаков")
    st.pyplot(fig_imp)

# Примеры предсказаний
st.subheader("🔍 Примеры предсказаний")
preview_df = pd.DataFrame({
    "Истинное значение": y_test.values[:10],
    "Предсказано": y_pred[:10]
})
st.table(preview_df)
