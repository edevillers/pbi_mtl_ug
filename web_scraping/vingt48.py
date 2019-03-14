from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import datetime
import pandas as pd

browser = webdriver.Firefox()

browser.get('http://2048game.com/')

htmlElem = browser.find_element_by_tag_name('html')

def play_game(browser):
    htmlElem = browser.find_element_by_tag_name('html')
    while True:
        htmlElem.send_keys(Keys.DOWN)
        htmlElem.send_keys(Keys.LEFT)
        htmlElem.send_keys(Keys.UP)
        htmlElem.send_keys(Keys.RIGHT)
        
        # on veut voir si la game est finie, un peu de defensive programming
        try:
            game_over = browser.find_element_by_class_name("game-over")
            # on va aller chercher notre score 
            score_raw = browser.find_element_by_class_name("score-container").text
            score = score_raw.split("+")[0].replace('\n', '') # des fois on a des +4, des + 8, et des CR dans le score 
            print(score)
            print(game_over.text)
            now = str(datetime.datetime.now())
            return (score, now)
        except NoSuchElementException:
            pass

scores = []
dates = []

for i in range(2):
    score, now = play_game(browser)
    print(score, now)
    scores.append(score)
    dates.append(now)
    try_again = browser.find_element_by_class_name("retry-button")
    try_again.click()
print(scores)
print(dates)

# on peut fermer le browser
browser.quit()

# et mettre nos scores dans un dataframe pour analyse
df = pd.DataFrame(list(zip(scores,dates)),
                    columns=['Score', 'Date'])

print(df)