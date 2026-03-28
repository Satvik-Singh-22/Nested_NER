# Nested NER with Span-based Model

This project implements a span-based Nested Named Entity Recognition (NER) model using PyTorch. The model is designed to handle overlapping and nested entities, which are common in domains like biomedical literature.

## Model Architecture

The model follows a span-based classification approach:

1.  **Embedding Layer**: Uses pre-trained bio-embeddings (from `vocab_embed_bio.npy`) to initialize token representations.
2.  **Encoder**: A Bi-directional LSTM (BiLSTM) that processes the input sequence and generates hidden states for each token.
3.  **Span Representation**: For every potential span $(i, j)$ in the sentence (up to a maximum length), a representation is created by concatenating:
    -   Hidden state at the start index $i$.
    -   Hidden state at the end index $j$.
    -   Mean pool of hidden states for all tokens within the span $[i, j]$.
4.  **Classifier**: A Multi-Layer Perceptron (MLP) with a hidden layer, ReLU activation, and Dropout. It classifies each span into one of the following entity types:
    -   `DNA`
    -   `RNA`
    -   `cell_type`
    -   `protein`
    -   `cell_line`
    -   `NONE` (no entity)

## Dataset

The model is trained and evaluated on the **GENIA** dataset, a standard benchmark for biomedical nested NER.

## Results (Epoch 3)

The model achieved the following performance after 3 epochs:

| Metric | Value |
| :--- | :--- |
| **Train Loss** | 0.0189 |
| **Precision** | 0.7933 |
| **Recall** | 0.7948 |
| **F1-Score** | 0.7941 |

## Usage

To train or evaluate the model, refer to the `model1.ipynb` notebook. It contains the complete pipeline from data loading and preprocessing to training and evaluation.

### Prerequisites

-   Python 3.x
-   PyTorch
-   NumPy
-   Pandas
-   Scikit-learn
-   tqdm
