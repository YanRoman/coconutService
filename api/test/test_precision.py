from django.test import SimpleTestCase

from api.model.global_top import global_top
from api.data.data_loader import DataLoader
import numpy as np
from tqdm import tqdm
import logging

DATA_FILE_NAME = "chunk_0.csv"
data_loader = DataLoader(DATA_FILE_NAME)


def get_precision(func):
    transactions = data_loader.get_transactions()['product_ids'].to_list()
    total_precision = 0

    for product_ids in tqdm(transactions, desc="Считаю точность..."):
        logging.disable(logging.CRITICAL)
        predict = func(data_loader)
        logging.disable(logging.NOTSET)

        precision = np.isin(predict, product_ids).sum() / len(predict)
        total_precision += precision

    average_precision = total_precision / len(transactions) if transactions else 0
    logging.info(f"[Method: {func.__name__}] [Precision: {average_precision:.2f}] [Iter count: {len(transactions)}]")


class TestPrecision(SimpleTestCase):
    def test_global_top(self):
        get_precision(global_top)
