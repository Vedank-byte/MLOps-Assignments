# Assignment 9 — SHAP and LIME Explainability

**Aim:** Explain Random Forest Iris predictions globally and locally.

**Files:** [9.py](9.py) contains the complete script reproduced in the assignment report; [requirements.txt](requirements.txt) lists dependencies.

**Recorded output:** **100% accuracy** on 30 held-out samples; local predicted species **Versicolor**. SHAP class-0 importance emphasized petal length and petal width. LIME positive contributions were approximately **+0.214** (petal length) and **+0.174** (petal width). The original SHAP and LIME chart images have not yet been uploaded here.

**Run:** `python -m pip install -r requirements.txt`, then `python 9.py`.
