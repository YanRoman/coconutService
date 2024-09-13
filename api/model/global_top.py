from collections import Counter

from api.timer.timer_decorator import timer


@timer
def global_top(data_loader):
    products = data_loader.get_df()['product_id']

    counter = Counter(products)
    top_products = counter.most_common(3)
    return [product for product, count in top_products]
    # TODO тут можно будет сделать предикт количества итемов которые возьмет юзер
