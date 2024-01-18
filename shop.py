# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# driver.find_element_by_link_text("My Account").click()
# time.sleep(3)
# driver.find_element_by_id("username").send_keys("123av@mail.ru")
# driver.find_element_by_id("password").send_keys("?12a45!Av!")
# time.sleep(3)
# driver.find_element_by_class_name("form-row").click()
# time.sleep(3)
# driver.find_element_by_id("menu-item-40").click()
# time.sleep(3)
# driver.find_element_by_class_name("post-181").click()
# time.sleep(3)
# name = driver.find_elements_by_partial_link_text("HTML5 Forms")
# if name is not None:
#     print("Название книги HTML5 Forms")
# else:
#     print("Название книги другое")
# driver.quit()
import time

# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# driver.find_element_by_link_text("My Account").click()
# time.sleep(3)
# driver.find_element_by_id("username").send_keys("123av@mail.ru")
# driver.find_element_by_id("password").send_keys("?12a45!Av!")
# time.sleep(3)
# driver.find_element_by_class_name("form-row").click()
# time.sleep(3)
# driver.find_element_by_id("menu-item-40").click()
# time.sleep(3)
# driver.find_element_by_class_name("cat-item-19").click()
# products = driver.find_element_by_class_name("masonry-done")
# if products is not None:
#     print ("На странице 3 товара")
# else:
#     print ("На странице больше или меньше 3 товаров")
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
# driver.find_element_by_link_text("My Account").click()
# time.sleep(3)
# driver.find_element_by_id("username").send_keys("123av@mail.ru")
# driver.find_element_by_id("password").send_keys("?12a45!Av!")
# time.sleep(3)
# driver.find_element_by_class_name("form-row").click()
# time.sleep(3)
# driver.find_element_by_id("menu-item-40").click()
# time.sleep(3)
# status_selector = driver.find_element_by_class_name("woocommerce-ordering")
# status_selector_menu_order = status_selector.get_attribute("value")
# if status_selector_menu_order == "Default sorting":
#     print("Выбрано значение Default sorting")
# else:
#     print("Выбрано другое значение")
# driver.find_element_by_tag_name("select").click()
# driver.find_element_by_css_selector("option:nth-child(6)").click()
# time.sleep(3)
# selector = driver.find_element_by_class_name("woocommerce-ordering")
# selector_price_desc = selector.get_attribute("value")
# if selector_price_desc == "Sort by price: high to low":
#     print("Выбрано значение Sort by price: high to lo")
# else:
#     print("Выбрано другое значение")
# driver.quit()


# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_link_text("My Account").click()
# driver.find_element_by_id("username").send_keys("123av@mail.ru")
# driver.find_element_by_id("password").send_keys("?12a45!Av!")
# driver.find_element_by_class_name("form-row").click()
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_css_selector(".post-169 h3").click()
# book_old_price = driver.find_element_by_css_selector(".price > del > span")
# book_old_price_text = book_old_price.text
# book_new_price = driver.find_element_by_css_selector(".price > ins > span")
# book_new_price_text = book_new_price.text
# assert book_old_price_text == "₹600.00"
# assert book_new_price_text == "₹450.00"
# book_cover = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# book_cover.click()
# book_cover_close = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# book_cover_close.click()
# driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-40").click()
# driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]').click()
# product = driver.find_element_by_class_name("cartcontents")
# product_text = product.text
# price = driver.find_element_by_class_name("amount")
# price_text = price.text
# assert product_text == "1 item"
# assert price_text == "₹180.00"
# time.sleep(5)
# driver.find_element_by_class_name("wpmenucart-contents").click()
# subtotal_text = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "cart-subtotal"), "₹180.00"))
# total_text = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "order-total"), "₹183.60"))
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]').click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="content"]/ul/li[5]/a[2]').click()
# driver.find_element_by_class_name("wpmenucart-contents").click()
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="page-34"]/div/div[1]/form/table/tbody/tr[1]/td[1]/a').click()
# time.sleep(3)
# driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > div.woocommerce-message > a").click()
# time.sleep(3)
# driver.find_element_by_css_selector("tr:nth-child(1) > td.product-quantity > div > input").clear()
# driver.find_element_by_css_selector("tr:nth-child(1) > td.product-quantity > div > input").send_keys("3")
# driver.find_element_by_css_selector("tr:nth-child(3) > td > input.button").click()
# time.sleep(3)
# driver.find_element_by_css_selector("tr:nth-child(3) > td > div > input.button").click()
# coupon_cod = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-error"), "Please enter a coupon code."))
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.find_element_by_id("menu-item-40").click()
# driver.execute_script("window.scrollBy(0, 300);")
# driver.find_element_by_xpath('//*[@id="content"]/ul/li[4]/a[2]').click()
# time.sleep(5)
# driver.find_element_by_class_name("wpmenucart-contents").click()
# checkout_btn = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
# checkout_btn.click()
# first_name = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.ID, "billing_first_name")))
# first_name.send_keys("Victoria")
# last_name = driver.find_element_by_id("billing_last_name")
# last_name.send_keys("Pav")
# email = driver.find_element_by_id("billing_email")
# email.send_keys("123av@mail.ru")
# phone = driver.find_element_by_id("billing_phone")
# phone.send_keys("546783821")
# driver.find_element_by_id("s2id_billing_country").click()
# country = driver.find_element_by_css_selector("#s2id_autogen1_search")
# country.send_keys("Russia")
# driver.find_element_by_class_name("select2-match").click()
# address = driver.find_element_by_id("billing_address_1")
# address.send_keys("Nevsky prospect 12")
# city = driver.find_element_by_id("billing_city")
# city.send_keys("St. petersburg")
# state_country = driver.find_element_by_id("billing_state")
# state_country.send_keys("Russia")
# zip = driver.find_element_by_id("billing_postcode")
# zip.send_keys("12345")
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(5)
# check = driver.find_element_by_id("payment_method_cheque")
# check.click()
# place_order = driver.find_element_by_id("place_order")
# place_order.click()
# element = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# element2 = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#page-35 > div > div.woocommerce > ul > li.method"), "Check Payments"))
# driver.quit()

