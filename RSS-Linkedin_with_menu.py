import requests
import feedparser
import time
import threading

def main():
    rss_feed_urls = []
    while True:
        print_menu()
        option = input("Select an option: ")

        if option == '1':
            add_rss_feed(rss_feed_urls)
        elif option == '2':
            display_added_feeds(rss_feed_urls)
        elif option == '3':
            break
        else:
            print("Invalid option. Please choose a valid option.")

    access_token = input("Enter your LinkedIn API Access Token: ")
    company_id = input("Enter your LinkedIn Company Page ID: ")
    preview_image = input("Enter URL for the custom preview image: ")
    preview_text = input("Enter custom preview text: ")

    schedule_option = input("Select schedule option:\n1. Every 5 minutes\n2. Every 10 minutes\n3. Every 30 minutes\n4. Every hour\n5. Every 2 hours\nEnter option (1/2/3/4/5): ")

    schedule_mapping = {
        '1': 300,
        '2': 600,
        '3': 1800,
        '4': 3600,
        '5': 7200
    }

    interval_seconds = schedule_mapping.get(schedule_option, 300)

    print(f"Script will run every {interval_seconds} seconds.")

    start_scheduled_updates(rss_feed_urls, access_token, company_id, preview_image, preview_text, interval_seconds)

def print_menu():
    print("\nOptions:")
    print("1. Add RSS feed")
    print("2. Display added RSS feeds")
    print("3. Continue to LinkedIn setup and scheduling")

def add_rss_feed(rss_feed_urls):
    rss_feed = input("Enter RSS feed URL (or type 'done' to finish): ")
    if rss_feed.lower() != 'done':
        rss_feed_urls.append(rss_feed)

def display_added_feeds(rss_feed_urls):
    if rss_feed_urls:
        print("\nAdded RSS feeds:")
        for index, rss_feed in enumerate(rss_feed_urls, start=1):
            print(f"{index}. {rss_feed}")
    else:
        print("No RSS feeds added yet.")

def start_scheduled_updates(rss_feed_urls, access_token, company_id, preview_image, preview_text, interval_seconds):
    def run_updates():
        while True:
            post_updates(rss_feed_urls, access_token, company_id, preview_image, preview_text)
            time.sleep(interval_seconds)

    threading.Thread(target=run_updates).start()

def post_updates(rss_feed_urls, access_token, company_id, preview_image, preview_text):
    post_url = 'https://api.linkedin.com/v2/shares'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }

    for rss_feed_url in rss_feed_urls:
        feed = feedparser.parse(rss_feed_url)

        if not feed.entries:
            print(f'No entries found in the RSS feed: {rss_feed_url}')
            continue

        latest_entry = feed.entries[0]
        print('Title:', latest_entry.title)
        print('Description:', latest_entry.description)
        print('Link:', latest_entry.link)
        print()

        update_text = latest_entry.title + '\n' + latest_entry.description + '\n' + latest_entry.link

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

        response = requests.post(post_url, headers=headers, json=payload)

        if response.status_code == 201:
            print('Update posted successfully!')
        else:
            print('Error posting update:', response.status_code, response.json())

if __name__ == "__main__":
    main()
