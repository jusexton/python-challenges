import pytest

from challenges.codewars.pagination import PaginationHelper


class TestPaginationHelper:
    @pytest.fixture
    def helper(self):
        return PaginationHelper(range(0, 11), 5)

    def test_item_count_is_correctly_returned(self, helper):
        assert 11 == helper.item_count()

    def test_page_count_is_correctly_returned(self, helper):
        assert 3 == helper.page_count()

    @pytest.mark.parametrize("index,count", [(0, 5), (1, 5), (2, 1), (3, -1)])
    def test_page_item_count_correctly_returns_how_many_items_are_on_a_page(
        self, helper, index, count
    ):
        assert count == helper.page_item_count(index)

    @pytest.mark.parametrize(
        "index,page",
        [
            (10, 2),
            (9, 1),
            (5, 1),
            (4, 0),
            (2, 0),
            (0, 0),
            (-1, -1),
            (-10, -1),
            (11, -1),
            (20, -1),
        ],
    )
    def test_page_index_correctly_returns_which_page_an_index_belongs_too(
        self, helper, index, page
    ):
        assert page == helper.page_index(index)
