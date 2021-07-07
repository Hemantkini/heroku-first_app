import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

import graphviz as graphviz
from sklearn.datasets import load_iris
from sklearn import tree
import streamlit as st


X, y = load_iris(return_X_y=True)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

dot_data  = tree.export_graphviz(clf, out_file=None)

st.graphviz_chart(dot_data)

