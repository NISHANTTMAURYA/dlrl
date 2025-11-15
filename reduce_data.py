import pandas as pd
import numpy as np

print("=" * 60)
print("REDUCING TRAINING AND TEST DATA BY 50%")
print("=" * 60)

# Load the normalized data
print("\nLoading data...")
train_df = pd.read_csv('dataset/train_data_normalized.csv')
test_df = pd.read_csv('dataset/test_data_normalized.csv')

print(f"Original train rows: {len(train_df):,}")
print(f"Original test rows: {len(test_df):,}")

# Get unique test IDs
train_test_ids = train_df['ID_test'].unique()
test_test_ids = test_df['ID_test'].unique()

print(f"\nOriginal train test sessions: {len(train_test_ids)}")
print(f"Original test test sessions: {len(test_test_ids)}")

# Randomly sample 50% of test IDs (to keep complete sessions)
np.random.seed(42)  # For reproducibility
train_sample_ids = np.random.choice(train_test_ids, size=len(train_test_ids)//2, replace=False)
test_sample_ids = np.random.choice(test_test_ids, size=len(test_test_ids)//2, replace=False)

print(f"\nSampled train test sessions: {len(train_sample_ids)}")
print(f"Sampled test test sessions: {len(test_sample_ids)}")

# Filter data to keep only sampled test IDs
train_reduced = train_df[train_df['ID_test'].isin(train_sample_ids)]
test_reduced = test_df[test_df['ID_test'].isin(test_sample_ids)]

print(f"\nReduced train rows: {len(train_reduced):,} ({len(train_reduced)/len(train_df)*100:.1f}%)")
print(f"Reduced test rows: {len(test_reduced):,} ({len(test_reduced)/len(test_df)*100:.1f}%)")

# Overwrite the original files
print("\nSaving reduced data...")
train_reduced.to_csv('dataset/train_data_normalized.csv', index=False)
test_reduced.to_csv('dataset/test_data_normalized.csv', index=False)

print("\n✓ Overwritten train_data_normalized.csv")
print("✓ Overwritten test_data_normalized.csv")

print("\n" + "=" * 60)
print("DATA REDUCTION COMPLETE!")
print("=" * 60)
print(f"\nTraining data reduced by: {len(train_df) - len(train_reduced):,} rows")
print(f"Test data reduced by: {len(test_df) - len(test_reduced):,} rows")
print("\nYour model training should now be much faster!")
