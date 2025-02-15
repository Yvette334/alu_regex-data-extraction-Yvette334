import re

# Regular expressions for each type of data
reg_patt = {
    "email_addresses": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "urls": r"https?://(?:www\.)?[a-zA-Z0-9.-]+(?:\.[a-zA-Z]+)+[/\w\-%=&.?]*",
    "phone_numbers": r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b",
    "credit_card_numbers": r"(?:\d{4}[-\s]?){3}\d{4}",
    "time_formats": r"\b(?:[01]?[0-9]|2[0-3]):[0-5][0-9](?:\s?[APMapm]{2})?\b",
    "html_tags": r"<[^>]+>",
    "hashtags": r"#[A-Za-z0-9_]+",
    "currency_amounts": r"\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?"
}

# Function to extract data based on regex patterns
def extract_info(input_text, patterns):
    extracted_info = {}
    for data_type, pattern in patterns.items():
        extracted_info[data_type] = re.findall(pattern, input_text)
    return extracted_info

txt = """
    Email addresses:
    - user@example.com
    firstname.lastname@company.co.uk
    URLs:
    https://www.example.com
    https://subdomain.example.org/page
    Phone numbers (various formats):
    (123) 456-7890
    123-456-7890
    123.456.7890
    Credit card numbers:
    1234 5678 9012 3456
    1234-5678-9012-3456
    Time:
    14:30 (24-hour format)
    2:30 PM (12-hour format)
    HTML tags:
    <p>
    <div class="example">
    <img src="image.jpg" alt="description">
    Hashtags:
    #example
    #ThisIsAHashtag
    Currency amounts:
    $19.99
    $1,234.56
"""

# Extract data from the sample text
extracted_info = extract_info(txt, reg_patt)

# Display data using the format
output = ""

for data_type, matches in extracted_info.items():
    output += "{}:\n".format(data_type.replace('_', ' ').capitalize())
    if matches:
        for match in matches:
            output += "- {}\n".format(match)

    else:
        output += "None\n"

# Print output
print(output)
