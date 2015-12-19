# NLP_movie_roles
Use natural language processing techniques to extract relations between movie character names, and their corresponding roles and genders.

### Collaborators:
* ##### Wenqin Chen
  Roles: Information Architect, Data Cleaning, POS and NER tagger, Name Extraction, Name Filtering, Alias Association, Regex and Chunking
* ##### Jordan Shedlock
  Roles: Data Cleaning, Regex and Chunking, Result Evaluation and Analysis

### Project Overview:
* ##### Problem Statement:
  The representation of character roles and genders in movies has significant social impact. To study the distribution of roles and genders in movies, we need
to first get the data. How can we effectively extract characters’ roles and genders from movie summaries and credit lists?
* ##### Dataset:
  Credit list and summary information for around 34,000 US movies with 10 or more IMDb reviews and IMDb and/or Wikipedia summaries.
* ##### Result:
  We found 114,922 character name variants in the summaries, for which we were able to 
extract 71,216 candidate character roles (2.1 roles per movie).
On a semi-random evaluation set of 10 movies, our algorithm achieved a 54% 
precision (proportion of correct, descriptive character roles among those that 
were matched), and 46% recall (character names from summaries correctly 
matched with IMDB credits).
* ##### Project Flowchart
  Please view it in out poster at findings_and_reports/RoleModels_final_post.pdf 

### Usage:
* ##### Main code
  Our main code is in role_models-final.ipynb
* ##### Data
  data/input contains the data obtained after inital cleaning. data/output contains data that are generated later on, some of which in turn became input data for further steps.
* ##### Running Stanford NER and POS taggers
  stanfordTaggers/ contains the tagger code. We optimized these taggers' speed by creating a server and client. For example, to start the client and server for NET tagger, do the following: in nerTagger/, start-nert-server.sh starts the nert server, run with "bash start-nert-server.sh", nertclient.py is client to above, import it in your code.
* ##### Findings: 
  findings_and_reports/ contains our final report and poster.
