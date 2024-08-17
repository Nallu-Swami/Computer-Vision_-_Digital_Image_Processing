import gensim.downloader as api
import numpy as np

# Load pre-trained GloVe vectors
glove_model = api.load('glove-wiki-gigaword-100')  # You can choose different models

def get_average_glove_vectors(tokens_list, model, vector_size):
    feature_vectors = []
    for tokens in tokens_list:
        vec = np.zeros(vector_size)
        count = 0
        for token in tokens:
            if token in model:
                vec += model[token]
                count += 1
        if count > 0:
            vec /= count
        feature_vectors.append(vec)
    return np.array(feature_vectors)

X_train_glove = get_average_glove_vectors(X_train_tokens, glove_model, 100)
X_test_glove = get_average_glove_vectors(X_test_tokens, glove_model, 100)

# Scale features and train
scaler = StandardScaler()
X_train_glove = scaler.fit_transform(X_train_glove)
X_test_glove = scaler.transform(X_test_glove)

model_glove = LogisticRegression(max_iter=1000)
model_glove.fit(X_train_glove, y_train)
y_pred_glove = model_glove.predict(X_test_glove)

accuracy_glove = accuracy_score(y_test, y_pred_glove)
print(f"GloVe Model Accuracy: {accuracy_glove * 100:.2f}%")
