# CSS styles for the title and body text
title_style = "font-size: 36px; font-weight: bold; color: #4CAF50;"  # Customize this as needed
body_style = "font-size: 18px; color: #333; line-height: 1.6;"  # Customize this as needed
# CSS styles for the categories, time, and text
category_style = "font-weight: bold; color: #FF5722; font-size: 20px;"  # Bold category
time_style = "color: #9E9E9E; font-size: 14px;"  # Time in grey
text_style = "color: #333; font-size: 16px;"  # Body text

def get_feed_styles():
    return category_style, time_style, text_style

def get_pad_styles():
    return title_style, body_style