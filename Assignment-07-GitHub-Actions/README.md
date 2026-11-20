# Assignment 7 — GitHub Actions CI/CD

**Original assignment repository:** https://github.com/vednk-shinde/Assignment7-ML-CICD

The report preserved this model code:

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train_model():
    iris = load_iris()
    X_train, X_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    return accuracy_score(y_test, model.predict(X_test))
```

Test logic in report:

```python
from src.model import train_model

def test_model_accuracy():
    accuracy = train_model()
    assert accuracy >= 0.80
```

**Workflow outline** (not guaranteed identical to original YAML):

```yaml
name: ML CI/CD Pipeline
on: [push]
jobs:
  build-and-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: python src/model.py
      - run: python -m pytest tests/ -v
  deploy:
    needs: build-and-test
    runs-on: ubuntu-latest
    steps:
      - name: Simulated deployment
        run: |
          echo "All tests passed."
          echo "Deploying Iris ML model..."
          echo "Deployment completed successfully."
```

The deployment step is **simulated**, not deployment to a live hosting service. The original repository is the authoritative source for exact source and test threshold.
