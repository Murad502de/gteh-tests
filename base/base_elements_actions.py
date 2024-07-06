from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import logging
from time import sleep
# from datetime import datetime
# from allure_commons.types import AttachmentType
# import allure

#from .base_exceptions import ElementNotFounded


class BaseElementsActions(object):
    '''
       Класс BaseElementsActions предназначен для выполнения основных действий
       c объектами WebElement на странице браузера.
    '''

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=20):
        ''' Вызов метода возвращает WebElement, если он присутствует в DOM дереве и отрисован на странице.

       :param locator: - локатор элемента в DOM дереве. Например, (By.ID, "id_can_access").
       :param time: - время ожидания отрисовки элемента в секундах. Значение по умолчанию 3 секунды.
       :return: - Возвращает WebElement, если он присутствует в DOM дереве и отрисован на странице.
       '''

        try:
            return WebDriverWait(self.driver, time).until(EC.element_to_be_clickable(locator),
                                                          message=f"Can't find element by locator {locator}")
        except TimeoutException:
            return None

    def find_element_located(self, locator, time=20):
        """
        Вызов метода возвращает WebElement, если он присутствует в DOM дереве.
        :param locator: Локатор элемента в DOM дереве. Например, (By.ID, "id_can_access").
        :param time: Время ожидания отрисовки элемента в секундах. Значение по умолчанию 3 секунды.
        :return: Возвращает WebElement.
        """

        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements_after_all_elements_visibility(self, locator, time=3):
        ''' Вызов метода возвращает массив WebElement элементов, если они присутствуют
        в DOM дереве и отрисованы на странице.

       :param locator: - локатор элемента в DOM дереве. Например, (By.ID, "id_can_access").
       :param time: - время ожидания отрисовки элемента в секундах. Значение по умолчанию 3 секунды.
       :return: - возвращает массив WebElement элементов, если они присутствуют
        в DOM дереве и отрисованы на странице
       '''

        try:
            return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator),
                                                          message=f"Can't find elements by locator {locator}")
        except TimeoutException:
            return None

    def find_elements_after_any_elements_located(self, locator, time=3):
        ''' Вызов метода возвращает массив WebElement элементов, если хотя бы один элемент присутствуют
        в DOM дереве и отрисован на странице.

       :param locator: - локатор элемента в DOM дереве. Например, (By.ID, "id_can_access").
       :param time: - время ожидания отрисовки элемента в секундах. Значение по умолчанию 3 секунды.
       :return: - возвращает массив WebElement элементов, если хотя бы один элемент присутствуют
        в DOM дереве и отрисован на странице.
       '''

        try:
            return WebDriverWait(self.driver, time).until(EC.visibility_of_any_elements_located(locator),
                                                          message=f"Can't find elements by locator {locator}")
        except TimeoutException:
            return None

    def click(self, locator, time_wait=10, time_sleep=0):
        sleep(time_sleep)
        logging.info(f"Клик по элементу с локатором: {locator}")
        try:
            element = WebDriverWait(self.driver, time_wait).until(EC.element_to_be_clickable(locator))
            element.click()

            # Обновляем ссылку на элемент с помощью явного ожидания
            self.wait_for_element_to_be_updated(element)

            return element
        except NoSuchElementException:
            logging.error(f"Элемент с локатором {locator} не найден")
            raise

    def wait_for_element_to_be_updated(self, element):
        try:
            WebDriverWait(self.driver, 2).until(staleness_of(element))
        except TimeoutException:
            pass

    # def scroll_to_element(self, locator, time_sleep=0):
    #     """
    #     Метод предназначен для скролла до WebElement-а,
    #     если он находится за пределами видимости в окне браузера.
    #
    #    :param locator: - локатор элемента в DOM дереве. Например, (By.ID, "id_can_access").
    #    :param time: - время ожидания отрисовки элемента в секундах. Значение по умолчанию 3 секунды.
    #    """
    #
    #     sleep(time_sleep)
    #     element = self.find_element(locator)
    #
    #     if (element):
    #         action_chains = ActionChains(self.driver)
    #         action_chains.move_to_element(element).perform()
    #     else:
    #         raise ElementNotFounded('Элемент не найден')

    # def input_value(self, locator, text='', keys=None, time_wait=10, time_sleep=0, click=False, clear=True):
    #     logging.info(f"Ввод значения '{text}' в элемент с локатором: {locator}")
    #     try:
    #         sleep(time_sleep)
    #         element = self.find_element(locator, time_wait)
    #         if click:
    #             self.scroll_to_element(locator)
    #             sleep(time_sleep)
    #             WebDriverWait(self.driver, time_wait).until(EC.element_to_be_clickable(locator)).click()
    #         if clear:
    #             element.clear()
    #         sleep(time_sleep)
    #         element.send_keys(text)
    #         if keys is not None:
    #             element.send_keys(keys)
    #         return element
    #     except NoSuchElementException:
    #         logging.error(f"Элемент с локатором {locator} не найден")
    #         raise
    #     except ElementClickInterceptedException:
    #         logging.error(f"Элемент с локатором {locator} был перекрыт другим элементом")
    #         raise

    # def scroll_by_pixels(self, x=0, y=0, time_sleep=0):
    #     """
    #     Метод предназначен для скролла на х, у пикселей.
    #
    #    :param x: - количество пикселей для координаты х.
    #    :param y: - количество пикселей для координаты у.
    #    :param time: - время ожидания отрисовки элемента в секундах. Значение по умолчанию 3 секунды.
    #    """
    #
    #     sleep(time_sleep)
    #     self.driver.execute_script(f"window.scrollBy({x}, {y})", "")

    def waiting_for_element_invisible(self, element, time=700):
        """
        Метод предназначен для ожидания пока элемент станет не видимым (не пропадет со страницы)
        """
        try:
            WebDriverWait(self.driver, timeout=time).until(EC.invisibility_of_element_located(element))
        except TimeoutException as e:
            print(f'Time exception for waiting invisible element:\n {str(e)}')

    def waiting_for_element_visible(self, element):
        """
        Метод предназначен для ожидания видимости элемента (появится на странице)
        """
        try:
            WebDriverWait(self.driver, 240).until(EC.visibility_of_element_located(element))
        except TimeoutException as e:
            print(f'Time exception for waiting visible element:\n {str(e)}')

    def double_click(self, locator):
        """
        Метод предназначен для твойного клика по локатору
        """
        element = self.find_element(locator)

        action_chains = ActionChains(self.driver)
        return action_chains.double_click(element).perform()

    def execute_script(self, script, time_sleep=0):
        """
        Метод предназначен для выполнения скриптов js на странице
        """
        sleep(time_sleep)
        return self.driver.execute_script(f"{script}")

    def make_screenshot(self):
        """
        Метод предназначен для создания стриншота страницы и помещения его сразу в allure report
        В названии скрина дата и время
        """
        #time_to_fail = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        # allure.attach(self.driver.get_screenshot_as_png(), name=f"{time_to_fail}", attachment_type=AttachmentType.PNG)

    def select_elements_ctrl_click(self, *locators):
        """
        Метод предназначен для массового выделения через ctrl элементов на странице
        в *locators передается список элементов
        """
        action_chains = ActionChains(self.driver)
        action_chains.key_down(value=Keys.LEFT_CONTROL)
        for l in locators:
            el = self.find_element(l)
            action_chains.click(on_element=el)
        action_chains.key_up(value=Keys.LEFT_CONTROL)
        action_chains.perform()

    def custom_clearing_element(self, locator):
        element = self.find_element(locator)
        element.click()
        element.send_keys(Keys.END)
        while element.get_attribute('value') != '' or element.text != '':
            element.send_keys(Keys.BACKSPACE)
