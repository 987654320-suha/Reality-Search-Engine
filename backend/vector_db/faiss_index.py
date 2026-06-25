import faiss
import numpy as np
import os

INDEX_FILE = "data/faiss.index"


def load_or_create_index(dim=384):

    if os.path.exists(INDEX_FILE):

        return faiss.read_index(
            INDEX_FILE
        )

    return faiss.IndexFlatL2(dim)


def save_index(index):

    faiss.write_index(
        index,
        INDEX_FILE
    )