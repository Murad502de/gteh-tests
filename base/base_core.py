from base.base_router import BaseRouter
from base.base_elements_actions import BaseElementsActions


class BaseCore(BaseRouter, BaseElementsActions):

    def __init__(self, driver):
        super().__init__(driver)
