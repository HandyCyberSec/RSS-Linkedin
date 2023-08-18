# RSS-Linkedin

This Python script fetches content from an RSS feed, displays available fields for each entry, and posts a chosen entry to your LinkedIn company page. You can also customize the preview image and text for the URL in the LinkedIn post.

## Prerequisites

Before using this script, make sure you have:

1. A LinkedIn API Access Token: Obtain an access token from LinkedIn's Developer Console.

2. Company Page ID: Identify the ID of the LinkedIn company page where you want to post updates.

3. RSS Feed URL: Provide the URL of the RSS feed containing the content you want to post.

## Usage

1. Clone the repository or download the script `post_linkedin_update.py`.

2. Open the script in a text editor and replace the placeholders with your actual credentials:

   ```python
   rss_feed_url = 'URL_TO_YOUR_RSS_FEED'
   access_token = 'YOUR_ACCESS_TOKEN'
   company_id = 'YOUR_COMPANY_ID'
   ```

3. Customize the preview image and text:

   ```python
   preview_image = 'URL_TO_CUSTOM_IMAGE'
   preview_text = 'Custom preview text for the URL'
   ```

4. Run the script in your terminal:

   ```sh
   python post_linkedin_update.py
   ```

5. The script will display available fields for each entry from the RSS feed. Choose an entry number to post on LinkedIn.

## Automating Updates

To automate the process of posting company updates using this script, you can set up a scheduled task (cron job) on your server or local machine. This will ensure that the script runs at specified intervals to fetch the latest content from the RSS feed and post it to LinkedIn.

Here's how you can set up automation using a cron job:

1. Open your terminal or command prompt.

2. Type `crontab -e` and press Enter to open the crontab configuration.

3. Add a new line to schedule the script to run at your desired intervals. For example, to run the script every day at 9:00 AM, add the following line:

   ```sh
   0 9 * * * /usr/bin/python /path/to/post_linkedin_update.py
   ```

   Make sure to replace `/usr/bin/python` with the correct path to your Python interpreter, and `/path/to/post_linkedin_update.py` with the actual path to your script.

4. Save the crontab configuration and exit the editor.

Now, the script will automatically run at the specified intervals and post updates to your LinkedIn company page.

### Note

- Be cautious with automation and make sure you choose appropriate intervals to avoid excessive posting.
- Always test the automation setup to ensure it's working as expected before relying on it for important updates.

## Customization and Advanced Usage

- You can further customize the script to suit your needs. For example, you can add additional fields from the RSS feed to the LinkedIn post or include more complex formatting.

- If you want to explore more advanced automation options, you can use tools like Task Scheduler (Windows), cron jobs (Linux/macOS), or cloud-based services to schedule and trigger the script.

- Review LinkedIn's API documentation for any additional features or customization options you might want to incorporate.

## Troubleshooting

If you encounter issues while using the script or setting up automation, here are some steps to consider:

1. Double-check your LinkedIn API credentials, including the access token and company page ID.

2. Ensure that the RSS feed URL is correct and that the feed is properly formatted.

3. Test the script manually to confirm that it's working as expected before setting up automation.

4. Check the console or terminal for error messages and refer to the LinkedIn API documentation for troubleshooting guidance.

## License

This project is licensed under the [MIT License](LICENSE).
