import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import io

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelBinarizer
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report, roc_curve, auc
)

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

from sklearn.decomposition import PCA

st.set_page_config(page_title="ML Analyzer", layout="wide")
st.title("🌸 Анализ моделей машинного обучения (Iris Dataset)")

# Загрузка данных
dataset = load_iris()
X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
y = dataset.target
target_names = dataset.target_names

# Интерактивный фильтр
st.sidebar.header("🔎 Фильтр данных")
filter_feature = st.sidebar.selectbox("Признак для фильтрации", X.columns)
min_val, max_val = float(X[filter_feature].min()), float(X[filter_feature].max())
val_range = st.sidebar.slider("Диапазон", min_val, max_val, (min_val, max_val), step=0.1)
filtered_idx = X[filter_feature].between(val_range[0], val_range[1])
X = X[filtered_idx]
y = y[filtered_idx]

# Блок: информация о датасете
with st.expander("ℹ️ Описание датасета Iris"):
    st.markdown(f"""
        **Классификация ирисов (Iris)** — классический датасет, включающий 150 образцов цветков трёх видов:
        - **Setosa**, **Versicolor**, **Virginica**

        **Признаки (4)**:
        - Длина и ширина чашелистика
        - Длина и ширина лепестка
    """)
    st.dataframe(X.join(pd.Series(y, name="target")))

# Графики признаков
st.subheader("📊 Распределение признаков по классам")
selected_feature = st.selectbox("Выберите признак", X.columns)
fig, ax = plt.subplots()
for label in np.unique(y):
    sns.kdeplot(X[selected_feature][y == label], label=target_names[label], fill=True, ax=ax)
plt.legend()
st.pyplot(fig)

# График распределения целевой переменной
st.subheader("🟠 Распределение целевой переменной (Классы)")
fig, ax = plt.subplots()
sns.countplot(x=y, ax=ax)
ax.set_xticklabels(target_names)
plt.title("Распределение классов в целевой переменной")
st.pyplot(fig)

# Параллельные координаты
st.subheader("📈 Параллельные координаты")
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

fig, ax = plt.subplots()
for i, label in enumerate(target_names):
    ax.plot(X_scaled[y == i, :].T, color=sns.color_palette("Set2")[i], alpha=0.3)
ax.set_title("Параллельные координаты")
ax.set_xticks(np.arange(X_scaled.shape[1]))
ax.set_xticklabels(X.columns, rotation=45)
st.pyplot(fig)

# Матрица корреляции признаков
st.subheader("📊 Матрица корреляции признаков")
corr_matrix = X.corr()
fig, ax = plt.subplots()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)
plt.title("Корреляция признаков")
st.pyplot(fig)

# Параметры моделей
st.sidebar.header("⚙️ Настройки моделей")
test_size = st.sidebar.slider("Доля теста", 0.1, 0.5, 0.3)

models_selected = st.sidebar.multiselect(
    "Выберите модели:", ["Логистическая регрессия", "Случайный лес", "SVM"],
    default=["Логистическая регрессия", "Случайный лес"]
)

params = {}
if "Логистическая регрессия" in models_selected:
    params["lr_C"] = st.sidebar.slider("C (LogReg)", 0.01, 10.0, 1.0)
if "Случайный лес" in models_selected:
    params["rf_n_estimators"] = st.sidebar.slider("n_estimators (RF)", 10, 200, 100)
if "SVM" in models_selected:
    params["svm_C"] = st.sidebar.slider("C (SVM)", 0.01, 10.0, 1.0)

# Обучение
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

results = {}

st.subheader("🏋️ Обучение моделей и результаты")

for model_name in models_selected:
    if model_name == "Логистическая регрессия":
        model = LogisticRegression(C=params["lr_C"], max_iter=200)
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
    elif model_name == "Случайный лес":
        model = RandomForestClassifier(n_estimators=params["rf_n_estimators"])
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
    elif model_name == "SVM":
        model = SVC(C=params["svm_C"], probability=True)
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)

    acc = accuracy_score(y_test, y_pred)
    results[model_name] = {
        "model": model,
        "accuracy": acc,
        "y_pred": y_pred,
        "report": classification_report(y_test, y_pred, target_names=target_names, output_dict=True)
    }

