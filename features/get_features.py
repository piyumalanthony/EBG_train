import sys
import os
current_script_dir = os.path.dirname(os.path.abspath(__file__))

# Get the parent of the parent directory
parent_of_parent_dir = os.path.dirname(os.path.dirname(current_script_dir))

# Add the parent of the parent directory to sys.path
sys.path.insert(0, parent_of_parent_dir)
from EBG_train.features.feature_extractor import FeatureExtractor
import os
import pandas as pd


if __name__ == '__main__':
    raw_path = os.path.join(os.path.pardir, "data", "raw")
    folder_names = [folder for folder in os.listdir(raw_path) if os.path.isdir(os.path.join(raw_path, folder))]
    counter = 0
    results_final = []
    for file in folder_names:
        counter += 1
        if counter % 10 == 0:
            print(f"Finished computation: {counter} / {len(folder_names)}")
        msa_path = os.path.abspath(os.path.join(raw_path, file, file + "_msa.fasta"))
        tree_path = os.path.abspath(os.path.join(raw_path, file, file + ".newick"))
        model_path = os.path.abspath(os.path.join(raw_path, file, file + "_model.txt"))

        os.chdir(os.path.join(os.path.pardir, "data", "processed", "features"))
        extractor = FeatureExtractor(msa_path, tree_path, model_path, file, "raxml-ng", True)

        features = extractor.extract_features()
        results_final.append(features)
        if counter == 2:
            break
    results_final_df = pd.concat(results_final)
    results_final_df = results_final_df.reset_index(drop=True)
    results_final_df.to_csv(os.path.join(os.path.pardir, "data", "processed", "features"))