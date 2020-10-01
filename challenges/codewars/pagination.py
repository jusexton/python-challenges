import math


class PaginationHelper:
    def __init__(self, collection, items_per_page):
        if items_per_page <= 0:
            raise ValueError('Page must have at least 1 item')

        self.collection = collection
        self.items_per_page = items_per_page
        self._page_count = math.ceil(len(collection) / items_per_page)

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return self._page_count

    def page_item_count(self, page_index):
        start = self.items_per_page * page_index
        if start >= self.item_count():
            return - 1
        page_slice_len = self.item_count() - start
        return self.items_per_page if page_slice_len >= self.items_per_page else page_slice_len

    def page_index(self, item_index):
        if item_index >= self.item_count() or item_index < 0:
            return -1
        return item_index // self.items_per_page
