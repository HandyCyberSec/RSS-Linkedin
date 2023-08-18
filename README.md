# RSS-Linkedin with Menu

This Python script allows you to automatically post updates to your LinkedIn company page using data from RSS feeds. You can customize the preview image, text, and schedule for posting updates.

For the use of the script without menu go to [README Script](https://github.com/HandyCyberSec/RSS-Linkedin/blob/main/README-script.md)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- LinkedIn API Access Token.
- LinkedIn Company Page ID.
- URLs of the RSS feeds you want to use.

## Installation

1. Clone the repository to your local machine:

   ```sh
   git clone https://github.com/your-username/linkedin-auto-post.git
   cd linkedin-auto-post
   ```

2. Install the required dependencies using pip:

   ```sh
   pip install requests feedparser
   ```

## Usage

1. Run the script by executing the following command:

   ```sh
   python post_linkedin_update.py
   ```

2. Follow the on-screen instructions to add RSS feed URLs, provide LinkedIn API credentials, customize the preview image and text, and select a posting schedule.

3. The script will automatically fetch and post updates from the specified RSS feeds at the chosen interval.

## Options

- `Add RSS feed`: Enter the URL of an RSS feed to add it to the list of feeds.
- `Display added RSS feeds`: View the list of currently added RSS feeds.
- `Continue to LinkedIn setup and scheduling`: Proceed to enter LinkedIn API credentials, customize preview details, and choose the posting schedule.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Note:** This script is provided as-is and may require adjustments based on your specific requirements. Use it responsibly and ensure you comply with LinkedIn's API usage policies.

For more information, refer to the [LinkedIn API documentation](https://docs.microsoft.com/en-us/linkedin/marketing/).

Created by [Your Name](https://github.com/HandyCyberSec)
