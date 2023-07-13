from webbrowser import get,Error

with open('websites.txt', 'r') as file:
    websites = [line.strip() for line in file]


try:
    browser = get()
    for site in websites:
        try:
            browser.open(site)
        except Error as e:
            # If there is an invalid URL, it will create an error file.
            error_message = f"An error occurred while opening {site}"
            with open('error_log.txt', 'w') as error_file:
                error_file.write(error_message + "\n")
except Error as e:
    error_message = "An error occurred while opening your websites."
    with open('error_log.txt', 'a') as error_file:
        error_file.write(error_message + '\n')