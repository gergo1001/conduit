import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pages.func as f
import pages.page_registration as p
import pages.page_signin as s
import pages.page_editor as e
import pages.page_article as a
import pages.class_article as ca
import csv
from webdriver_manager.chrome import ChromeDriverManager


class PageMain:
    URL = "http://localhost:1667/"
    # articles
    articles = []
    articles_xpath = "//*[@class='preview-link']"
    a_link_attritube = 'href'
    a_tittle_tag = 'h1'
    a_shorttext_tag = 'h1'

    # global feed link
    global_feed_xpath = '/html/body/div[1]/div/div[2]/div/div[1]/div[1]/ul/li[2]/a'
    # cookis elérések
    cookies_accept_button_xpath = "//button[@class='cookie__bar__buttons__button cookie__bar__buttons__button--accept']"
    cookies_decline_button_xpath = "//button[@class='cookie__bar__buttons__button cookie__bar__buttons__button--decline']"
    cookies_page_link_xpath = "//a[@href='https://cookiesandyou.com/']"
    cookie_name = "vue-cookie-accept-decline-cookie-policy-panel"

    # sign in elérése
    registration_link_xpath = '//li[@class="nav-item"]/a[@href="#/register"]'
    signin_link_xpath = '//li[@class="nav-item"]/a[@href="#/login"]'
    editor_link_xpath = '//li[@class="nav-item"]/a[@href="#/editor"]'

    # menű elemek elérése
    menu_items_classname = 'nav-item'
    # belépett felhasználó esetén
    home_pos_signin = 0
    newarticle_pos_signin = 1
    settings_pos_signin = 2
    username_pos_signin = 3
    logout_pos_signin = 4

    # ha nincs bejelentkezett felhasznalo
    home_pos_signout = 0
    signin_pos_signout = 1
    signup_pos_signout = 1

    # pages
    page_links_xpath = "//ul[@class='pagination']/li/a"

    def __init__(self):
        if not f.webpage_visible:
            browser_options = Options()
            browser_options.add_experimental_option("excludeSwitches", ["enable-logging"])
            browser_options.headless = True
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)

        else:
            browser_options = Options()
            browser_options.headless = False
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=browser_options)
        time.sleep(0.5)

    def all_article_list(self):
        self.driver.find_element_by_xpath(self.global_feed_xpath).click()
        time.sleep(2)

    def open(self):
        self.driver.get(self.URL)
        time.sleep(1)

    def regpage_open(self):
        self.driver.find_element_by_xpath(self.registration_link_xpath).click()
        time.sleep(1)
        return p.PageRegistration(self.driver)

    def signinpage_open(self):
        self.driver.find_element_by_xpath(self.signin_link_xpath).click()
        time.sleep(1)
        return s.PageSignin(self.driver)

    def newarticlepage_open(self):
        self.driver.find_element_by_xpath(self.editor_link_xpath).click()
        time.sleep(1)
        return e.PageEditor(self.driver)

    def get_user_sign_in(self, username):
        menu_items = self.driver.find_elements_by_class_name(self.menu_items_classname)
        if len(menu_items) > 3:
            if username == menu_items[self.username_pos_signin].text:
                return True
        return False

    def logout_click(self):
        menu_items = self.driver.find_elements_by_class_name(self.menu_items_classname)
        if len(menu_items) > 4:
            menu_items[self.logout_pos_signin].click()
            return True
        return False

    def deletecookies(self):
        self.driver.delete_all_cookies()

    def getcookies(self):
        value = ""
        cookies = self.driver.get_cookie(self.cookie_name)
        if cookies is not None:
            if 'value' in cookies.keys():
                value = cookies['value']
        return value

    def cookies_accept(self):
        self.driver.find_element_by_xpath(self.cookies_accept_button_xpath).click()
        time.sleep(1)

    def cookies_decline(self):
        self.driver.find_element_by_xpath(self.cookies_decline_button_xpath).click()
        time.sleep(1)

    def cookies_button_visible(self):
        ok_value = True
        accept_buttons = self.driver.find_elements_by_xpath(self.cookies_accept_button_xpath)
        if len(accept_buttons) != 1:
            ok_value = False
        else:
            if not accept_buttons[0].is_displayed():
                ok_value = False

        decline_buttons = self.driver.find_elements_by_xpath(self.cookies_decline_button_xpath)
        if len(decline_buttons) != 1:
            ok_value = False
        else:
            if not decline_buttons[0].is_displayed():
                ok_value = False
        return ok_value

    def cookies_website_click(self):
        self.driver.find_element_by_xpath(self.cookies_page_link_xpath).click()
        time.sleep(1)

    def get_and_close_second_window_url(self):
        url = ""
        current = self.driver.current_window_handle
        multi_window = self.driver.window_handles

        for window in multi_window:
            if window != current:
                self.driver.switch_to.window(window)
                time.sleep(1)
                url = self.driver.current_url
                self.driver.close()
        self.driver.switch_to.window(current)
        time.sleep(1)
        return url

    def get_pages_count(self):
        self.all_article_list()
        return len(self.driver.find_elements_by_xpath(self.page_links_xpath))

    def fill_article(self):
        self.all_article_list()
        self.articles.clear()
        pages = self.driver.find_elements_by_xpath(self.page_links_xpath)
        bejart_lap = 0
        for page in pages:
            bejart_lap += 1
            page.click()
            time.sleep(1)
            articles = self.driver.find_elements_by_xpath(self.articles_xpath)
            for article in articles:
                link = article.get_attribute(self.a_link_attritube)
                titles = article.find_elements_by_tag_name(self.a_tittle_tag)
                title = titles[0].text
                shorttext = article.find_element_by_tag_name('p').text
                tags_all = article.find_element_by_class_name("tag-list")
                tags = tags_all.find_elements_by_tag_name('a')
                tag_text = []
                for tag in tags:
                    tag_text.append(tag.text)

                article_element = ca.Article(link, title, shorttext, tag_text, None)
                self.articles.append(article_element)
        return bejart_lap

    # ha nincs előtte közvetlen cikk listázás, akkor fel kell tölteni
    def del_article(self, tittle, must_fillarticle):
        if must_fillarticle:
            self.fill_article()
        for article in self.articles:
            if article.title == tittle:
                self.article_open(article.link)
                p_article = a.PageArticle(self.driver)
                p_article.delete_article()

    def search_article_with_title(self, title):
        self.fill_article()
        volt = False
        for article in self.articles:
            if article.gettitle() == title:
                volt = True
        return volt

    def none_repeat_tittle(self):
        self.fill_article()
        tittles = []
        for article in self.articles:
            if article.title not in tittles:
                tittles.append(article.title)
            else:
                return False
        return True

    def none_repeat_tittle_from_list_article(self, articles_tittles):
        self.fill_article()
        tittles = []
        for article in self.articles:
            if article.title in articles_tittles:
                if article.title not in tittles:
                    tittles.append(article.title)
                else:
                    return False
        return True

    # meghivása után kell a close() is, hogy visszatérjen
    def article_open(self, link):
        self.driver.get(link)
        time.sleep(1)
        return a.PageArticle(self.driver)

    def article_close(self):
        self.driver.back()
        time.sleep(1)

    def article_shorttext_van(self, tittle, shorttext):
        self.fill_article()
        for article in self.articles:
            if article.title == tittle:
                if article.shorttext == shorttext:
                    return True
        return False

    def articles_write_to_file(self, filenev):
        self.fill_article()
        with open(filenev, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            fieldnames = ['tittle', 'shorttext']
            writer = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
            writer.writerow(fieldnames)
            row_count=0
            for article in self.articles:
                row_count +=1
                writer.writerow([article.gettitle(), article.getstext()])
        return row_count

    def get_article(self, must_fillarticle):
        if must_fillarticle:
            self.fill_article()
        return len(self.articles)

    def __del__(self):
        self.driver.quit()
