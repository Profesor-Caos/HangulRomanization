### Project Goal
The goal of this project is to get a bit of practice with machine learning. I plan to get a bunch of data on Korean words and their romanizations from wiktionary and use that to create a model that can romanize a hangul word.

### Data Acquisition
Downloaded enwiktionary-late-page.sql.gz from https://dumps.wikimedia.org/enwiktionary/latest/ containing every page on the English wiktionary
Ran it to create a MySQL database table of pages.
Unfortunately, this doesn't have page content, so I found another file, https://dumps.wikimedia.org/enwiktionary/latest/enwiktionary-latest-pages-articles.xml.bz2 that has article text in it and is quite massive, almost 9 GB when unzipped.
I decided since this is nested xml, I'll use python to load it into the database instead of MySQL's load xml.
Using Python, I can also only include the pages with Hangul characters in the titles and exclude the majority of the data.

