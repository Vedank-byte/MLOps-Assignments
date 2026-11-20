"""Reconstructed selection step."""
from sklearn.feature_selection import SelectKBest,f_classif

def build_selector(k=8):
    return SelectKBest(score_func=f_classif,k=k)
