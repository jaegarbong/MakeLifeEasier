## README
This script is used to scrape the job postings from the following URL: <br>
https://www.analyticsinsight.net/top-10-data-science-jobs-to-apply-for-this-week/
<br>

Using BeautifulSoup, the script gathers the relevant text from the website and processes it into csv format.
It saves the csv file in the current working directory.

### External Libraries:
These libraries are necessary to run this script on a local IDE.
1. requests
2. Pandas
3. BeautifulSoup (bs4)

### Next Steps:
1. I am planning to write another function where I can upload this on Google Drive for public consumption. 
2. Since this involved creation and consumption of Google API, this will take some time to implement.
3. I am also working on converting this to an executable that can be consumed without the necessity of a python system