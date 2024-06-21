import requests
from bs4 import BeautifulSoup

def get_recommendations(video_url):
    response = requests.get(video_url)
    print(response)
    soup = BeautifulSoup(response.text, 'html.parser')

    recommendations = []
    print("something is working")
    # Find the recommended videos section
    for video in soup.select('a#video-title'):
        title = video.get('title')
        video_id = video.get('href').split('=')[1]
        recommendations.append({'title': title, 'video_id': video_id})
        print(title)
    return recommendations

video_url = 'https://www.youtube.com/watch?v=AvgFmr-ckpk&list=RDAvgFmr-ckpk&start_radio=1'
recommendations = get_recommendations(video_url)

for rec in recommendations:
    print(f"Title: {rec['title']}, Video ID: {rec['video_id']}")
