class TestEntryList(object):

    def test_blog_page_entries(self, browser):
        browser.visit('http://127.0.0.1:8000/blog/')
        entries = browser.find_by_css('.page-content')
        assert browser.status_code == 200
        assert len(entries) > 0

    def test_entry_page_search(self, browser):
        browser.visit('http://127.0.0.1:8000/blog2/search/?q=test')
        entries = browser.find_by_css('.page-content')
        assert browser.status_code == 200
        assert browser.is_text_present('search')
        assert len(entries) > 0

    def test_entry_page_author(self, browser):
        browser.visit('http://127.0.0.1:8000/blog/author/admin/')
        entries = browser.find_by_css('.page-content')
        assert browser.status_code == 200
        assert browser.is_text_present('Entries for author')
        assert len(entries) > 0

    def test_entry_page_category(self, browser):
        browser.visit('http://127.0.0.1:8000/blog/category/test/')
        entries = browser.find_by_css('.page-content')
        assert browser.status_code == 200
        assert browser.is_text_present('Entries for category')
        assert len(entries) > 0

    def test_entry_page_tag(self, browser):
        browser.visit('http://127.0.0.1:8000/blog/tag/test/')
        entries = browser.find_by_css('.page-content')
        assert browser.status_code == 200
        assert browser.is_text_present('Entries for tag')
        assert len(entries) > 0

    def test_entry_page_archive_year(self, browser):
        browser.visit('http://127.0.0.1:8000/blog/2016/')
        entries = browser.find_by_css('.page-content')
        assert browser.status_code == 200
        assert browser.is_text_present('Entries for date')
        assert len(entries) > 0

    def test_entry_page_archive_year_month(self, browser):
        browser.visit('http://127.0.0.1:8000/blog/2016/03/')
        entries = browser.find_by_css('.page-content')
        assert browser.status_code == 200
        assert browser.is_text_present('Entries for date')
        assert len(entries) > 0
