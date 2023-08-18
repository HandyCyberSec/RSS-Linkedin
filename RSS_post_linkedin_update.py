import requests
import feedparser

# URL of the RSS feed
rss_feed_url = 'URL_TO_YOUR_RSS_FEED'

# Parse the RSS feed
feed = feedparser.parse(rss_feed_url)

if not feed.entries:
    print('No entries found in the RSS feed.')
    exit()

# Display the latest entry from the RSS feed in the terminal
latest_entry = feed.entries[0]
print('Title:', latest_entry.title)
print('Description:', latest_entry.description)
print('Link:', latest_entry.link)
print()

# Replace with your actual credentials
access_token = 'YOUR_ACCESS_TOKEN'

# URL for posting a company update
post_url = 'https://api.linkedin.com/v2/shares'

# Company page ID
company_id = 'YOUR_COMPANY_ID'

# Construct the update text
update_text = latest_entry.title + '\n' + latest_entry.description + '\n' + latest_entry.link

# Customize the preview image and text
preview_image = 'URL_TO_CUSTOM_IMAGE'
preview_text = 'Custom preview text for the URL'

# Create the headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
}

# Create the JSON payload with custom content
payload = {
    'owner': f'urn:li:organization:{company_id}',
    'text': {
        'text': update_text
    },
    'content': {
        'contentEntities': [
            {
                'thumbnails': [{'url': preview_image}],
                'description': preview_text,
                'title': latest_entry.title,
                'content': latest_entry.description,
                'entityLocation': latest_entry.link
            }
        ],
        'title': latest_entry.title,
        'description': latest_entry.description
    }
}

# Make the API request
response = requests.post(post_url, headers=headers, json=payload)

# Check the response
if response.status_code == 201:
    print('Update posted successfully!')
else:
    print('Error posting update:', response.status_code, response.json())
