from quan_tri_mang import qtm
from techtalk import tt
from tinh_te import tinh_te
from top_dev import td


def test_qtm():
    _qtm = qtm()
    _qtm.get_html_code(99)
    _qtm.get_articles_attributes()


def test_td():
    _td = td()
    _td.get_html_code(1)
    _td.get_articles_attributes()


def test_tt():
    _tt = tt()
    _tt.get_html_code(0)
    _tt.get_articles_attributes()


def test_tinh_te():
    _tt = tinh_te()
    _tt.get_auth_token()
    _tt.get_raw_html()
    _tt.get_json_code(0)
    _tt.get_articles_attributes


LIST_TEST = [
    test_qtm, test_td,
    test_tt, test_tinh_te
]


if __name__ == '__main__':
    for func in LIST_TEST:
        func()