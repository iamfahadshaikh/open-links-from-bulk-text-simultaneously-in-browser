# PYTHON CODE TO EXTRACT LINKS AND OPEN IN BROWSER.

import re
import webbrowser

def extract_links(text):
    # Regular expression to find URLs in the text
    url_pattern = re.compile(r'https?://\S+')
    return url_pattern.findall(text)

def open_links_in_browser(links):
    for link in links:
        webbrowser.open_new_tab(link)

def main():
    print("Enter text (press Enter twice to finish input):")
    
    # Keep taking input until an empty line is entered
    user_input = ""
    while True:
        line = input()
        if not line:
            break
        user_input += line + "\n"
    
    # Extract links from the user input
    links = extract_links(user_input)
    
    if links:
        print("\nOpening links in the default browser:")
        open_links_in_browser(links)
    else:
        print("No links found in the input.")

if __name__ == "__main__":
    main()
