import requests
from bs4 import BeautifulSoup
import webbrowser

class scraper:
    def __init__(self):
        pass


    def cheat_sheet_scraper(self, topic):
        url = f"https://quickref.me/{topic}"
        w = requests.get(url)
        print(url)

        if w.status_code == 200:
            print('you can proceed')
        else:
            print("you can't")

        main_obj = BeautifulSoup(w.content,'html.parser')
        sheet= main_obj.find_all('code' , class_ = f"hljs language-{topic}")

        print('success')

        try:
            with open(f'{topic}.txt', 'a+', encoding = 'UTF-8') as file:
                for code in sheet:
                    ref = code.get_text()
                    file.write(f'{ref}')
        except IOError as e:
            print(f"File handling error: {e}")
        except Exception as e:
            print(f"Error parsing HTML content: {e}")

        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    
    def newslink_scraper(self, title):
        url = f'https://timesofindia.indiatimes.com/topic/{title}'

        response = requests.get(url)

        if response.status_code == 200:
            print("Page fetched successfully")
        else:
            print('Failed to fetch page')

        soup = BeautifulSoup(response.content, 'html.parser')
        articles = soup.find_all('div', class_='uwU81')

        for article in articles:
            anchor = article.find('a')
            if anchor:
                href = anchor.get('href')
                text = anchor.get_text(strip=True)
                # print(f"Link: {href}")
                # print(f"Text: {text}")
                with open(f"{title}.txt",'a+',encoding='utf-8') as file:
                    file.write(f"Link: {href}\n")
                    file.write(f"Text: {text}\n\n")


    def minitv_scraper(self, menu):
        url = f"https://www.amazon.in/minitv/ct/{menu}"
    
    # Fetch the webpage
        w = requests.get(url)

        if w.status_code == 200:
            print("Processing...")
        else:
            print("Failed to fetch the webpage. Status code:", w.status_code)
            exit()

        # Parse the HTML content
        obj = BeautifulSoup(w.content, 'html.parser')

        # Find all anchor tags with the specified class that contain series links
        anchors = obj.find_all('a', class_='normalisedLink ThumbnailCard_thumbnailLinkWrapper__kxFo8')

        hreflist = []

        # Extract href attribute from each anchor tag
        for anchor in anchors:
            href = anchor.get('href')
            if href.startswith('/'):
                href = f"https://www.amazon.in{href}"  # Complete the relative URL
            hreflist.append(href)

        # Process each URL
        with open('list.txt', 'a+', encoding='UTF-8') as file:
            for index, p_url in enumerate(hreflist):
                try:
                    p_w = requests.get(p_url)
                    raj = BeautifulSoup(p_w.content, 'html.parser')

                    # Extract title and genre
                    title = raj.find('h1', {'data-testid': 'titleScreen_descriptionCard_title'}).text.strip()
                    genre = raj.find('p', {'data-testid': 'titleScreen_descriptionCard_genre'}).text.strip()

                    # Write details to file
                    file.write(f"Name of series: {title}\n")
                    file.write(f"Genre: {genre}\n")
                    file.write(f"URL: {p_url}\n\n")

                    # print(f"Processed page #{index + 1}: {p_url}")

                except requests.exceptions.RequestException as e:
                    print(f"Error fetching URL {p_url}: {e}")
                    continue
                except AttributeError as ae:
                    print(f"Error parsing content for URL {p_url}: {ae}")
                    continue
                
        print("Process completed. Check 'list.txt' for details.")
        
    

# topic=input("enter topic ")
# scraper.cheat_sheet_scraper(topic)


# while True:

#     print(''' \033[92m
#         [1] cheat sheet scraper   
#         [2] Important news title and link scraper
#         [3] Minitv genre scraper
#         [4] Exit
# ''')
#     option = input("please select any option: ")
#     if option == '1':
#         topic = input("please enter your topic: ")
#         if not topic:
#             print("topic is not provided yet!!!")
#         else:
#             scraper.cheat_sheet_scraper(topic)
#     elif option == '2':
#         title = input("enter your title to get news: ")
#         if not title:
#             print("provide your title please ")
#         else:
#             scraper.newslink_scraper(title)
#     elif option == '3':
#         while True:
#             print('''\033[91m       [a] scrape
#        [b] stream
#        [c] back''')
#             click = input("select an option: ") 
#             if click == 'a':
#                 while True:
#                     print('''
#     [a] Home
#                              [b] Imported
#                              [c] Web series 
#                              [d] Movies
#                              [e] Romance
#                              [f] Comedy 
#                              [g] Tamil
#                              [h] Telugu 
#                              [i] Back''')
#                     menu = input('enter any choice of your desired menu: ')
#                     if menu == 'a':
#                         menu = 'home'
#                         scraper.minitv_scraper(menu)
#                     elif menu == 'b':
#                         menu = 'imported'
#                         scraper.minitv_scraper(menu)
#                     elif menu == 'c':
#                         menu = 'webseries'
#                         scraper.minitv_scraper(menu)
#                     elif menu == 'd':
#                         menu = 'movies'
#                         scraper.minitv_scraper(menu)
#                     elif menu == 'e':
#                         menu = 'romance'
#                         scraper.minitv_scraper(menu)
#                     elif menu == 'f':
#                         menu = 'comedy'
#                         scraper.minitv_scraper(menu)
#                     elif menu == 'g':
#                         menu = 'Tamil'
#                         scraper.minitv_scraper(menu)
#                     elif menu == 'h':
#                         menu = 'Telugu'
#                         scraper.minitv_scraper(menu)
#                     elif menu == 'i':
#                         break

#             elif click == 'b':
#                 url = input(" enter your minitv url: ")
#                 if not url:
#                     print('provide an url!!') 
#                 else:
#                     webbrowser.open(url , 0)
#             elif click == 'c':
#                 break 
 
#     elif option == '4':
#         print('\n\033[97m thank you ')
#         break             