# %%
#import libraries
import re
import os
from pypdf import PdfReader
import pandas as pd

# Specify the folder path
# data_folder_path = "C:/Users/Annek/Documents/semestre 1/ML avec python/YODA/yoda_says/data"

# #### 1. Handling scripts

def extract_from_scrpits(data_folder_path):
# Load scripts
  dialogues = {}
  patterns = {
    "01": r"(?<=\n)([A-Z ]+)(?=:\s)(.+?)(?=(\n\s*\n|\n[A-Z ]+\n|\Z))",  # Pattern for "01" or "03"
    "03": r"(?<=\n)([A-Z ]+)(?=:\s)(.+?)(?=(\n\s*\n|\n[A-Z ]+\n|\Z))",
    "02": r"(?<=\n)([A-Z ]+)(?=\n)(.+?)(?=(\n\s*\n|\n[A-Z ]+\n|\Z))",   # Pattern for "02" and "06"
    "06": r"(?<=\n)([A-Z ]+)(?=\n)(.+?)(?=(\n\s*\n|\n[A-Z ]+\n|\Z))",
    "05": r"(?<=\n)([A-Z ]+)\s*(\([^)]*\))?\s*(.+?)(?=(\n\s*\n|\n[A-Z ]+\n|\Z))"  # Pattern for "05"
}
# Loop through all files in the folder
  for filename in os.listdir(data_folder_path+"/scripts"):
     print(filename)
     if filename.endswith(".txt"):  # Process only .txt files
        file_path = os.path.join(data_folder_path+"/scripts", filename)
        with open(file_path, "r") as file:
          script_text = file.read()
      # Determine which pattern to use based on the filename
          character_dialogue_pattern = None
          for key, pattern in patterns.items():
            if key in filename:  # Check if the key is part of the filename
               character_dialogue_pattern = re.compile(pattern, re.DOTALL)
               break

            # Skip files without a matching pattern
            if not character_dialogue_pattern:
                # print(f"No matching pattern for file: {filename}")
                continue
          for match in character_dialogue_pattern.finditer(script_text):
            character = match.group(1).strip()
            if "05" in filename:
              dialogue = match.group(3).strip()
            else:
              dialogue = match.group(2).strip()
            if character not in dialogues:
              dialogues[character] = []
            if "01" in filename or "03" in filename:
              dialogues[character].append(dialogue.split(": ")[1].replace("\n", ""))
            elif "05" in filename:
              dialogues[character].append(dialogue.split(".\n")[0].split("?\n")[0].replace("\n", ""))
            else:
              dialogues[character].append(dialogue.replace("\n", ""))
  print("Number of sentences from scripts:", len(dialogues["YODA"]))
  #Correct some dialogues
  dialogues["YODA"][1]="Trained as a Jedi, you request for him?"
  dialogues["YODA"][2]="Good, good, young one. How feel you?"
  dialogues["YODA"][3]="See through you, we can."
  dialogues["YODA"][4]="...Correct you were, Qui-Gon."
  dialogues["YODA"][5]="An apprentice, you have, Qui-Gon. Impossible, to take on a second."
  dialogues["YODA"][6]="Our own council we will keep on who is ready. More to learn, he has..."
  dialogues["YODA"][7]="Young Skywalker's fate will be decided later."
  dialogues["YODA"][8]="Confer on you, the level of Jedi Knight the Coucil does. But agreeon you taking this boy as your Padawan learner, I do not."
  return dialogues





# #### 2. Handling books

# first book
def read_yoad_dark_rendez_vous(data_folder_path):
  with open(data_folder_path+ "/books/epdf.pub_yoda-dark-rendezvousd56673c5bd1ecce25ac520457237f52013162.txt", "r", encoding="latin-1") as file:
    book_text = file.read()
  first_dialogues=re.findall(r'\bYoda\b.*?"(.*?)"', book_text.replace("\n",""))
  yoda_dialogues_book1=first_dialogues + [dialogue for dialogue in re.findall(r'"(.*?)".*?\bYoda\b', book_text.replace("\n","")) 
                                                 if dialogue not in first_dialogues]
  yoda_dialogues_book1= list(filter(lambda s: s.strip(), yoda_dialogues_book1))
  print("Number of sentences from book1:", len(yoda_dialogues_book1))
  return yoda_dialogues_book1


