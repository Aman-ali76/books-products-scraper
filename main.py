import requests
from bs4 import BeautifulSoup
import os
import pandas as pd


while True:
    try:

        if os.path.isfile('page_num.txt') == False:
            with open('page_num.txt', 'w') as f:
                f.write('1')
                num = 1
        else:
            with open('page_num.txt' , 'r') as f:
                num = f.read()
                num = int(num)
        

        url = f"https://books.toscrape.com/catalogue/page-{num}.html"

        response = requests.get(url)

        if response.status_code == 404:
            print('No more pages')
            break
        elif response.status_code == 200:

            soup = BeautifulSoup(response.text, 'html')

            main = soup.find('ol')
            books = main.find_all('li')

            df = pd.DataFrame(columns= ['Product Number', 'Product Name' , 'Price' , 'Stock Avalibility', 'Image URL'])

            for single in books:
                title_h3 = single.find('h3')
                title = title_h3.a['title']
                price_div = single.find_all('div')
                price = price_div[1].p.text
                stock = price_div[1].find('p', class_='instock availability').text.strip()
                img = single.find('img')
                base_link = 'https://books.toscrape.com/'
                image_url_final = base_link + img['src'].lstrip('../../')
                lenght = len(df)
                df.loc[lenght] = [lenght+1, title, price, stock, image_url_final]

            os.makedirs('CSV_Books', exist_ok=True)

            with open('page_num.txt', 'w') as f2:
                f2.write(f'{num+1}')

            df.to_csv(f'CSV_Books/Page_{num}.csv', index=False)
            print(f"Page {num}.csv is created")

        else :
            print('Error in retriving data')
            print(response.status_code)
            break

    except KeyboardInterrupt:
        print("Program is terminated by the user")
        break


           


