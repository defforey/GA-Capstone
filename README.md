# <img width="40" src="/Resources/book_stack.jpeg"> Using text reviews to guide book marketing strategies 
## Capstone Project for DSI at General Assembly

This repository contains notebooks and associated files for my capstone project completed during the Data Science Immersive course at General Assembly (London, UK).

### Project Goals
Book ratings give an incomplete picture of what consumers think of books, which can make it difficult to improve marketing strategies for publishers or retailers. The main goal of this project is to identify common topics in text reviews of books using topic modelling, and to determine whether developing distinct marketing strategies to promote books based on their genre would be an effective strategy to pursue. A secondary goal of the project is to train and test a topic model capable of predicting the main topics of text reviews.

The findings of this project may have interesting business outcomes for publishers and retailers as they could enable more effective marketing strategies for different books should distinct topics be identified across book genres. For example, fantasy readers may care more about character personalities than sci-fi readers and thus marketing materials for fantasy books could be adjusted accordingly. Conversely, if book genres are not identified in review topics, this could indicate that investing resources in creating promotion materials for distinct book genres is an unnecessary expense. 

### Repository Contents
Notebooks can be viewed on nbviewer using the links provided below. I recommend using these links since most markdown cells contain html tags and will not be rendered properly when viewing the notebooks on GitHub.

[Notebook 00: Project Overview](https://nbviewer.jupyter.org/github/defforey/GA-Capstone/blob/master/00.%20Project%20overview.ipynb)
This notebook contains an overview of the project, including its goals, the datasets used, the overall approach, the project's findings and their limitations.

[Notebook 01: Importing the LibraryThing dataset](https://nbviewer.jupyter.org/github/defforey/GA-Capstone/blob/master/01.%20Importing%20the%20LibraryThing%20dataset.ipynb)
This notebook focuses on loading the dataset downloaded from Prof. McAuley's <a href="https://cseweb.ucsd.edu/~jmcauley/datasets.html#social_data" target="_blank">website</a> and selecting a sample of 5000 books to be used for the rest of the project.

[Notebook 02: Scraping Librarything.com](https://nbviewer.jupyter.org/github/defforey/GA-Capstone/blob/master/02.%20Scraping%20Librarything.com.ipynb)
The purpose of this notebook is to scrape the LibraryThing website for additional information on books that was not included in the first dataset (e.g. book titles, author names, ISBNs).

[Notebook 03: Goodreads API](https://nbviewer.jupyter.org/github/defforey/GA-Capstone/blob/master/03.%20Goodreads%20API.ipynb)
In this notebook, I use the ISBNs collected from the LibraryThing website to collect book genre information from Goodreads, which provides more comprehensive and quantitative genre information than LibraryThing. This notebook uses both the BetterReads package (a Python interface for the Goodreads API) and the Goodreads API directly via get requests.

[Notebook 04: Data Cleaning and EDA](https://nbviewer.jupyter.org/github/defforey/GA-Capstone/blob/master/04.%20Data%20cleaning%20and%20EDA.ipynb)
This notebook combines the datasets from the three previous notebooks into one, cleans the data and contains preliminary visualisations.

[Notebook 05: Modelling and Analysis](https://nbviewer.jupyter.org/github/defforey/GA-Capstone/blob/master/05.%20Modelling%20and%20analysis.ipynb)
The final notebook tests the performance of 10 different LDA models to extract topics from processed book reviews, then uses the best performing model to make topic predictions. It also includes sentiment analysis (polarity). An overall summary of the findings is included at the beginning of the notebook.

<a href="Book reviews data dictionary">Data Dictionary</a>
A document providing additional information on the characteristics of the final dataset, as well as the data sources used for this project.

<a href="Resources/Project Presentation Slides.pdf">Final Presentation Slides</a>
Final presentation of the project, involving its overall goal, the approach used, key findings, limitations and future work.
