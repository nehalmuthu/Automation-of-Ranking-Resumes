# Automation-of-Ranking-Resumes

## Problem Statement
 - Many institutions and companies use resumes as a way of short-listing candidates in preliminary rounds. 
 - Going through every resume and short-listing is an arduous process and in many instances, it is prone to human errors.  
 - This project aims to automate this short-listing process by retrieval of relevant resumes to a given job description(JD).

## Dataset 
- Resumes and Job descriptions are collected from indeed.com and linkedIn. 
- Also job reviews are scraped from ambitionbox.com. Also data related to the selected candidates  are available which is used for further analysis

## Tools
- Django framework is used to build the user interface.
- BeautifulSoup in python is used for scrapping documents from websites.
- NLTk and Spacy libraries are use to process documents.
- PDFMiner.six is used to convert pdf to text.

## Implementation Details:
The project is developed in 3 phases.

### Phase 1
- Data collected from resumes and job sections of Naukri.com and linkedIn.
- Data Cleaning
- Dictionary and Posting list are created.
- Then each resume is vectorized.
- Building search engine.
- Query  is Job description given by the company
- Similarity score is computed between job description and resumes.
- Finally, search engine will rank and display the suitable candidates.
- Scope for improvement: incorporating NLP techniques like NER into the above model and improving on ranking methods.


### Phase 2 

- **Vectorizing:** 
    - With the help of indexing we build document vectors  using tf-idf approach(both tf and idf normalized). 
    - We get a 570*3500 dimenstional matrix where 570 is the no of documents and 3500 is the dimension of each vector. 

- **Querying:** 
    - Here query is of two types. We can either query documents based on keywords(eg: skillset,college,etc) or based on job description document. 
    - For the latter approach we have to upload JD do all the pre-processing (as in phase1) and then vectorize the query. 
    - We integrated it in django framework.

- **Ranking:** 
    - For ranking initially cosine similarity is used to retrieve top N documents. 
    - List of selected candidates is available for cross verification. Also Binomial model was used to rank the documents.
    - Both the ranking methods were evaluated using precision@R metric.

- **User interface:** 
    - UI for querying is built with the help of django framework. 
    - Database for resume uploading is also created.


### Phase 3
In phase 1 and phase 2 we build a basic search engine to retrieve the resumes which matches the JD.
In Phase 3 we improved the model by working on 3 major aspects: Vectorization, Information extraction and an ensemble ranking approach.

- **Vectorization:**
    - Words are vectorized using GloVe vectorization.
    - GloVe model is built by taking both global statistics and concurent word similarities.
    - So it is a better fit than the tf-idf  approach.

- **Information Extraction:**
    - For the information extraction part we used Named Entity Recognition to extract skillset info from resume.
    - For this we built a custom corpus and trained our own model so as to suit the context of our dataset.
    - This will help us to capture better features.
- **Ranking:**
    - Finally for the ranking we used a combined strategy of classification and ranking.
    - Classification is sone using Naive Bayes, SVM and RNN models and for ranking BM25 and cosine similarity measures were taken.
    - For a ranking, documents are chosen based on max voting of the classifiers and then the selected documents are ranking based on the average of the 2 ranking scores.
- **Evaluation:**
    - Models are evaluated using precision @R 
    - For the base model we got precision@R value of 32%
    - After adapting research paper and implementing them, we improved precision@R to 71%.


## Run the Code:
- Create a virtual environment for installing dependencies. [creating venv](https://www.geeksforgeeks.org/create-virtual-environment-using-venv-python/?ref=rp)
- Install dependencies from requirements.txt
- Run the djando framework. [run django](https://www.geeksforgeeks.org/django-basics/) 




