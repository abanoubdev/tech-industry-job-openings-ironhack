import kagglehub
import pandas as pd
import os
from .DataSetConstants import df_ai_impact_on_job_market_2024_2030, df_ai_impact_jobs_2030

class DataSetCombiner:    
    def __init__(self):
        self.dataset_a_handle = df_ai_impact_on_job_market_2024_2030
        self.dataset_b_handle = df_ai_impact_jobs_2030
        self.merge_key = 'Job_Title'

    def _get_csv_path(self, folder_path: str) -> str:
        csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
        if not csv_files:
            raise FileNotFoundError(f"No CSV file found in {folder_path}")
        return os.path.join(folder_path, csv_files[0])

    def execute_pipeline(self) -> pd.DataFrame:
        try:
            
            print("Downloading datasets...")
            path_a = kagglehub.dataset_download(self.dataset_a_handle) 
            path_b = kagglehub.dataset_download(self.dataset_b_handle)

            csv_path_a = self._get_csv_path(path_a)
            csv_path_b = self._get_csv_path(path_b)

            df_a = pd.read_csv(csv_path_a)
            df_b = pd.read_csv(csv_path_b)

            if 'Job Title' in df_a.columns:
                df_a.rename(columns={'Job Title': self.merge_key}, inplace=True)

            df_a[self.merge_key] = df_a[self.merge_key].astype(str).str.lower().str.strip()
            df_b[self.merge_key] = df_b[self.merge_key].astype(str).str.lower().str.strip()

            merged_df = pd.merge(df_a, df_b, on=self.merge_key, how='inner')
            
            print(f"Successfully merged! The new dataset has {merged_df.shape[0]} rows.")
            return merged_df

        except Exception as e:
            print(f"An error occurred during the merge pipeline: {e}")
            return pd.DataFrame() # Return empty dataframe on failure