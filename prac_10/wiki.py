# wiki.py

import wikipedia


def get_wiki_summary(title):
    try:
        page = wikipedia.page(title)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print("URL:", page.url)
    except wikipedia.DisambiguationError as e:
        print(f"Disambiguation Error: {e.options}")


if __name__ == "__main__":
    while True:
        user_input = input("Enter a Wikipedia page title or search phrase (blank to exit): ").strip()
        if not user_input:
            break
        get_wiki_summary(user_input)
