from selenium.webdriver.common.by import By

class Page:
        logo_button= By.ID, "logom"
        scroll_up_button = By.XPATH, "//a[@class='backToTop__BtnGoUp-sc-1deq75d-0 fIqtKc']"
        whatsapp_button = By.XPATH, "//a[@class='callUsWhatsapp__BtnWhatsapp-sc-1bcgurk-0 cPQmgB']"
        whatsapp_identify = By.XPATH, "//a[@class='_36or _2zq_']"
        name_input = By.ID, "name"
        company_input = By.ID, "company"
        email_input = By.ID, "email"
        phone_input = By.ID, "telephone"
        talk_to_us_button = By.XPATH, "//a[@class='commun__Button-mgrfny-0 commun__ButtonContact-mgrfny-1 form__ButtonContact-sc-1ju2h8q-1 gGWtQr']"
        thank_you = By.XPATH, "//span[contains(text(),'תודה!')]"
        over_lay = By.XPATH, "//div[@class='ReactModal__Overlay ReactModal__Overlay--after-open']"

class ourJobs:
       right_arrow = By.XPATH, "//div[@class='slick-arrow slick-next']"
       left_arrow = By.XPATH, "//div[@class='slick-arrow slick-prev']"
       root = By.XPATH, "//div[@class='slick-slider portfolio__Slider-sc-1bteqw2-2 idRhPL slick-initialized']"
class ourCustomers:
        navigator = By.CSS_SELECTOR, "div:nth-child(1) div.layout__Layout-k13eu9-0.fkvIOy section.customers__Customers-sc-1w1u0ay-0.eDDkCa:nth-child(9) div.customers__Container-sc-1w1u0ay-2.gfsorQ > div.slick-slider.customers__Slider-sc-1w1u0ay-4.bSKFKn.slick-initialized"