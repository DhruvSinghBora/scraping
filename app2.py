from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_recommendations(video_url):
    # Set up Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Navigate to the YouTube video page
    driver.get(video_url)
    
    recommendations = []
    
    # Wait for the elements to load
    driver.implicitly_wait(10)
    
    # Find the recommended videos section
    video_elements = driver.find_elements(By.CSS_SELECTOR, 'a#video-title')
    
    for video in video_elements:
        title = video.get_attribute('title')
        video_url = video.get_attribute('href')
        recommendations.append({'title': title, 'video_url': video_url})
    
    driver.quit()
    
    return recommendations

video_url = 'https://www.youtube.com/watch?v=AvgFmr-ckpk&list=RDAvgFmr-ckpk&start_radio=1'
recommendations = get_recommendations(video_url)

for rec in recommendations:
    print(f"Title: {rec['title']}, Video URL: {rec['video_url']}")
