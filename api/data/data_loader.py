import pandas as pd
import logging
import sys
from sklearn.model_selection import train_test_split

"""
DataLoader загружает данные, чистит и создает train test выборки
"""
DATA_MAX_SIZE = 20000


class DataLoader:

    def __init__(self, file_name):
        try:
            self.df = pd.read_csv(f"api/data/{file_name}")
            logging.info(f"Файл {file_name} успешно загружен.")
        except FileNotFoundError:
            logging.error(f"Файл {file_name} не найден.")
            sys.exit(1)

        if len(self.df) > DATA_MAX_SIZE:
            self.df = self.df.sample(n=DATA_MAX_SIZE, random_state=1)
            logging.info(f"Файл обрезан до {DATA_MAX_SIZE} записей.")

    def get_df(self):
        return self.df

    def get_transactions(self):
        cart_df = self.df.groupby('user_session')['product_id'].apply(list).reset_index()
        cart_df.columns = ['user_session', 'product_ids']
        cart_df = cart_df[cart_df['product_ids'].apply(len) > 1]
        return cart_df

    def get_transactions_train_test(self):
        test_cart_df, train_cart_df = train_test_split(self.get_transactions(), test_size=0.2, random_state=42)
        return test_cart_df, train_cart_df
