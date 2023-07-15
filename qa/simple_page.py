import mwclient 


CATEGORY_TITLE = "Category:2022 FIFA World Cup"
WIKI_SITE = "en.wikipedia.org"


def titles_from_category(
    category: mwclient.listing.Category, max_depth: int
) -> set[str]:
    """Return a set of page titles in a given Wiki category and its subcategories."""
    titles = set()
    for cm in category.members():
        if type(cm) == mwclient.page.Page:
            # ^type() used instead of isinstance() to catch match w/ no inheritance
            titles.add(cm.name)
        elif isinstance(cm, mwclient.listing.Category) and max_depth > 0:
            deeper_titles = titles_from_category(cm, max_depth=max_depth - 1)
            titles.update(deeper_titles)
    return titles

def get_page_from_title(
    title: str,
    site_name: str = WIKI_SITE
) -> str: 
    site = mwclient.Site(site_name)
    page = site.pages[title]
    return page.text()

site = mwclient.Site(WIKI_SITE)
category_page = site.pages[CATEGORY_TITLE]
titles = titles_from_category(category_page, max_depth=2)
print(f"Found {len(titles)} article titles in {CATEGORY_TITLE}.")



for title in titles:
    with open('pages/' + title + '.txt','w') as f: 
        f.write(get_page_from_title(title))
    print(title)
print(f"Found {len(titles)} pages.")


    

