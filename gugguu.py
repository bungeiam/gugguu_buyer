import time
import requests
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def availabilitycheck():
    r = requests.get("https://www.gugguu.com/collections/lapland-collection/products.json")

    products = json.loads(r.text)['products']

    for product in products:
        productname = product['title']
        time.sleep(0.2)
        print(productname)

        if productname == 'Print College':
            print("Found Item: ")
            print(productname)

            producturl = 'https://www.gugguu.com/collections/lapland-collection/products/' + product['handle']

            return producturl
    else:
        return False


def BuyProduct(url):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # go to url
    driver.get(url=str(url))

    # select type and size
    driver.find_element_by_xpath('//*[@value="Dino Rock"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@value="146"]').click()

    time.sleep(1)
    # add to cart
    driver.find_element_by_xpath('//*[@value="Lisää ostoskoriin"]').click()
    time.sleep(1)
    # go to checkout
    driver.get(url="https://www.gugguu.com/checkout")

    # enter email
    driver.find_element_by_xpath('//*[@id="checkout_email"]').send_keys("")

    # enter name
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_first_name"]').send_keys("")
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_last_name"]').send_keys("")

    # enter address
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_address1"]').send_keys("")
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_city"]').send_keys("")
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_zip"]').send_keys("")

    # enter phone number
    driver.find_element_by_xpath('//*[@id="checkout_shipping_address_phone"]').send_keys("")

    # go to next page
    driver.find_element_by_xpath('//*[@id="continue_button"]').click()
    time.sleep(5)

    # select shipping
    driver.find_element_by_xpath('//*[@data-shipping-method-label-title=""]').click()
    driver.find_element_by_xpath('//*[@id="continue_button"]').click()

    # select payment
    driver.find_element_by_xpath('//*[@value="25617170501"]').click()
    driver.find_element_by_xpath('//*[@id="continue_button"]').click()
    time.sleep(5)

    # make payment
    driver.find_element_by_xpath('//*[@id="placeOrderButton"]').click()
    time.sleep(3)
    iframe = driver.find_element_by_id("klarna-pay-later-fullscreen")
    driver.switch_to.frame(iframe)
    driver.find_element_by_xpath('//*[@id="purchase-approval-form-national-identification-number"]').send_keys("")
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="purchase-approval-form-continue-button"]').click()

    time.sleep(20)


while True:
    myUrl = availabilitycheck()
    if myUrl:
        BuyProduct(myUrl)
        print("Tuote tilattu")
        break

    else:
        print()
        print("Not found, re-scanning in 5 secs.")
        time.sleep(1)
        print("5")
        time.sleep(1)
        print("4")
        time.sleep(1)
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("Re-scanning....")
