import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """
    Load CSV file into DataFrame
    """
    df = pd.read_csv(file_path, on_bad_lines='skip')
    return df


def convert_datetime(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert datetime columns
    """
    df['created_at'] = pd.to_datetime(df['created_at'], errors='coerce')
    df['resolved_at'] = pd.to_datetime(df['resolved_at'], errors='coerce')
    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing/null values
    """
    # Drop critical missing rows
    df = df.dropna(subset=['created_at', 'resolved_at'])

    # Fill optional columns
    df['csat_score'] = df['csat_score'].fillna(df['csat_score'].median())
    df['num_replies'] = df['num_replies'].fillna(0)

    return df


def fix_data_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert columns to correct data types
    """
    numeric_cols = [
        'resolution_hours',
        'sla_target_hours',
        'csat_score',
        'num_replies',
        'first_response_hours'
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    df['sla_breached'] = df['sla_breached'].astype(bool)

    return df


def validate_sla(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recalculate SLA breach for validation
    """
    df['calculated_sla_breach'] = df['resolution_hours'] > df['sla_target_hours']
    return df


def remove_anomalies(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove invalid / extreme values
    """
    df = df[df['resolution_hours'] >= 0]
    df = df[df['first_response_hours'] >= 0]

    # Optional upper cap
    df = df[df['resolution_hours'] < 500]

    return df


def clean_data(file_path: str) -> pd.DataFrame:
    """
    Full cleaning pipeline
    """
    df = load_data(file_path)
    df = convert_datetime(df)
    df = handle_missing_values(df)
    df = fix_data_types(df)
    df = validate_sla(df)
    df = remove_anomalies(df)
    df = feature_engineering(df)

    return df


def save_data(df: pd.DataFrame, output_path: str):
    """
    Save cleaned dataset
    """
    df.to_csv(output_path, index=False)

def feature_engineering(df):
    """
    Create derived features for analysis
    """

    # 1. Resolution Speed Category
    def resolution_category(hours):
        if hours <= 8:
            return "Fast"
        elif hours <= 24:
            return "Medium"
        else:
            return "Slow"

    df['resolution_speed_category'] = df['resolution_hours'].apply(resolution_category)

    # 2. First Response Delay Flag
    df['response_delay_flag'] = df['first_response_hours'].apply(
        lambda x: "Delayed" if x > 24 else "On-Time"
    )

    # 3. SLA Compliance (clean version)
    df['sla_compliance'] = df['resolution_hours'] <= df['sla_target_hours']

    # 4. Normalize categorical columns (clean text)
    categorical_cols = ['priority', 'category', 'channel', 'region', 'status']

    for col in categorical_cols:
        df[col] = df[col].str.strip().str.title()

    return df