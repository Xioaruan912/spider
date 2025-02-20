from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def name_check(driver):  # 参数名称改为driver更清晰
    try:

        name_str = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[7]/div/div/div[2]/div[1]/div[1]/div/div[1]/a")
            )
        )
        logger.debug(name_str.text)  # 获取元素文本内容

    except Exception as e:
        logger.error(f"元素定位失败: {str(e)}")