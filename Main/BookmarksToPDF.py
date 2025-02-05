from fpdf import FPDF
import hashlib
from PIL import Image
import os
from playwright.sync_api import sync_playwright
import requests

def fetch_bookmarks_to_pdf():
    # Create a directory to store images
    if not os.path.exists("bookmarks_images"):
        os.makedirs("bookmarks_images")

    # Initialize PDF
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    with sync_playwright() as p:
        # Launch browser (headless mode for simplicity)
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://twitter.com")
        input("Please log in to Twitter on the browser that opened, and then press ENTER in here to continue")  #pauses the program until user input to give them enough time to log in

        # Navigate to Twitter Bookmarks
        target = input("\nSelect destination to download. \nPress 1 for bookmarks, \nor enter a Twitter profile or likes URL (any non-Twitter link will not work)\n\nTarget:  ").strip()
        if target == 1:
            page.goto("https://twitter.com/i/bookmarks")
        else:
            page.goto(target)

        # Initialize a set to store tweet content hashes (to avoid duplicates)
        saved_tweet_hashes = set()

        while True:
            previous_height = page.evaluate("document.body.scrollHeight")
            page.evaluate("window.scrollBy(0, window.innerHeight)")             #these two are used to catch the end
            # Scroll down by a small step
            page.evaluate("window.scrollBy(0, 500)")  # Finaly number (default 500) changes the amount of
                                                      # pixels scrolled, increase number to increase speed
            page.wait_for_timeout(2000)  # Wait for new content to load in miliseconds, decrease number to increase
                                         # speed. Please note that this is to factor in loading times and lowering it
                                         # too much could lead to premature termination of the program

            # Extract tweets after scrolling
            tweets = page.query_selector_all("article")
            print(f"Found {len(tweets)} tweets.")  # Debugging print statement

            for i, tweet in enumerate(tweets):
                # Extract tweet text
                tweet_text = tweet.inner_text()

                # Create a hash of the tweet text to ensure uniqueness
                tweet_hash = hashlib.md5(tweet_text.encode('utf-8')).hexdigest()

                # Check if the tweet's hash is already in the set (to avoid duplicates)
                if tweet_hash not in saved_tweet_hashes:
                    print(f"Processing tweet with hash {tweet_hash}")  # Debugging print statement
                    saved_tweet_hashes.add(tweet_hash)  # Mark this tweet as saved
                    pdf.add_page()

                    # Add tweet text to the PDF
                    pdf.set_font("Arial", size=12)
                    pdf.multi_cell(0, 10, tweet_text.encode('latin-1', 'ignore').decode('latin-1'))
                    pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
                    pdf.set_font("DejaVu", size=12)

                    # Extract images in the tweet
                    images = tweet.query_selector_all("img")
                    for img_index, img in enumerate(images):
                        img_url = img.get_attribute("src")
                        if img_url:
                            # Modify the URL to fetch a higher resolution
                            if ":small" in img_url or ":medium" in img_url or ":large" in img_url:
                                img_url = img_url.replace(":small", ":large").replace(":medium", ":large")

                            try:
                                response = requests.get(img_url)
                                image_path = f"bookmarks_images/tweet_{i + 1}_img_{img_index + 1}_{tweet_hash}.jpg"    #tweet_hash ensures images are uniquely saved and don't overwrite each other
                                with open(image_path, "wb") as file:
                                    file.write(response.content)

                                # Add image to PDF
                                if os.path.exists(image_path):
                                    pdf.image(image_path, x=(210 - 180) / 2, y=None,
                                              w=180)  # Center the image, scale width to 180
                                    pdf.ln(1)  # Add some space after the image
                            except Exception as e:
                                print(f"Failed to download image {img_url}: {e}")

                    # Extract videos in the tweet (thumbnails only)
                    videos = tweet.query_selector_all("video")
                    for vid_index, video in enumerate(videos):
                        poster_url = video.get_attribute("poster")  # Thumbnail image
                        if poster_url:
                            try:
                                response = requests.get(poster_url)
                                video_thumb_path = f"bookmarks_images/tweet_{i + 1}_vid_{vid_index + 1}_{tweet_hash}.jpg"
                                with open(video_thumb_path, "wb") as file:
                                    file.write(response.content)

                                # Add video thumbnail to PDF
                                pdf.image(video_thumb_path, x=10, y=None, w=180)
                            except Exception as e:
                                print(f"Failed to download video thumbnail {poster_url}: {e}")
                else:
                    print(f"Skipping duplicate tweet with hash {tweet_hash}")  # Debugging print statement

            # Get the new page height after scrolling
            new_height = page.evaluate("document.body.scrollHeight")

            # Get the new visible tweet count
            new_visible_tweets_count = len(page.query_selector_all("article"))

            # Check if the page height is still the same (no more content to load)
            if new_height == previous_height and new_visible_tweets_count == visible_tweets_count:
                scroll_attempts += 1  # Increment scroll attempt count
            else:
                previous_height = new_height  # Update the previous height if new content is loaded
                visible_tweets_count = new_visible_tweets_count  # Update the visible tweet count
                scroll_attempts = 0  # Reset the scroll attempt counter

            # Stop scrolling if no new tweets have been found and no height change after multiple attempts
            if scroll_attempts > 3:
                print("No new content found, stopping scrolling.")
                break

            # # Scroll by a small step (100px) to load more content
            # page.evaluate(f"window.scrollBy(0, 1000)")
            # page.wait_for_timeout(scroll_pause_time)  # Wait for the new content to load

        # Close the browser
        browser.close()

    # Save the PDF
    pdf.output("Twitter_Bookmarks.pdf")

    # Cleanup images directory if needed
    print("PDF created: Twitter_Bookmarks.pdf")

fetch_bookmarks_to_pdf()
