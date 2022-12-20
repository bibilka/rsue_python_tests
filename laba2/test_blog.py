from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test(successful_title):
    """
    функция для тестирования поиска статьи на сайте
    :successful_title: ожидаемый заголовок найденной статьи
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)

    # url = "https://blog.noveogroup.ru/"
    # этот сайт недоступен на момент выполнения лабораторной
    url = "https://блог.новео.рф"
    driver.get(url)

    sleep(1)
    search = "валидация"
    driver.find_element(By.CSS_SELECTOR, "[type=search]").send_keys(search)
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "[type=search]").send_keys(Keys.ENTER)

    sleep(1)
    driver.find_element(By.TAG_NAME, "article").click()

    sleep(1)
    title = driver.find_element(By.CSS_SELECTOR, "article>header>h2").text
    assert title == successful_title, "Test Failed"
    print("Yeah! thats it!")

    sleep(1)
    driver.close()

print("test case 1")
test("Валидация данных в Nest")

print("test case 2 wrong")
test("Wrong title")