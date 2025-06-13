Restaurant Recommendation System using Machine Learning with Graphs
A bipartite graph-based restaurant recommendation system that predicts user ratings using both traditional feature engineering and graph representation learning approaches.
📋 Table of Contents

Overview
Features
Architecture
Dataset
Installation
Usage
Model Approaches
Results
Project Structure
Contributing
License

🎯 Overview
This project implements a restaurant recommendation system that predicts user ratings using machine learning with graphs. The system models the recommendation task as an edge prediction problem in a bipartite graph, where users and restaurants are nodes, and ratings are edges.
Key Highlights

Dual Approach: Compares feature engineering vs. graph representation learning
Bipartite Graph Modeling: Users and restaurants as nodes, ratings as edges
Neural Network Classification: Predicts overall, food, and service ratings
Graph Embeddings: Uses DeepWalk algorithm for unsupervised learning

✨ Features

Feature Engineering: Hand-crafted features from restaurant characteristics and user preferences
Graph Representation Learning: Task-independent embeddings using random walk algorithms
Multi-target Prediction: Predicts overall rating, food rating, and service rating
Comprehensive Evaluation: Confusion matrices and accuracy metrics
Modular Design: Separate notebooks for different experimental phases

🏗️ Architecture
The system uses two main approaches:
1. Feature Engineering Approach

Input: 24-dimensional feature vectors
Features: Restaurant-user relations, restaurant attributes, user demographics
Model: Feed-forward neural networks

2. Graph Representation Learning Approach

Input: 256-dimensional embedding vectors (128 per node, concatenated)
Algorithm: DeepWalk random walk embeddings
Model: Feed-forward neural networks with larger hidden layers

📊 Dataset
Uses the publicly available restaurant and consumer dataset from UCI Machine Learning Repository:

Users: 138 users with demographic and preference data
Restaurants: 130 restaurants with characteristics and amenities
Ratings: 1,161 ratings (overall, food, service)
Files: 9 CSV files containing restaurant data, user profiles, and ratings

Data Split

Training: 76% (885 instances)
Validation: 12% (138 instances)
Test: 12% (138 instances)

🚀 Installation
Prerequisites
bashPython 3.7+
pip install -r requirements.txt
Required Libraries
bashpip install numpy pandas scikit-learn
pip install easygraph networkx
pip install matplotlib seaborn
pip install graphviz
pip install jupyter
Clone Repository
bashgit clone https://github.com/yourusername/restaurant-recommendation-system.git
cd restaurant-recommendation-system
📖 Usage
Quick Start

Data Preparation:
bash# Place dataset files in data/raw/ directory
# Run main project notebook
jupyter notebook notebooks/A-MainProject.ipynb

Feature Engineering Model:
bashjupyter notebook notebooks/B-Model-Features.ipynb

Graph Representation Learning Model:
bashjupyter notebook notebooks/C-Model-DW.ipynb


Running Individual Components
python# Data wrangling
from src.wrangling import process_restaurant_data, process_user_data

# Feature engineering
from src.modeling import create_feature_vectors, train_neural_network

# Graph embeddings
from src.graphing import create_bipartite_graph, generate_deepwalk_embeddings
🔬 Model Approaches
Feature Engineering

Vector Size: 24 dimensions
Feature Categories:

Restaurant-user relations (9 features)
Restaurant attributes (8 features)
User demographics (7 features)



Graph Representation Learning

Algorithm: DeepWalk
Embedding Size: 128 dimensions per node
Edge Vector: 256 dimensions (concatenated node embeddings)
Advantage: Task-independent, no manual feature engineering

📈 Results
Model Performance Comparison
ApproachOverall RatingFood RatingService RatingFeature Engineering43.47%47.82%47.10%Graph Representation49.27%59.42%53.62%
Key Findings

Graph representation learning outperformed traditional feature engineering
Best results achieved for food rating prediction (59.42% accuracy)
Graph embeddings produced more meaningful error patterns
Model showed some overfitting but maintained good generalization
