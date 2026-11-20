import shap
import lime.lime_tabular
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42)
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
print("Model Accuracy:", accuracy_score(y_test, model.predict(X_test)))

explainer = shap.TreeExplainer(model)
shap_values = explainer(X_test)
shap.plots.bar(shap_values[:, :, 0], show=False)
plt.savefig("shap_explanation.png", bbox_inches="tight")
plt.show()

lime_explainer = lime.lime_tabular.LimeTabularExplainer(
    X_train, feature_names=iris.feature_names,
    class_names=iris.target_names.tolist(), mode="classification",
    random_state=42)
explanation = lime_explainer.explain_instance(
    X_test[0], model.predict_proba, num_features=4)
print("Predicted Species:", iris.target_names[model.predict([X_test[0]])[0]])
print("LIME Explanation:", explanation.as_list())
fig = explanation.as_pyplot_figure()
fig.savefig("lime_explanation.png", bbox_inches="tight")
plt.show()
print("SHAP and LIME implemented successfully!")
