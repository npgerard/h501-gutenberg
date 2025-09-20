from tt_gutenberg.helpers import *

def list_authors(by_languages=True, alias=True):
    """
    Return a list of authors or aliases sorted by translation count or language count.

    Parameters:
    - by_languages (bool): If True, sort by the number of unique languages translated into.
                           If False, sort by total number of translations.
    - alias (bool): If True, use the 'alias' column.
                    If False, use the 'author' column.

    Returns:
    - List of author names or aliases sorted descending by selected metric.
    """
    df = get_author_works_translations()

    # Select which column to group by
    group_col = 'alias' if alias else 'author'

    # Filter out missing or empty values in the chosen column
    df = df[df[group_col].notna()]
    df = df[df[group_col].str.strip() != '']

    if by_languages:
        # Count unique languages per author/alias
        counts = df.groupby(group_col)['language'].nunique()
    else:
        # Count total translations per author/alias
        counts = df.groupby(group_col).size()

    counts = counts.sort_values(ascending=False)

    return counts.index.tolist()

def get_author_works_translations():
    return load_merged_author_works_languages_dataset()

