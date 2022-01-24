import wikipedia
import time
import pandas as pd
from tqdm import tqdm
tqdm.pandas()

titles = pd.read_csv("./political_topics_l1.csv")
print(titles.head())
# titles = titles.head(2)

def get_wiki_text(title: str):
    try:
        wiki = wikipedia.page(title)
        text = wiki.content
        return " ".join(text.split())
    except:
        return "NA"

titles["text"] = titles.progress_apply(lambda row: get_wiki_text(row.title), axis=1)

print(titles.head())

titles.to_csv(f"./titles_with_text_{time.time()}.csv", index=False)


