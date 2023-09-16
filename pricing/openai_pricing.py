from bs4 import BeautifulSoup
from pyppeteer import launch
import asyncio
import json

pricingPageUrl = "https://openai.com/pricing"

async def get_loaded_html():
    browser = await launch({"headless": True})
    page = await browser.newPage()
    await page.goto('https://openai.com/pricing')

    # Get the loaded HTML content
    html_content = await page.content()

    await browser.close()
    return html_content

def extract_openai_pricing(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extracting the pricing details for the various models
    pricing_details = {}
    # Extracting Language Models Pricing
    language_models = soup.find_all('div', {'class': 'container'})
    for model in language_models:
        model_object = model.find('h3')
        if model_object:
            model_name = model_object.text.strip()
        else:
            continue
        model_prices = []
        table = model.find('table')
        if not table:
            continue
        rows = table.find_all('tr')
        firstRow = rows[0]
        columnlen = len(firstRow.find_all('td'))
        # loop over columnlen and get object field names
        for row in rows[1:]:  # Skip the header row
            tds = row.find_all('td')
            propObject = {}
            for i in range(columnlen):
                fieldValue = firstRow.find_all('td')[i].span.text.strip()
                propObject[fieldValue] = tds[i].span.text    
            model_prices.append(propObject)
        pricing_details[model_name] = model_prices
    # You can add more sections similarly if needed
    return pricing_details

def writeRawHtmlData(pricingPageRawHtml,current_datetime):
    current_datetimeiso = current_datetime.isoformat()
    with open(current_datetimeiso+"_pricing_response.html", "w") as f:
            f.write(pricingPageRawHtml)



def getPricingDetailsFromOpenAI(current_datetime):
    pricingPageRawHtml = asyncio.get_event_loop().run_until_complete(get_loaded_html())
    writeRawHtmlData(pricingPageRawHtml,current_datetime)
    pricing_details = extract_openai_pricing(pricingPageRawHtml)

    return pricing_details