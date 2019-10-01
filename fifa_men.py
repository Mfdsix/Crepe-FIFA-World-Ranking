import requests
import time
import os
import sys
from bs4 import BeautifulSoup

def search_by_country(country, gender):
	request = requests.get(fifa_world_url+genders[gender])
	soup = BeautifulSoup(request.text, "html.parser")
	table = soup.find('table', class_="fi-table")
	tbody = table.find('tbody')
	rows = tbody.find_all('tr')

	world = 0;
	afc = 0;
	conmebol = 0;
	concacaf = 0;
	caf = 0;
	afc = 0;
	ofc = 0;
	found = False

	for row in rows : 
		columns = row.find_all('td')
		world_rank = columns[0].find('span').getText();
		country = columns[1].find('span', class_="fi-t__nText").getText()
		country_prefix = columns[1].find('span', class_="fi-t__nTri").getText()
		total_points = columns[2].find('span').getText();
		progress = columns[4].find('span').getText();
		flag = columns[6].find('span').getText();

		if flag == "#AFC#":
			afc += 1
			region = "AFC Rank : "+str(afc)
		elif flag == "#CONMEBOL#":
			conmebol += 1
			region = "Conmebol Rank : "+str(conmebol)
		elif flag == "#CONCACAF#":
			concacaf += 1
			region = "Concacaf Rank : "+str(concacaf)
		elif flag == "#CAF#":
			caf += 1
			region = "CAF Rank : "+str(caf)
		elif flag == "#OFC#":
			ofc += 1
			region = "OFC Rank : "+str(ofc)

		if country.lower() == team.lower() : 
			found = True
			break;
	os.system('clear')
	if found:
		print("FIFA World Football Rank for "+team.upper()+" "+genders[gender].upper())
		print("------------------------------------------")
		print("World Rank : "+world_rank)
		print(region)
		print("Points : "+total_points)
		print("Country Prefix : "+country_prefix)
		print("\n\n\n")
	else :
		print("The team name is not found")

fifa_world_url = "https://www.fifa.com/fifa-world-ranking/ranking-table/"
categories = ["World", "UEFA", "Conmebol","Concacaf", "CAF", "AFC", "OFC"]
genders = ["men", "women"]
prefix = ["", "UEFA", "CONMEBOL", "CONCACAF", "CAF", "AFC", "OFC"]
os.system('clear')
print("---------------------------------------------")
print("Welcome to FIFA World Football Rank System")
print("---------------------------------------------")
time.sleep(2)
os.system('clear')

print("What do you want?")
print("----------------------------")
print("1. See By Category")
print("2. See My Favourite National Team")

want = input()
os.system('clear')
time.sleep(1)

want = int(want)

if want != 1 and want != 2:
	print("Not Valid Input")
	sys.exit()
elif want == 2:
	print("Type your Favourite National Team")
	print("----------------------------")
	team = input()
	time.sleep(1)
	os.system('clear')

	print("Choose the gender")
	print("----------------------------")
	print("1. Men")
	print("2. Women")

	gender = input()

	os.system('clear')
	print("Processing ...")
	gender = int(gender)

	search_by_country(team, (gender-1))
	
elif want == 1:
	print("Choose the gender first")
	print("----------------------------")
	print("1. Men")
	print("2. Women")

	gender = input()
	os.system('clear')
	gender = int(gender)

	time.sleep(1)
	if gender != 1 and gender != 2:
		print("Not Valid Input")
		sys.exit()

	print("Choose number of categories Below")
	print("----------------------------")
	for i in range(7):
		print(str(i+1)+" "+categories[i])

	category = input()
	category = int(category)
	os.system('clear')
	
	if category < 1 or category > 7 :
		print("Not Valid Input")
		sys.exit()

	else :
		print("Processing ...")
		request = requests.get(fifa_world_url+genders[gender-1])
		soup = BeautifulSoup(request.text, "html.parser")
		table = soup.find('table', class_="fi-table")
		tbody = table.find('tbody')
		rows = tbody.find_all('tr')

		base_url = "https://www.fifa.com";
		rank = 1;
		os.system('clear')
		for row in rows : 
			columns = row.find_all('td')
			world_rank = columns[0].find('span').getText();
			# detail_link = columns[1].find('a', class_="fi-t__link")['href']
			# image = columns[1].find('img', class_="fi-flag--4")['src']
			country = columns[1].find('span', class_="fi-t__nText").getText()
			country_prefix = columns[1].find('span', class_="fi-t__nTri").getText()
			total_points = columns[2].find('span').getText();
			# prev_points = columns[3].find('span').getText();
			progress = columns[4].find('span').getText();
			flag = columns[6].find('span').getText();

			if prefix[category-1] != "" and "#"+prefix[category-1]+"#" != flag :
				continue

			if progress != "-" and int(progress) > 0 :
				progress = "+"+progress

			print("-------------------")
			print(str(rank)+". "+country+" ("+country_prefix+")")
			# print("Detail Link : "+base_url+detail_link)
			# print("Image Link : "+image)
			print("Total Points : "+total_points)
			# print("Prev Points : "+prev_points)
			print("Progress : "+progress)

			if prefix[category-1] != "" : 
				print("World Rank : "+world_rank)
			rank += 1