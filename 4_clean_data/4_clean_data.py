import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

def clean_and_preprocess(df):
    # Separate numerical and categorical columns
    numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    

    # Define preprocessing for numerical columns (impute missing values, then normalize)
    numerical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ])

    # Define preprocessing for categorical columns (impute missing values, then one-hot encode)
    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ])

    # Combine preprocessing steps
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numerical_transformer, numerical_cols),
            ('cat', categorical_transformer, categorical_cols)
        ]
    )

    # Apply transformations
    df_processed = preprocessor.fit_transform(df)

    # Convert the processed data back into a DataFrame
    df_processed = pd.DataFrame(df_processed, columns=numerical_cols.tolist() + list(preprocessor.named_transformers_['cat']['onehot'].get_feature_names_out(categorical_cols)))

    return df_processed


df = pd.read_csv("not_cleaned.csv")
print(df.head())
print()
cleaned_df = clean_and_preprocess(df)
print(cleaned_df.head())
