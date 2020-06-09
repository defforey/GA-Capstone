# <img width="40" src="/resources/book_stack.jpeg"> Using text reviews to guide book marketing strategies 
## Capstone Project for DSI at General Assembly

This repository contains notebooks and associated files for my capstone project completed during the Data Science Immersive course at General Assembly (London, UK). It has since been updated to improve readability.

### Project Goals
Book ratings give an incomplete picture of what consumers think of books, which can make it difficult to improve marketing strategies for publishers or retailers. The main goal of this project is to identify common topics in text reviews of books using topic modelling (LDA), and to determine whether developing distinct marketing strategies to promote books based on their genre would be an effective strategy to pursue. A secondary goal of the project is to train and test a topic model capable of predicting the main topics of text reviews.

The findings of this project may have interesting business outcomes for publishers and retailers as they could enable more effective marketing strategies for different books should distinct topics be identified across book genres. For example, fantasy readers may care more about character personalities than sci-fi readers and thus marketing materials for fantasy books could be adjusted accordingly. Conversely, if book genres are not identified in review topics, this could indicate that investing resources in creating promotion materials for distinct book genres is an unnecessary expense. 

### Datasets
This project combines data from three sources:<br>(1) a dataset of scraped information from the librarything.com website that was collected by Prof. Julian McAuley (University of California, San Diego) and colleagues<sup>1, 2</sup>. This dataset can be downloaded on Prof. McAuley's <a href="https://cseweb.ucsd.edu/~jmcauley/datasets.html#social_data" target="_blank">website</a>.<br>(2) additional information (book titles, authors, ISBNs) I scraped from the <a href="https://www.librarything.com/" target="_blank">LibraryThing website</a>.<br>(3) book genre information I collected using the <a href="https://www.goodreads.com/api/index" target="_blank">Goodreads API</a>.

### Key Findings and their Limitations
#### <a href="https://htmlpreview.github.io/?https://github.com/defforey/GA-Capstone/blob/master/resources/lda_model5.html" target="_blank">Link to interactive LDA topic visualisation</a>
Using bigrams, 20 topics and 10 corpus passes yielded the best model out of the 10 models tested. This model produced topics that were interpretable, with some overlap but overall low perplexity and acceptable topic coherence. It can now be used to predict topics in book reviews.<br><br>
     The key findings of this modelling exercise are that some themes common to specific book genres do come across as topics in the topic model, for example magic, love and courtship, story plots or adventure. This indicates that it may be worth developing distinct marketing strategies for fantasy, romance, thriller books in particular. Another finding is that target audiences also come up as topics, in particular children and young adult, indicating that books for this demographic range should be promoted in a way that targets this specific audience. An important potential limitation to bear in mind when interpreting these findings is that topics were manually labelled, and that there may be some bias imparted by the person labelling them.
     
### Future Work and Considerations for Real World Production Environment
<ul type="disk">
    <li>Manually label books with incorrect or missing ISBNs and add them to the dataset to increase the size of the corpus and improve model performance.</li>
    <li>Create a web interface (e.g. with Flask) where users can input reviews, then retrieve dominant topics.</li>
    </ul>

### Additional resources  
<a href="resources/book_reviews_data_dictionary.txt">Data Dictionary</a>
A document providing additional information on the characteristics of the final dataset, as well as the data sources used for this project.

<a href="resources/Project Presentation Slides.pdf">Final Presentation Slides</a>
Final presentation of the project, involving its overall goal, the approach used, key findings, limitations and future work.

### References
1. <b>SPMC: Socially-aware personalized Markov chains for sparse sequential recommendation</b><br>
Chenwei Cai, Ruining He, Julian McAuley<br>
<i>IJCAI</i>, 2017<br>

2.<b> Improving latent factor models via personalized feature projection for one-class recommendation</b><br>
Tong Zhao, Julian McAuley, Irwin King<br>
<i>Conference on Information and Knowledge Management (CIKM)</i>, 2015

3.<b> Latent Dirichlet Allocation</b><br>
David M. Blei, Andrew Y. Ng, Michael I. Jordan<br>
<i>Journal of Machine Learning Research</i> 3, 993-1022, 2003

4.<b> LDAvis: A method for visualizing and interpreting topics</b><br>
Carson Sievert, Kenneth E. Shirley<br>
<i>Proceedings of the Workshop on Interactive Language Learning, Visualization, and Interfaces</i>, 63-70, 2014 
