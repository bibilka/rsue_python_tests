from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException


def test(email, password):
    """
    функция для тестирования авторизации
    :email: email для авторизации
    :password: пароль для авторизации
    """
    s = Service('../chromedriver.exe')

    driver = webdriver.Chrome(service=s)
    driver.get('https://adminqa.neapro.site/login')
    driver.set_window_size(1024, 600)
    driver.minimize_window()

    driver.find_element(By.XPATH, '//*[@id="admin_email"]').send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="admin_password"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[@id="admin_submit_action"]/input').click()

    # проверяем что появился элемент в шапке страницы содержащий ссылку на переход в аккаунт
    # если такой элемент есть - значит авторизация прошла успешно
    try:
        driver.find_element(By.XPATH, '//*[@id="current_user"]')
        print("Test Passed Successfully")
    except NoSuchElementException:
        print("Test failed ;(")
    driver.close()


# выполняем тестирование с разными параметрами
print("Test case 1")
test("wrong_email@mail.ru", "wrong_password")
print("test case 2")
test("moderat@neapro.ru", "Aa123456")
