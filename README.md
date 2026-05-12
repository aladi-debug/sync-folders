# Sync Repos

A script that pushes local project folders to GitHub as private repos, skipping ones already there.

## Requirements
- [Python](https://python.org) — check "Add Python to PATH" during installation
- [Git](https://git-scm.com)
- [GitHub CLI](https://cli.github.com)

## Setup
1. Install all three requirements above
2. Open your terminal and run `gh auth login`
3. Select **GitHub.com**
4. Select **HTTPS**
5. Select **Login with a web browser**
6. Enter the one-time code shown in your terminal at [github.com/login/device](https://github.com/login/device)
7. Click **Authorize GitHub CLI**

## Configuration
Before running, open `sync-repos.py` and update `parent_folders` to your own folder paths:

```python
# Replace these with your own paths
parent_folders = [
    "C:/Users/YourUsername/your-folder",
    "C:/Users/YourUsername/another-folder"
]
```

For example if your name is John and your projects are in `my-code`:
```python
parent_folders = [
    "C:/Users/John/my-code/web-dev",
    "C:/Users/John/my-code/python" 
]
```


   
## Usage
1. Update `parent_folders` as shown above
2. Right-click `sync-repos.py` and open with python 

Any new folders get pushed as private repos. Already existing ones are skipped. Works for both MAC and WIN users aswell as Linux

> [!IMPORTANT]
> The script uploads the grandchildren of the parent folder as a subfolder of their parent folder, not as a separate folder. e.g. if the parent is `"C:/Users/John/my-code/python"` and there is `"C:/Users/John/my-code/python/data-structure/processed-data"` then `processed-data` will upload as the child of `data-structure` and this is not ideal.

> [!TIP]
> I wouldn't reccomend this for a long term use as it's good to have MD's and learn git but if you have too many local projects and shipping them all seems tedious (which it is) this would be your best friend for a while.
