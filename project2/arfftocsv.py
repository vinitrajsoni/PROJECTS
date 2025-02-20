import pandas as pd
from scipy.io import arff

def arff_to_csv(arff_file, csv_file):
    # Load the ARFF file
    data, meta = arff.loadarff(arff_file)

    # Convert to a pandas DataFrame
    df = pd.DataFrame(data)

    # Save to a CSV file
    df.to_csv(csv_file, index=False)

# Example usage
arff_file = '95k-random.arff'
csv_file = '95k-random.csv'
arff_to_csv(arff_file, csv_file)

print(f"Conversion complete! CSV file saved as {csv_file}")
