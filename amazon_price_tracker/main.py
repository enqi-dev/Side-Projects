import requests
from bs4 import BeautifulSoup
from email_manager import EmailManager

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers={"Accept-Language": "en-US,en;q=0.9", 
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

response = requests.get(url=URL, headers=headers)
contents = response.text

soup = BeautifulSoup(contents, "lxml")
manage_email = EmailManager()

text = [i.getText() for i in soup.findAll(name="span", class_="a-offscreen")]
price = float(text[0].strip("$"))
product_title = (soup.find(name="span", id="productTitle").getText()).strip()


if price < 100:
    message_text = f"{product_title}\n${price}\n{URL}"
    manage_email.send_email(message=message_text, sub="Subject:Amazon Price Alert!")