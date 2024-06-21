import asyncio
from pyppeteer import launch

async def get_recommendations(video_url):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(video_url)
    
    recommendations = []

    # Wait for the video recommendations to load
    await page.waitForSelector('a#video-title')

    # Get all recommended video titles and URLs
    video_elements = await page.querySelectorAll('a#video-title')

    for video in video_elements:
        title = await (await video.getProperty('title')).jsonValue()
        href = await (await video.getProperty('href')).jsonValue()
        video_id = href.split('v=')[-1]
        recommendations.append({'title': title, 'video_id': video_id})
    
    await browser.close()
    return recommendations

# URL of the YouTube video
video_url = 'https://www.youtube.com/watch?v=AvgFmr-ckpk&list=RDAvgFmr-ckpk&start_radio=1'

# Run the asyncio event loop to execute the async function
recommendations = asyncio.get_event_loop().run_until_complete(get_recommendations(video_url))

for rec in recommendations:
    print(f"Title: {rec['title']}, Video ID: {rec['video_id']}")
