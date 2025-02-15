# yoda_says
This project is an attempt to apply what has been learn in class. The goal is to create a chatbot that interacts in Yoda's style.
There are 3 main parts:
## Install required libraries
```
python install -r requirements.txt
```
# 1. Extracting yoda's dialogues 
Here the dialogues are extracted from:
## a. Star wars 1 to 6 scipts:
- 01_the_phatom_menace, 
- 02_attack_of_the_clones, 
- 03_revenge_of_the_sith, 
- 05_the_empire_strikes_back, 
- 06_return_of_the_jedi
## b. Star wars books:
- Yoda: Dark Rendezvous: Star Wars Legends: A Clone Wars Novel Poche – 23 novembre 2004, Édition en Anglais  de Sean Stewart (Auteur)
- Star Wars Episode III: Revenge of the Sith Relié – 2 avril 2005, Édition en Anglais  de Matthew Woodring Stover (Auteur), George Lucas (Auteur)
## c. Yoda's quotes from the internet:
- https://starwars.fandom.com/wiki/Wookieepedia:Quote_of_the_Day/Archive/Yoda
- https://parade.com/943548/parade/yoda-quotes/
- https://www.buzzfeed.com/jeremyhayes/yoda-quotes
- https://www.rd.com/article/yoda-quotes/
## c. Star wars corpus from Kaggle: 
https://www.kaggle.com/datasets/stefanocoretta/yoda-speech-corpus?resource=download

## Data folder structure:

│── data/              
│   ├── books 
|   |   ├── yoda-dark-rendezvous.txt      
|   |   ├── MATTHEW STOVER - Star Wars, Episode III - Revenge of the Sith-LucasBooks (2005).pdf      
│   ├── scripts
|   |   ├── 01_the_phatom_menace.txt 
|   |   ├── 02_attack_of_the_clones.txt 
|   |   ├── 03_revenge_of_the_sith.txt
|   |   ├── 05_the_empire_strikes_back.txt 
|   |   ├── 06_return_of_the_jedi.txt         
│   ├── yoda-corpus.csv

## Execute code
```
python extract_yoda_dialogues.py
```
# 2. Fine-tuning text generation model
# 3. Create the chatbot