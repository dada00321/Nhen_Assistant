from modules.basic_scraping_module import *

def scraping_book(busNum):
    url = f"https://nhentai.net/g/{busNum}/"
    print(f"正在爬本本: {busNum}")
    r = get_response(url)
    soup = get_soup(r)
    #//div[@id='thumbnail-container'] -- X
    #//div[@id='thumbs']
    pics = soup.find("div", class_="thumbs")
    #print(pics.attrs)
    
    #//div[@class='thumbs']//div
    pics_count = len(pics.find_all("div"))
    print(f"Total: {pics_count} images")
    
    # pattern:
    #print(pics.find("img")["data-src"])
    img_pattern = pics.find("img")["data-src"]
    #print(img_pattern)
    #print('/'.join(img_pattern.split("/")[:-1]))
    img_pattern = '/'.join(img_pattern.split("/")[:-1])
    
    for i in range(1, pics_count+1):
        partial = f"/{i}t.jpg"
        print(f"圖片{i}下載中")
        imgUrl = img_pattern + partial
        #print(imgUrl)
        download_pic(i, imgUrl, busNum)
        
def scraping_many_books():
    path = "BusNumbers.txt"
    with open(f"res/{path}", 'r') as fp:
        data = fp.read()
        data = data.replace("\n", " ")
        #print(data.split())
        busNum_list = data.split()
        #print(*(e for e in busNum_list))
        for busNum in busNum_list:
            scraping_book(busNum)

if __name__ == "__main__":
    busNum = 196970 # 本本號
    scraping_book(busNum)
    #scraping_many_books()
        