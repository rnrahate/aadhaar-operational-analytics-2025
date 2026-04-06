import pandas as pd
import os
import datetime
from src.config import (DATA_RAW_DIR, DATA_PROC_DIR, FIGURES_DIR, 
                        DATE_FORMAT, STATE_MAPPING, FILES, JOIN_KEYS)

def load_data(file_key):
    """Loads a raw dataset."""
    path = os.path.join(DATA_RAW_DIR, FILES[file_key])
    print(f"Loading {FILES[file_key]}...")
    return pd.read_csv(path)

def clean_dates(df, date_col='date'):
    """Converts string dates to datetime objects."""
    df[date_col] = pd.to_datetime(df[date_col], format=DATE_FORMAT)
    return df

def standardize_states(df, state_col='state'):
    """Standardizes state names and drops corrupted rows."""
    df[state_col] = df[state_col].astype(str).str.strip().str.lower()
    df[state_col] = df[state_col].replace(STATE_MAPPING)
    
    # DROP CORRUPTED ROWS
    initial_rows = len(df)
    df = df[df[state_col] != 'DROP'].copy()
    dropped_rows = initial_rows - len(df)
    if dropped_rows > 0:
        print(f"  -> Removed {dropped_rows} corrupted rows.")
    
    # Convert back to Title Case
    df[state_col] = df[state_col].str.title()
    df[state_col] = df[state_col].str.replace(' And ', ' and ')
    df[state_col] = df[state_col].str.replace(' Of ', ' of ')
    
    return df

def fix_pincodes(df, pin_col='pincode'):
    """Ensures pincodes are exactly 6 digits."""
    df[pin_col] = df[pin_col].astype(str).str.split('.').str[0].str.zfill(6)
    return df

def process_and_save(file_key):
    """Runs the full Phase 0 pipeline for a specific file and saves it."""
    df = load_data(file_key)
    df = clean_dates(df)
    df = standardize_states(df)
    df = fix_pincodes(df)
    
    out_path = os.path.join(DATA_PROC_DIR, f"cleaned_{FILES[file_key]}")
    df.to_csv(out_path, index=False)
    print(f"  -> Saved clean data to {out_path}\n")
    return df

def merge_datasets(df_bio, df_demo, df_enrol):
    """Merges all 3 datasets via OUTER JOIN to preserve all events."""
    merged_1 = pd.merge(df_enrol, df_demo, on=JOIN_KEYS, how='outer')
    final_merged = pd.merge(merged_1, df_bio, on=JOIN_KEYS, how='outer')
    
    # Fill missing numeric values with 0
    numeric_cols = final_merged.select_dtypes(include=['float64', 'int64']).columns
    final_merged[numeric_cols] = final_merged[numeric_cols].fillna(0).astype(int)
    return final_merged

def save_figure(fig, filename_prefix):
    """Saves a matplotlib/plotly figure with a timestamp."""
    os.makedirs(FIGURES_DIR, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(FIGURES_DIR, f"{filename_prefix}_{timestamp}.png")
    
    if hasattr(fig, 'write_image'):
        fig.write_image(filepath)
    else:
        fig.savefig(filepath, bbox_inches='tight', dpi=300)
    print(f"Saved figure to {filepath}")