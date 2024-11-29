import kagglehub

# Download latest version
path = kagglehub.dataset_download("uciml/german-credit")

print("Path to dataset files:", path)
input()
