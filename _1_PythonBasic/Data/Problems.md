---
output:
  word_document: default
  html_document: default
---
# Data Acquisition and Manipulation with Python Problems
*Curtis Miller*

## Section 1 Problems

1. The files `titanic.csv`[^1], `titanic.xlsx`, and `titanic.json` contain data describing passengers of the Titanic disaster (including who survived). Use each of these files to create a Pandas `DataFrame`.

[^1]: This dataset originated from this website: http://web.stanford.edu/class/archive/cs/cs109/cs109.1166/problem12.html

2. An API for obtaining the latest exchange rates between currencies is provided at `http://api.fixer.io/latest`. The field `base` determines the base currency the exchange rate is quoted as, and the field `symbols` determines which currencies to get an exchange rate for. Using this API, get the latest exchange rates in terms of your local currency for the British pound sterling (GBP), the U.S. dollar (USD), the Japanese yen (JPY), and the euro (EUR). (If your local currency is among these, exclude it. If your local currency is not available, use USD. Hint: for the `symbols` parameter, you can request quotes for multiple symbols by separating them with a comma. See the documentation at [fixer.io](http://fixer.io/).)

3. Create a MySQL database for the first ten rows of the `titanic` dataset (see Problem 1 of this section) for every field except the name of the passengers.

4. After completing Problem 3 of this section, add the remaining rows of the `titanic` dataset to the same database.

5. Connect to the database created in Problem 4 of this section. Then create Pandas `DataFrame`s that:
a. Contain all the data in the database.
b. Contain the sex of all survivors.
c. Contains the passenger class and surival status of all men over the age of 30 who paid a fare greater than 10 pounds.

6. After completing Problem 2 of this section, create a database containing the symbol and exchange rate for every currency available through the API. Include a column containing the date the data was retrieved. (Hint: omitting the `symbols` parameter will retrieve all symbols available through the API.)

7. The API mentioned in Problem 2 of this section works if `latest` in the base URL is replaced with a date following the `YYYY-MM-DD` format. Use this to repeat Problem 6 from this section but with yesterday's exchange rates. Then add this data to the database created before.

8. After completing Problem 7 of this section, create Pandas tables with: all data in the database and data only for currencies with an exchange rate greater than 1 on the most recent day.

## Section 2 Problems

1. Load in the data contained in the files `mtc1.csv` and `mtc2.csv`. Join the rows of these datasets together. (This data was extracted from the 1974 *Motor Trend* magazine, and provided with every R installation. Hint: Car model should be an index; the table itself should contain only numeric data.)

2. The file `mortality.csv` contains mortality data for selected years of selected countries (the data is from the U.S. Census Bureau). Using the population pyramid data we have seen before, perform a right join that leads to a dataset that, for years common to both datasets, contains the male population, female population, male life expectancy, and female life expectancy.

3. Consider the dataset that results from completing Problem 1 of this section. This dataset is in wide-form format. Convert it to long-form format, where variable values are the values of a Pandas `Series`, and the key contains the make of the car and the variable that a value in the `Series` represents. (Hint: this will involve stacking.)

4. The file `crimes.csv` contains data for arrests per 100,000 in U.S. states for selected crimes. Convert this dataset from long-form to wide-form format, where state name is the index of the Pandas `DataFrame`, the contents of the `DataFrame` are the crime rates, and each crime has its own column. (This data is from the 1975 Statistical Abstracts of the United States, and included with every R installation.)

5. For the Titanic dataset contained in the file `titanic.csv`, create a Pandas `DataFrame` where the variable `Sex` takes the value `0` for males and `1` for females.

6. For the Titanic dataset considered in problem 5 of this section, standardize the values of the columns `Fare` and `Age`.

7. The file `ubuntuirclog20170901.txt` contains the transcript of an IRC chat session that took place on September 1st, 2017. Create a Pandas `DataFrame` from this log file, with a column for the time, a column for the author of the statement, and a column with the text of the statement. (Hint: the characters `[` and `]` would normally have a special meaning in a regular expression. If you want to refer to the *literal character* `[` or `]`, prepend with a `\`, so the regular expression `\[a\]` would match a substring in the string "We went to [a] movie." Also, beware that not all lines in the text files are user comments and don't all follow the same format. You may need to skip lines that don't actually contain a comment by a user.)

8. Take the `DataFrame` created in Problem 7 of this section and use it to create a text file where a user comment (contained in a row of the `DataFrame`) is written on its own line in a format similar to: "At 11:22, superuser0101 wrote 'Hello, world!'"

## Section 3 Problems

1. The file `mtcars.csv` contains data for different cars. Form three different grouping schemes, based on: the number of forward gears (the variable `gear`); the number of cylinders (`cyl`); and combinations of forward gears and cylinders. (This data was extracted from the 1974 *Motor Trend* magazine, and provided with every R installation. Hint: Car model should be an index; the table itself should contain only numeric data.)

2. After forming the groups in Problem 1 of this section, iterate through the groups formed and print out the dimensions of the corresponding `DataFrame`s, along with a numerical summary of each `DataFrame` (perhaps using the `describe()` method). Do this using a `for` loop.

3. After forming the groups in Problem 1 of this section, for each group in each grouping scheme created, get the following statistics: the size of the group; the mean of each column in the group; the standard deviation of each column in the group; the 5th percentile of each column; and the 95th percentile of each column.

4. After forming the groups in Problem 1 of this section, write functions that compute the range of a dataset (the largest value minus the smallest value) and the midrange of each dataset (the arithmetic mean of the largest and smallest value). Use the `agg()` or `aggregate()` methods to compute the range and midrange of each group in each grouping scheme. Do so in a "pretty" format (a table with the name of the statistic each column represents).

5. After forming the groups in Problem 1 of this section, create "standardized" versions of the variables `mpg` (miles per gallon), `disp` (displacement), `hp` (gross horsepower), `drat` (rear axle ratio), `wt` (weight), and `qsec` (quarter-mile time), using the mean and standard deviation of the respective groups to perform the standardization. Do this only for the grouping based on the number of cylinders.

6. The file `mtcars_censored.csv` is similar to the file `mtcars.csv` mentioned in Problem 1 of this section but the quarter-mile time (`qsec`) value for some cars was censored. First, fill in the missing data using the mean `qsec` value involving the entire dataset. Then fill in using the mean `qsec` value of the group (stratified based on `cyl` and `gear`) that the car belongs to. Compare the result of these two data imputation schemes to the actual `qsec` value of the car (available in `mtcars.csv`). Which approach seens to produce the "better guesses"?

7. The following table contains the sex and grades of students in a classroom:

Student  | Sex | Grade
---------|-----|-------
Sam      |  M  |   A
Susan    |  F  |   A
Beth     |  F  |   A
Courtney |  F  |   B
Abigail  |  F  |   A
Daniel   |  M  |   C
Evan     |  M  |   C
Falicia  |  F  |   B
Greg     |  M  |   B
Hank     |  M  |   A
Ivan     |  M  |   B
Jacob    |  M  |   C
Ken      |  M  |   D
Lisa     |  F  |   F
Mary     |  F  |   A
Nick     |  M  |   A

Perform cross-tabulation. Do the sexes appear to get the same grades with the same frequency?

8. Using the data set from Problem 7 of this section, use a pivot table to see the proportion of students falling into different combinations of sex and grade.

## Section 4 Problems

1. The website [quotes.toscrape.com](http://quotes.toscrape.com/) is a website containing quotes from notable persons. (This website is intended for people learning web scraping.) Inspect the DOM of this site using a Web browser such as Chrome or Firefox. Can you find an element in the DOM that links to the page on Albert Einstein?

2. Some quotes on [quotes.toscrape.com](http://quotes.toscrape.com/) are categorized with tags; for example, one quote by Einstein is tagged, "change". Describe the DOM element corresponding to tags. What `div` contains a quote? What is the `class` of a tag? How could this be used when scraping the web?

3. Choose two websites and view their `robots.txt` file, if it exists (often it is located in the directory right below the domain name, like `http://www.example.com/robots.txt`). What pages are allowed and disallowed for web crawlers? What other useful information is in the file?

4. Visit [robotstxt.org](http://www.robotstxt.org/). While there, read about the <META> tag. What is the tag for? How might it be used by a webpage that does not want to be scraped?

5. Go to [whatismybrowser.com](https://www.whatismybrowser.com/) and discover the header information your browser is sending out. Create a `dict` that, when passed to an argument for the `get()` method of a `Session()` object from **requests**, will lead to that header being used by the method when making a `GET` request to a server.

6. Get the page `http://quotes.toscrape.com` via functionality provided in the **requests** module in Python. Be sure to use the header information contained in the `dict` you created in Problem 5 of this section.

7. Create a `BeautifulSoup` object of the page obtained in Problem 6 of this section. With this object, get the title of the page (that is, the text "Quotes to Scrape").

8. Using the `BeautifulSoup` object created in Problem 7 of this section, get links to all author pages on the website [quotes.toscrape.com](http://quotes.toscrape.com). (Notice that links on this page are relative links.) Put these links in a `list` or `dict`. (You only need to do this for the first page of the website.)

9. Using the object created in Problem 8 of this section, visit every author page on the website [quotes.toscrape.com](http://quotes.toscrape.com), and get their birthdays. Store them in a `DataFrame`. (Note that you may need to parse the dates using **datetime**, given their format.)

10. Quotes on [quotes.toscrape.com](http://quotes.toscrape.com) often are categorized with tags. On the first page, create a `dict` for each quote using the `BeautifulSoup` object created in Problem 7 of this section that includes every tag associated with that quote and the destination of the tag's link.

11. Using the `dict`s created in Problem 10, for every quote on the first page of [quotes.toscrape.com](http://quotes.toscrape.com), create a `set` of "similar quotes" found by following links to the quotes' tags' pages, which contain quotes considered "similar".

## Section 5

1. After downloading and installing Selenium for Python, download the driver for the browser you wish to use and start the driver in Python.

2. Visit [quotes.toscrape.com](http://quotes.toscrape.com) using the driver instance created in Problem 1 of this section.

3. Using the driver instance created in Problem 2 of this section, visit the first three pagees of [quotes.toscrape.com](http://quotes.toscrape.com), then go back to the first page. Do this by "clicking" the buttons "Next" and "Previous".

4. Create a `set` of links to author pages using the driver instance created in Problem 2 of this section, "clicking" through the first three pages of the website to get a more complete list.

5. Using the driver instance created in Problem 2 of this section, click the link "Login" at the top of the main page of [quotes.toscrape.com](http://quotes.toscrape.com). Wait until the textbox for entering a username and password appear. "Type" the username "guest" and the password "guest" (for this website, it does not matter what you enter). Then "click" the "Login" button.

6. After completing Problem 5 of this section, parse the first page of quotes by feeding the page's source to `BeautifulSoup`. Using the resulting `BeautifulSoup` object, get all links to the website [Goodreads](https://www.goodreads.com/).

## Section 6

1. Use the Scrapy shell to develop code that locates the text for any quote on a page of [quotes.toscrape.com](http://quotes.toscrape.com).

2. Use the Scrapy shell to develop code that can find a link to the next page when on a page of [quotes.toscrape.com](http://quotes.toscrape.com).

3. Create a new Scrapy project for scraping [quotes.toscrape.com](http://quotes.toscrape.com).

4. For the project created in Problem 3 of this section, create a Scrapy spider called "quotes".

5. For the Scrapy spider "quotes" created in Problem 4 of this section, program the spider to collect the text of all quotes on a given page of [quotes.toscrape.com](http://quotes.toscrape.com).

6. Modify the spider created in Problem 5 of this section so that it tries to detect the "Next" button of the page and follow the link to the next page if it exists.

7. Deploy the spider created in Problem 6 of this section, creating a `JSON` file "quotes.json" containing the quotes found by the spider.

8. Repeat Problems 1-7 of this section, but build a collection of author names and links to their pages instead (you don't need to actually follow the links, just collect them).
