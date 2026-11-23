
# Download the Northwind SQL script and create the database

import urllib.request
from html.parser import HTMLParser
import sqlite3

# Website containing the Northwind SQL script
url = "https://en.wikiversity.org/wiki/Applied_Programming/Databases/Northwind_SQL"


# Extract SQL code from the webpage
class SQLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside_pre = False
        self.sql_parts = []
        self.current_part = []

    # Detect the beginning of a code block
    def handle_starttag(self, tag, attrs):
        if tag == "pre":
            self.inside_pre = True
            self.current_part = []

    # Detect the end of a code block
    def handle_endtag(self, tag):
        if tag == "pre" and self.inside_pre:
            self.sql_parts.append("".join(self.current_part))
            self.inside_pre = False

    # Collect text inside code blocks
    def handle_data(self, data):
        if self.inside_pre:
            self.current_part.append(data)


# Download the webpage using a browser-style request
def download_sql_page():
    print("Downloading Northwind SQL script...")

    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "Accept": "text/html"
        }
    )

    with urllib.request.urlopen(request, timeout=30) as response:
        webpage = response.read().decode("utf-8")

    return webpage


# Extract SQL from the webpage
def extract_sql(webpage):
    parser = SQLParser()
    parser.feed(webpage)

    sql_script = "\n".join(parser.sql_parts)
    return sql_script


# Save SQL script to a file
def save_sql_file(sql_script):
    with open("northwind.sql", "w", encoding="utf-8") as file:
        file.write(sql_script)

    print("SQL script saved as northwind.sql")


# Create the Northwind SQLite database
def create_database(sql_script):
    connection = sqlite3.connect("northwind.db")

    try:
        connection.executescript(sql_script)
        connection.commit()
        print("Northwind database created successfully!")
        print("Database saved as northwind.db")

    except sqlite3.Error as error:
        print("Database error:", error)

    finally:
        connection.close()


# Main program
def main():
    try:
        webpage = download_sql_page()
        sql_script = extract_sql(webpage)

        # Make sure SQL was successfully extracted
        if not sql_script.strip():
            print("No SQL script was found on the webpage.")
            return

        # Save the SQL and create the database
        save_sql_file(sql_script)
        create_database(sql_script)

    except urllib.error.HTTPError as error:
        print("Website download error:", error.code)
        print("The website blocked the download request.")

    except urllib.error.URLError as error:
        print("Connection error:", error.reason)

    except Exception as error:
        print("An unexpected error occurred:", error)


# Run the program
if __name__ == "__main__":
    main()
