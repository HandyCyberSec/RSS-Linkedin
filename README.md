# RSS-Linkedin

This Python script allows you to fetch content from multiple RSS feeds, display the latest entries, and post them as company updates on LinkedIn using the LinkedIn API. You can also customize the preview image and text for the URLs in the LinkedIn posts.

## Prerequisites

Before using this script, make sure you have:

1. A LinkedIn API Access Token: Obtain an access token from LinkedIn's Developer Console.

2. Company Page ID: Identify the ID of the LinkedIn company page where you want to post updates.

3. RSS Feed URLs: Provide the URLs of the RSS feeds containing the content you want to post.

## Usage

1. Clone the repository or download the script `post_linkedin_update.py`.

2. Open the script in a text editor and replace the placeholders with your actual credentials:

   ```python
   rss_feed_urls = [
       'URL_TO_RSS_FEED_1',
       'URL_TO_RSS_FEED_2',
       # Add more URLs as needed
   ]
   access_token = 'YOUR_ACCESS_TOKEN'
   company_id = 'YOUR_COMPANY_ID'
   preview_image = 'URL_TO_CUSTOM_IMAGE'
   preview_text = 'Custom preview text for the URL'
   ```

3. Run the script in your terminal:

   ```sh
   python post_linkedin_update.py
   ```

4. The script will iterate through each RSS feed, display the latest entry, and post it to your LinkedIn company page.

## Automating Updates

To automate the process of posting company updates using this script, you can set up a scheduled task (cron job) on your server or local machine. This will ensure that the script runs at specified intervals to fetch the latest content from the RSS feeds and post them to LinkedIn.

Here's how you can set up automation using a cron job:

1. Open your terminal or command prompt.

2. Type `crontab -e` and press Enter to open the crontab configuration.

3. Add a new line to schedule the script to run at your desired intervals. For example, to run the script every day at 9:00 AM, add the following line:

   ```sh
   0 9 * * * /usr/bin/python /path/to/post_linkedin_update.py
   ```

   Make sure to replace `/usr/bin/python` with the correct path to your Python interpreter, and `/path/to/post_linkedin_update.py` with the actual path to your script.

4. Save the crontab configuration and exit the editor.

Now, the script will automatically run at the specified intervals and post updates from the configured RSS feeds to your LinkedIn company page.

### Note

- Be cautious with automation and make sure you choose appropriate intervals to avoid excessive posting.
- You can configure the crontab schedule to match your preferred update frequency.
- Always test the automation setup to ensure it's working as expected before relying on it for important updates.

## Customization and Advanced Automation

- If you have additional requirements for automation, you can explore more advanced options such as Task Scheduler (Windows), cron jobs (Linux/macOS), or cloud-based services to schedule and trigger the script.

- Consider enhancing the script to handle error scenarios gracefully, such as network failures or invalid RSS feeds.

- Review LinkedIn's API documentation for any additional features or customization options you might want to incorporate into the automated updates.

## Troubleshooting

If you encounter issues while setting up or running the automated updates, here are some steps to consider:

1. Verify that the crontab schedule is correctly configured and matches your desired update intervals.

2. Check the console or terminal for error messages and refer to the LinkedIn API documentation for troubleshooting guidance.

3. Test the automated setup in a controlled environment before relying on it for important updates.

## License

This project is licensed under the [MIT License](LICENSE).
