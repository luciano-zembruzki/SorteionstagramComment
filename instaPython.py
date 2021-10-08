from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import os
import random
import fnmatch
import os
import csv


class Instabot:
	def __init__(self,username,password, post_to_comment):
		options = webdriver.ChromeOptions()
		# options.add_argument('--headless')
		# options.add_argument('--no-sandbox')
		# options.add_argument('--disable-dev-shm-usage')
		browser = webdriver.Chrome('./chromedriver',options=options)

		browser.get("http://instagram.com")

		username_element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
		password_element = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

		username_element.send_keys(username)
		password_element.send_keys(password)

		submit = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))

		submit.click()

		not_now = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))

		not_now.click()

		sleep(2)
		for _ in range(10000):
			count = 0
			for _ in range(6):
				try:
					to_comment_list = []
					with open('to_comment.txt') as to_comment:
						for line in to_comment:
							to_comment_list.append(line.strip())
					count = count + 1
					sleep(3)
					post = post_to_comment
					browser.get(post)
					sleep(3)
					comment_box = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')))				
					user = random.choice(to_comment_list)
					comment_box.click()
					sleep(1)
					comment_box = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')))
					comment_box.send_keys(user)
					sleep(2)
					post_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button[2]')))
					post_button.click()
					sleep(10)
					bill=open('commented.txt','a+')
					bill.write('\n')
					bill.write(user)
					bill.close()
					print(user)
					if count == 5:
						sleep(300)
					else:
						sleep(random.randint(60,90))
				except:
					print('Something does not work fine')
					pass
class Main:
	username = 'seu_usuário'
	password = 'sua_senha'
	post_to_comment = 'post_sorteio'
	Instabot(username,password, post_to_comment)

Main()
