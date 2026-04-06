import os

# --- BASE PATHS ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_RAW_DIR = os.path.join(BASE_DIR, 'data', 'raw')
DATA_PROC_DIR = os.path.join(BASE_DIR, 'data', 'processed')
FIGURES_DIR = os.path.join(BASE_DIR, 'reports', 'figures')

# --- FILE NAMES ---
FILES = {
    'biometric': 'aadhar_biometric_merged.csv',
    'enrolment': 'aadhar_enrolment_merged.csv',
    'demographic': 'aadhar_demographic_merged.csv'
}

# --- KEY COLUMNS & FORMATS ---
JOIN_KEYS = ['date', 'state', 'district', 'pincode']
DATE_FORMAT = '%d-%m-%Y'

# --- STATE STANDARDIZATION MAPPING ---
STATE_MAPPING = {
    # 1. CORRUPTED / SHIFTED ROWS (Must be dropped)
    '100000': 'DROP',
    'balanagar': 'DROP',
    'darbhanga': 'DROP',
    'jaipur': 'DROP',
    'madanapalle': 'DROP',
    'nagpur': 'DROP',
    'puttenahalli': 'DROP',
    'raja annamalai puram': 'DROP',

    # 2. TYPOS & VARIATIONS 
    'andaman & nicobar islands': 'andaman and nicobar islands',
    'chhatisgarh': 'chhattisgarh',
    'jammu & kashmir': 'jammu and kashmir',
    'delhi': 'nct of delhi',
    'orissa': 'odisha',
    'pondicherry': 'puducherry',
    'tamilnadu': 'tamil nadu',
    'uttaranchal': 'uttarakhand',
    'west  bengal': 'west bengal',
    'west bangal': 'west bengal',
    'west bengli': 'west bengal',
    'westbengal': 'west bengal',

    # 3. UNION TERRITORY CONSOLIDATION
    'dadra & nagar haveli': 'dadra and nagar haveli and daman and diu',
    'dadra and nagar haveli': 'dadra and nagar haveli and daman and diu',
    'daman & diu': 'dadra and nagar haveli and daman and diu',
    'daman and diu': 'dadra and nagar haveli and daman and diu',
    'the dadra and nagar haveli and daman and diu': 'dadra and nagar haveli and daman and diu',
}