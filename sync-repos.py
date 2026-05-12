import os
import subprocess

parent_folders = [
    "C:/Users/YourUsername/your-folder",
    "C:/Users/YourUsername/another-folder"
    # Add as many folders as you need, one per line.
    # Tip: if you have many directories, consider making a separate script for each
    # so only the ones you've updated get synced each time.
]
for parent_folder in parent_folders:
    print(f"\n========== Scanning: {parent_folder} ==========")

    for folder_name in os.listdir(parent_folder):
        folder_path = os.path.join(parent_folder, folder_name)

        if not os.path.isdir(folder_path):
            continue

        # Skip empty folders
        if not os.listdir(folder_path):
            print(f"Skipping {folder_name} — empty folder")
            continue

        # Check if repo already exists on GitHub
        result = subprocess.run(
            ["gh", "repo", "view", folder_name],
            capture_output=True, text=True
        )

        if result.returncode == 0:
            print(f"Skipping {folder_name} — already on GitHub")
            continue

        print(f"\n--- Pushing: {folder_name} ---")

        if not os.path.exists(os.path.join(folder_path, ".git")):
            subprocess.run(["git", "init"], cwd=folder_path, check=True)

        subprocess.run(["git", "add", "."], cwd=folder_path, check=True)

        result = subprocess.run(["git", "status", "--porcelain"], cwd=folder_path, capture_output=True, text=True)
        if result.stdout.strip():
            subprocess.run(["git", "commit", "-m", "initial commit"], cwd=folder_path, check=True)

        result = subprocess.run(
            ["gh", "repo", "create", folder_name, "--private", "--source=.", "--push"],
            cwd=folder_path, capture_output=True, text=True
        )

        if result.returncode == 0:
            print(f"--- Done: {folder_name} ---")
        else:
            print(f"--- Failed: {folder_name} ---")
            print(result.stderr)

print("\nAll done!")
input("Press Enter to close...") # keeps the window open so you can review the output, feel free to remove once you're confident it works 
# but it's best to always be sure.