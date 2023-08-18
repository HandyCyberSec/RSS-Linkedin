import requests
import feedparser

# Replace with your actual credentials
access_token = 'YOUR_ACCESS_TOKEN'

# URL for posting a company update
post_url = 'https://api.linkedin.com/v2/shares'

# Company page ID
company_id = 'YOUR_COMPANY_ID'

# URL of the RSS feed
rss_feed_url = 'URL_TO_YOUR_RSS_FEED'

# Parse the RSS feed
feed = feedparser.parse(rss_feed_url)

if not feed.entries:
    print('No entries found in the RSS feed.')
    exit()

# Get the latest entry from the RSS feed
latest_entry = feed.entries[0]
update_text = latest_entry.title + '\n' + latest_entry.description + '\n' + latest_entry.link

# Create the headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Create the JSON payload
payload = {
    'owner': f'urn:li:organization:{company_id}',
    'text': {
        'text': update_text
    }
}

# Make the API request
response = requests.post(post_url, headers=headers, json=payload)

# Check the response
if response.status_code == 201:
    print('Update posted successfully!')
else:
    print('Error posting update:', response.status_code, response.json())
