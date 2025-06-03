import pandas as pd

def clean_and_summarize(fp):
    df = pd.read_csv(fp)
    df[['Math', 'Science', 'English']] = df[['Math', 'Science', 'English']].apply(lambda x: x.fillna(x.mean()))
    df['Gender'] = df['Gender'].map({'Female': 0, 'Male': 1})
    return df.groupby('Gender')[['Math', 'Science', 'English']].mean().reset_index().round(2)

summary_df = clean_and_summarize(r'SA\student_scores.csv')
print(summary_df)