class BaseRouter(object):

    def __init__(self, driver):
        self.driver = driver

    def route_by_link(self, link):
        self.driver.get(link)

    def refresh_page(self):
        """
            Метод для перезагрузки страницы браузера
        """
        return self.driver.refresh()

    def close_chld_tab(self):
        try:
            parent = self.driver.window_handles[0]
            chld = self.driver.window_handles[1]
            self.driver.switch_to.window(chld)
            self.driver.close()
            self.driver.switch_to.window(parent)
        except:
            parent = self.driver.window_handles[0]
            self.driver.switch_to.window(parent)

    def tabs_counter(self):
        return len(self.driver.window_handles)

    def get_url_current_page(self):
        url = self.driver.current_url
        self.driver.back()
        return url
