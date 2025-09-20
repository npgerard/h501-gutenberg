import pandas as pd

def load_gutenbert_authors():
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
    df = pd.read_csv(url)

    # Drop rows with missing or invalid aliases
    df = df[df['alias'].notna()]
    df = df[df['alias'].str.strip() != '']

    return df

def load_gutenburg_metadata():
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"
    df = pd.read_csv(url)

    # Drop rows with missing or invalid language codes
    df = df[df['language'].notna()]
    df = df[df['language'].str.strip() != '']

    return df

def load_gutenberg_languages():
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv"
    df = pd.read_csv(url)

    # Drop rows with missing or invalid language codes
    df = df[df['language'].notna()]
    df = df[df['language'].str.strip() != '']

    return df

def load_merged_author_works_languages_dataset():
    authors_df = load_gutenbert_authors()
    metadata_df = load_gutenburg_metadata()
    languages_df = load_gutenberg_languages()

    # Merge authors with metadata on 'gutenberg_author_id' -> 'gutenberg_id'
    df_authors_works = authors_df.merge(metadata_df[['gutenberg_author_id', 'gutenberg_id', ]], how='left', on='gutenberg_author_id')

    # Merge the result with languages on 'language'
    df_authors_works_translations = df_authors_works.merge(languages_df, on='gutenberg_id', how='inner')

    return df_authors_works_translations

