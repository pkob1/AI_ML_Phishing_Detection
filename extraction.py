import pandas as pd
from urllib.parse import urlparse
import whois
from datetime import datetime

# Load the CSV file
file_path = '/Users/papakobinaorleans-bosomtwe/Desktop/Summer 2024/AI:ML Cyber/Project/project_final/data_bal - 20000.csv'
df = pd.read_csv(file_path)

# Function to extract features from a URL
def extract_features(url):
    parsed_url = urlparse(url)
    
    # Length of the URL
    url_length = len(url)
    
    # Count of dots in the URL
    dot_count = url.count('.')
    
    # Count of hyphens in the URL
    hyphen_count = url.count('-')
    
    # Whether the URL uses HTTPS
    uses_https = int(parsed_url.scheme == 'https')
    
    # Length of the domain
    domain_length = len(parsed_url.netloc)
    
    # Path length
    path_length = len(parsed_url.path)
    
    # Query length
    query_length = len(parsed_url.query)
    
    # WHOIS information and domain age
    domain = parsed_url.netloc
    try:
        whois_info = whois.whois(domain)
        creation_date = whois_info.creation_date
        
        if isinstance(creation_date, list):
            # Sometimes, creation_date is a list of dates; take the earliest
            creation_date = min(creation_date)
            
        if creation_date:
            domain_age = (datetime.now() - creation_date).days
        else:
            domain_age = None
    except Exception as e:
        whois_info = None
        domain_age = None

    return {
        'URL': url,
        'URL Length': url_length,
        'Dot Count': dot_count,
        'Hyphen Count': hyphen_count,
        'Uses HTTPS': uses_https,
        'Domain Length': domain_length,
        'Path Length': path_length,
        'Query Length': query_length,
        'Domain Age (days)': domain_age
    }

# Extract features for each URL in the dataframe
features = df['URLs'].apply(extract_features)

# Convert the features to a DataFrame
features_df = pd.DataFrame(features.tolist())

# Add the existing labels to the features DataFrame
features_df['Label'] = df['Labels']

# Output the features with labels to a new CSV file
output_file_with_labels = 'phishing_features_with_whois.csv'
features_df.to_csv(output_file_with_labels, index=False)

print(f"Features extracted and saved to {output_file_with_labels}")
