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

## Important Notes

- This script is provided as-is and may require further customization based on your needs.
- Be cautious when handling and storing your LinkedIn API credentials.
- Always adhere to LinkedIn's API usage policies and guidelines.
- Use responsibly and respect the terms of service of both LinkedIn and the RSS feed source.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README based on your specific use case, any additional features you've added, and any troubleshooting tips you might have. Include any dependencies, installation instructions, and other relevant information you think would be helpful for users of the script.
