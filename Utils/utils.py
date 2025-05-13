"""
Created a utils.py script for best code organization by separating the rank_moves helper function from the main analysis code. This makes it easier to update and common functions and also keeps the notebook cleaner.
"""

def rank_movies(df, column, ascending=False, filter_condition=None, n=10):
    """
    Rank movies based on a column with optional filtering
    """
    if filter_condition:
        filtered_data = df.filter(filter_condition)
    else:
        filtered_data= df

    if ascending:
        ranked_data = filtered_data.orderBy(col(column).asc())
    else:
        ranked_data = filtered_data.orderBy(col(column).desc())

    return ranked_data.limit(n)
