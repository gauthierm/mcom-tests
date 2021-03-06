# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.desktop.base import Base
from selenium.webdriver.common.by import By


class Notes(Base):

    _url = '{base_url}/{locale}/firefox/notes'

    _firefox_notes_header_locator = (By.CSS_SELECTOR, '.notes-head > h1')

    @property
    def firefox_notes_header_text(self):
        return self.selenium.find_element(*self._firefox_notes_header_locator).text