# Таблица метрик
st.markdown("### 📋 Сравнение метрик моделей")
summary = pd.DataFrame({
    model: {
        "Accuracy": f"{res['accuracy']:.2f}",
        "Precision": f"{np.mean([res['report'][cls]['precision'] for cls in target_names]):.2f}",
        "Recall": f"{np.mean([res['report'][cls]['recall'] for cls in target_names]):.2f}",
    }
    for model, res in results.items()
}).T
st.dataframe(summary)

# Классификационные отчёты
st.markdown("### 🧾 Классификационные отчёты")
for model_name, res in results.items():
    st.markdown(f"**{model_name}**")
    report_df = pd.DataFrame(res["report"]).T
    st.dataframe(report_df)

# Матрицы ошибок
st.markdown("### 🔍 Матрицы ошибок")
for model_name, res in results.items():
    st.markdown(f"#### {model_name}")
    cm = confusion_matrix(y_test, res["y_pred"])
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap="Blues", xticklabels=target_names, yticklabels=target_names)
    plt.xlabel("Предсказание")
    plt.ylabel("Истина")
    st.pyplot(fig)

# Важность признаков
if "Случайный лес" in results:
    st.markdown("### 🌟 Самые важные признаки (Random Forest)")
    rf_model = results["Случайный лес"]["model"]
    importances = rf_model.feature_importances_
    imp_df = pd.DataFrame({
        "Признак": X.columns,
        "Важность": importances
    }).sort_values("Важность", ascending=False)
    st.dataframe(imp_df)

    fig, ax = plt.subplots()
    sns.barplot(data=imp_df, x="Важность", y="Признак", palette="viridis")
    st.pyplot(fig)

# PCA визуализация
st.markdown("### 🧬 Визуализация кластеров (PCA)")
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
df_vis = pd.DataFrame(X_pca, columns=["PC1", "PC2"])
df_vis["Истинный класс"] = [target_names[i] for i in y]

fig, ax = plt.subplots()
sns.scatterplot(data=df_vis, x="PC1", y="PC2", hue="Истинный класс", palette="Set2", s=80)
plt.title("PCA — Истинные классы")
st.pyplot(fig)

if len(results) == 1:
    model_name = list(results.keys())[0]
    model = results[model_name]["model"]
    if model_name == "Случайный лес":
        y_pred_vis = model.predict(X)
    else:
        X_scaled_full = scaler.transform(X)
        y_pred_vis = model.predict(X_scaled_full)

    df_vis["Предсказание"] = [target_names[i] for i in y_pred_vis]
    fig2, ax2 = plt.subplots()
    sns.scatterplot(data=df_vis, x="PC1", y="PC2", hue="Предсказание", palette="Set1", s=80)
    plt.title(f"PCA — Предсказания модели: {model_name}")
    st.pyplot(fig2)

# ROC-кривые
if len(np.unique(y)) == 2:
    st.markdown("### 📉 ROC-кривые")
    lb = LabelBinarizer()
    y_test_bin = lb.fit_transform(y_test).ravel()
    for model_name, res in results.items():
        model = res["model"]
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba(X_test_scaled if model_name != "Случайный лес" else X_test)[:, 1]
            fpr, tpr, _ = roc_curve(y_test_bin, probs)
            roc_auc = auc(fpr, tpr)

            fig, ax = plt.subplots()
            ax.plot(fpr, tpr, label=f"AUC = {roc_auc:.2f}")
            ax.plot([0, 1], [0, 1], "--", color="gray")
            ax.set_title(f"ROC-кривая — {model_name}")
            ax.set_xlabel("FPR")
            ax.set_ylabel("TPR")
            ax.legend()
            st.pyplot(fig)

# Сохранение модели
st.markdown("### 💾 Сохранить модель")
model_to_save = st.selectbox("Выберите модель для сохранения", list(results.keys()))
model_file = io.BytesIO()
joblib.dump(results[model_to_save]["model"], model_file)
st.download_button("📥 Скачать модель", data=model_file.getvalue(), file_name=f"{model_to_save}.joblib")