#second book
def read_revenge_of_the_sith(data_folder_path):
  reader = PdfReader(data_folder_path+ "/books/MATTHEW STOVER - Star Wars, Episode III - Revenge of the Sith-LucasBooks (2005).pdf")
  first_dialogues=[]
  for i in range (len(reader.pages)):
    first_dialogues=first_dialogues + re.findall(r'\bYoda\b.*?"(.*?)"', reader.pages[i].extract_text().replace("\n",""))
    yoda_dialogues_book2=first_dialogues + [dialogue for dialogue in re.findall(r'"(.*?)".*?\bYoda\b', reader.pages[i].extract_text().replace("\n","")) 
                                                 if dialogue not in first_dialogues]
  yoda_dialogues_book2= list(filter(lambda s: s.strip(), yoda_dialogues_book2))
  print("Number of sentences from book2:", len(yoda_dialogues_book2))
  return yoda_dialogues_book2

# #### 3. Quotes from the internet

def yodas_quotes():
  quotes=[
"Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
"Once you start down the dark path, forever will it dominate your destiny. Consume you, it will.",
"Always pass on what you have learned.",
"Patience you must have my young Padawan.",
"In a dark place we find ourselves, and a little more knowledge lights our way.",
"Death is a natural part of life. Rejoice for those around you who transform into the Force. Mourn them do not. Miss them do not. Attachment leads to jealousy. The shadow of greed, that is.",
"Powerful you have become, the dark side I sense in you.",
"Train yourself to let go of everything you fear to lose.",
"Feel the force!",
"Truly wonderful the mind of a child is.",
"Do or do not. There is no try.",
"Great warrior. Wars not make one great.",
"Size matters not. Look at me. Judge me by my size, do you? Hmm? Hmm. And well you should not. For my ally is the Force, and a powerful ally it is. Life creates it, makes it grow. Its energy surrounds us and binds us. Luminous beings are we, not this crude matter. You must feel the Force around you; here, between you, me, the tree, the rock, everywhere, yes. Even between the land and the ship.",
"The dark side clouds everything. Impossible to see the light, the future is.",
"You will find only what you bring in.",
"To be Jedi is to face the truth, and choose. Give off light, or darkness, Padawan. Be a candle, or the night.",
"Control, control, you must learn control!",
"On many long journeys have I gone. And waited, too, for others to return from journeys of their own. Some return; some are broken; some come back so different only their names remain.",
"In the end, cowards are those who follow the dark side.",
"Difficult to see. Always in motion is the future.",
"Ready are you? What know you of ready? For eight hundred years have I trained Jedi. My own counsel will I keep on who is to be trained. A Jedi must have the deepest commitment, the most serious mind. This one a long time have I watched. All his life has he looked away… to the future, to the horizon. Never his mind on where he was. Hmm? What he was doing. Hmph. Adventure. Heh. Excitement. Heh. A Jedi craves not these things. You are reckless.",
"Secret, shall I tell you? Grand Master of Jedi Order am I. Won this job in a raffle I did, think you? ‘How did you know, how did you know, Master Yoda?’ Master Yoda knows these things. His job it is.",
"To answer power with power, the Jedi way this is not. In this war, a danger there is, of losing who we are.",
"Many of the truths that we cling to depend on our point of view.",
"Named must your fear be before banish it you can.",
"You think Yoda stops teaching, just because his student does not want to hear? A teacher Yoda is. Yoda teaches like drunkards drink, like killers kill.",
"Do not assume anything Obi-Wan. Clear your mind must be if you are to discover the real villains behind this plot.",
"You will know (the good from the bad) when you are calm, at peace. Passive. A Jedi uses the Force for knowledge and defense, never for attack.",
"Soon will I rest, yes, forever sleep. Earned it I have. Twilight is upon me, soon night must fall.",
"When you look at the dark side, careful you must be. For the dark side looks back.",
"You will know (the good from the bad) when you are calm, at peace. Passive. A Jedi uses the Force for knowledge and defense, never for attack.",
"Smaller in number are we, but larger in mind.",
"Your path you must decide.",
"Always two there are, no more, no less. A master and an apprentice.",
"No longer certain, that one ever does win a war, I am. For in fighting the battles, the bloodshed, already lost we have. Yet, open to us a path remains. That unknown to the Sith is. Through this path, victory we may yet find. Not victory in the Clone Wars, but victory for all time.",
"If no mistake you have made, losing you are. A different game you should play.",
"Happens to every guy sometimes this does.",
"Adventure. Excitement. A Jedi craves not these things.",
"Only the Dark Lord of the Sith knows of our weakness. If informed the senate is, multiply our adversaries will.",
"Do, or do not. There is no try.",
"For my ally is the Force. And a powerful ally it is.",
"Step forward, Padawan. Anakin Skywalker, by the right of the Council... by the will of the Force... dub thee I do... Jedi... Knight of the Republic.",
"You must unlearn what you have learned.",
"This one a long time have I watched. All his life has he looked away, to the future, to the horizon. Never his mind on where he was, hmm? What he was doing. Hmm. Adventure. Heh. Excitement. Heh. A Jedi craves not these things.",
"Like fire across the galaxy the Clone Wars spread.",
"If so powerful you are, why leave?",
"Mine! Mine! Mine! MINE!!!",
"When nine hundred years old you reach, look as good you will not, hmm?",
"For my ally is the Force. And a powerful ally it is. Life creates it, makes it grow. Its energy surrounds us and binds us. Luminous beings are we, not this crude matter. You must feel the Force around you. Here, between you, me, the tree, the rock, everywhere! Yes, even between the land and the ship.",
"No.... there is another.",
"Because it is easy.",
"Help you I can. Yes, mmm.",
"Oh! Great warrior. Wars not make one great.",
"Each act, you see, is like a fossil, preserved in the Force, as – aiee! Stop! Stop! Eating this, I am!",
"Victory? Victory, you say? Master Obi-Wan, not a victory. The shroud of the Dark Side has fallen. Begun, the Clone War has.",
"Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate....leads to suffering.",
 "Strong am I with the Force, but not that strong. Twilight is upon me, and soon night must fall. That is the way of things. The way of the Force.",
 "When you look at the dark side, careful you must be ... for the dark side looks back.",
 "If in anger you answer, then in shame you dwell.",
 "Yes. We would like our meal comped.",
 "I was. Defending my wallet I was from the evil price hikes.",
 "Luke... the Force runs strong in your family. Pass on what you have learned. Luke... there is... another... Sk... ky... walker...",
 "I don't want your help. I want my lamp back. I'm gonna need it to get out of this slimy mudhole.",
 "Mudhole? Slimy? My home this is!",
 "If no mistake have you made, yet losing you are... a different game you should play.",
 "I won't fail you. I'm not afraid.",
 "Oh, you will be. You will be.",
 "There's something not right here. I feel cold... death.",
 "That place is strong with the dark side of the Force. A domain of evil it is. In you must go.",
 "Only what you take with you.",
 "Secret, shall I tell you? Grand Master of Jedi Order am I. Won this job in a raffle I did, think you? 'How did you know, how did you know, Master Yoda?' Master Yoda knows these things. His job it is.",
 "Soon will I rest. Yes, forever sleep. Earned it, I have.",
 "I want… I want a rose.",
 "How you get so big eating food of this kind?", "Lost a planet Master Obi-Wan has. How embarrassing. How embarrassing.", 
 "Not if anything to say about it I have!",
 "Attachment leads to jealousy. The shadow of greed that is.",
 "Train yourself to let go of everything you fear to lose.",
 "Always with you it cannot be done. Hear you nothing that I say?",
 "Listen, friend, we didn't mean to land in that puddle, and if we could get our ship out, we would, but we can't, so why don't you just—",
 "Awww, cannot get your ship out!",
 "Strong you are with the dark side, young one… but not that strong.",
 "No! No different! Only different in your mind.",
 "A Jedi uses the Force for knowledge and defense, never for attack.",
 "Twilight is upon me, and soon night must fall. That is the way of things... the way of the Force.",
 "If far from the Force you find yourself, trust you can that it is not the Force which moved.",
 "Control, control, you must learn control!", "I cannot teach him. The boy has no patience.",
 "Hmm. Much anger in him, like his father.",
 "Was I any different when you taught me?",
 "To a dark place this line of thought will carry us.",
 "Stubborn and hard is your head. Soften it we will.",
 "Mysterious are the ways of the Force.",
 "Very mysterious.", "Alone? No. Always the past to keep me company. The creatures on the planet, and the Force. And now you. Annoying though you may be.",
 "A warrior who cannot dance? Clumsy in both war and peace he is.",
 "Yarael Poof has a small head. But a small head means not small thoughts.", "Mysterious are the ways of the Force.","Very mysterious.",
 "Think you I have never felt the touch of the dark? Know you what a soul so great as Yoda can make, in eight hundred years?",
 "Many mistakes!", "To be Jedi is to face the truth, and choose. Give off light, or darkness, Padawan. Be a candle, or the night, Padawan: but choose!",
 "Stop! Stop! Eating this, I am!",
 "Ignorant machine! Not on menu, my food ever is. Made special for me, was this!", "Back! Mine! Go away!", "Bah! Droids!", "Double jump you can. Easy it is.",
 "When you look back, lose your place on the path, you do. Learn you will, Anakin, that stars move and stars fall, and nothing at all do they have to do with you.",
 "Seen much have we, Artoo. Been part of much. Your part will continue. His part is just beginning… but my part, soon, will come to an end.","Surprised?",
 "Ready, are you? What know you of ready? For eight hundred years have I trained Jedi. My own counsel will I keep on who is to be trained.",
 "In pursuit of clues, we are.",
 "A Jedi's strength flows from the Force. But beware of the dark side. Anger. Fear. Aggression. The dark side of the Force are they. Easily they flow. Quick to join you in a fight. If once you start down the dark path, forever will it dominate your destiny. Consume you it will, as it did Obi-Wan's apprentice.",
 "No! No…no. Quicker. Easier. More seductive.", "You will know, when you are calm. At peace. Passive.", 
 "An infinite mystery is the Force. The more we learn, the more we discover how much we do not know.",
 "Only a fully trained Jedi knight, with the Force as his ally, will conquer Vader and his Emperor. If you end your training now, if you choose the quick and easy path, as Vader did, you will become an agent of evil.",
 "And sacrifice Han and Leia?", "If you honor what they fight for? Yes!", "Chaos begun cannot be ordered so easily.",
 "Believe I do, Senator, that a free society must guard its freedom zealously, lest wake one morning it does to find all freedom disappeared.",
 "Like a river, the Force flows through you. Learned much you have, in these past three months. And more quickly than any student I have taught before.",
 "Even my father?",
 "Strong was the Force with Anakin, before he became Vader. Yet impatient and stubborn he was. Constantly pushing to excel beyond his ability. More sublime, your approach has been.",
"Yet learned you have not the hazards of using a superheated blade against a foe made mainly of water.",
 "Will he finish what he begins?", "Wake up.", "Poking you with a stick, I am.",
 "What use saving the galaxy is if so much hurt and pain one must cause? The Jedi way that is not. No. Hurt you I won't. Trust you I will, trust you…and the Force. The Jedi way that is. Be good to speak again it will.",
 "Mmm. Friends you have there.", "It is the future you see.","The future... Will they die?", "Difficult to say. Always in motion is the future."
"It is the spontaneity that you find so easily which others do not, that is what sets you apart.",
"A flaw more and more common among Jedi. Too sure of themselves they are. Even the older, more experienced ones.",
"Blind we are, of creation of this clone army we could not see.",
"Doubt in battle, there cannot be. Belief, there must be.",
"No greater gift there is, than a generous heart.",
"If in anger you answer, then in shame you dwell.",
"Arduous is discovering oneself, going on the greatest exploration it is.",
"Many of the truths that we cling to depend on our point of view.",
"Patience you must have my young Padawan.",
"You think Yoda stops teaching, just because his student does not want to hear? A teacher Yoda is. Yoda teaches like drunkards drink, like killers kill.",
"If no mistake you have made, losing you are. A different game you should play.",
"Your path you must decide.",
"Hard to see the dark side is.",
"Always two there are, no more, no less. A master and an apprentice.",
"Clear, your mind must be, if you are to discover the real villains behind this plot.",
"To answer power with power, the Jedi way this is not. In this war, a danger there is, of losing who we are.",
"In the end, cowards are those who follow the dark side.",
"On many long journeys have I gone. And waited, too, for others to return from journeys of their own. Some return; some are broken; some come back so different only their names remain.",
"To be Jedi is to face the truth and choose. Give off light, or darkness, Padawan. Be a candle, or the night.",
"The dark side clouds everything. Impossible to see, the future is.",
"Feel the Force!"
"Powerful you have become. The dark side I sense in you.",
"Death is a natural part of life. Rejoice for those around you who transform into the Force. Mourn them do not. Miss them do not.",
"In a dark place we find ourselves, and a little more knowledge lights our way.",
"Much to learn you still have.",
"Attachment leads to jealousy. The shadow of greed, that is.",
"Named must your fear be before banish it you can.",
"Truly wonderful, the mind of a child is.",
"Anger, fear, aggression. The dark side are they.",
"Fear is the path to the dark side.",
"No, no, no. Quicker, easier, more seductive.",
"Train yourself to let go of everything you are afraid to lose.",
"A Jedi uses the Force for knowledge and defense, never for attack.",
"So certain are you? Always with you what cannot be done. Hear you nothing that I say?"
"A Jedi's strength flows from the Force.",
"I can’t teach him. The boy has no patience.",
"Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
"Smaller in number are we, but larger in mind.",
"Pass on what you have learned. Strength. Mastery. But weakness, folly, failure also. Yes, failure most of all.",
"You must unlearn what you have learned.",
"The greatest teacher, failure is.",
"When you look at the dark side, careful you must be. For the dark side looks back.",
"To a dark place this line of thought will carry us. Hmm. Great care we must take.",
"A way, there always is.", 
"You will find only what you bring in.",
"Always in motion, is the future.",
"...we are what they grow beyond. That is the true burden of all masters.",
"Once you start down the dark path, forever will it dominate your destiny. Consume you, it will.",
"Size matters not. Look at me. Judge me by my size, do you?",
"All his life has he looked away…to the future, to the horizon. Never his mind on where he was. Hmm? What he was doing. Hmph. Adventure. Heh. Excitement. Heh. A Jedi craves not these things.",
"Soon will I rest, yes, forever sleep. Earned it I have. Twilight is upon me, soon night must fall.",
"Control, control, you must learn control!"
"Ah! A great warrior. Wars not make one great.",
"Do. Or do not. There is no try."]
#Delete duplicates
  quotes=list(set(quotes))
  print("Number of quotes:", len(quotes))
  return quotes

# #### 4. Yoda corpus in Kaggle

def load_yoad_corpus(data_folder_path):
  starwars_corpus=pd.read_csv(data_folder_path+"/yoda-corpus.csv",sep=',')
  yoda_corpus=starwars_corpus[starwars_corpus["character"]=="YODA"]["text"].tolist()
  print("NUmber of sentences from corpus:", len(yoda_corpus))
  return yoda_corpus

# #### Final dataset

def retrieve_yoda_sentences(data_folder_path):
   #Assemble everything and delete duplicates
  yoda_dialogues_book1= read_yoad_dark_rendez_vous(data_folder_path)
  yoda_dialogues_book2= read_revenge_of_the_sith(data_folder_path)
  quotes= yodas_quotes()
  dialogues=extract_from_scrpits(data_folder_path)
  yoda_corpus=load_yoad_corpus(data_folder_path)
  yoda_dialogues=list(set(yoda_dialogues_book1+yoda_dialogues_book2+quotes+dialogues["YODA"][1:80]+yoda_corpus))
  print("Final number of sentences:",len(yoda_dialogues))
  return yoda_dialogues

if __name__ == "__main__":
  retrieve_yoda_sentences()

