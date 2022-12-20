from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test(slug, successful_title):
    """
    функция для тестирования поиска статьи на сайте
    :slug: чпу сегмент требуемой статьи
    :successful_title: ожидаемый заголовок найденной статьи
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)

    # url = "https://blog.noveogroup.ru/"
    # этот сайт недоступен на момент выполнения лабораторной
    url = "https://блог.новео.рф" + '/' + slug
    driver.get(url)

    sleep(1)
    title = driver.find_element(By.CSS_SELECTOR, "article>header>h2").text
    assert title == successful_title, "Test Failed"
    print("Yeah! thats it!")

    sleep(1)
    driver.close()

print("test case 1")
test("2022/10/validatsiya-dannyh-v-nest/", "Валидация данных в Nest")

print("test case 2")
test("2022/09/timbilding-ekstrima-i-prikljuchenij/", "Тимбилдинг экстрима и приключений!")

print("test case 3")
test("2022/09/timbilding-ekstrima-i-prikljuchenij/", "Тимбилдинг приключений и экстрима?")