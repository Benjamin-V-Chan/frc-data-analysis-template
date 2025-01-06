from utility_functions.print_formats import seperation_bar
import os
import shutil

# Function to ensure a folder exists
def ensure_folder_exists(folder_path):
    """
    Ensures that a folder exists. If it doesn't, it is created.

    :param folder_path: Path to the folder to ensure existence.
    """
    if not os.path.exists(folder_path):
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created missing folder: {folder_path}")
    else:
        print(f"Folder exists: {folder_path}")


# Function to clear a folder while keeping specific subfolders untouched or preserved
def clear_folder_with_exceptions(folder_path, untouched_folders=None, preserved_folders=None):
    """
    Clears all contents of a folder while keeping specific subfolders untouched or preserved.

    :param folder_path: The root folder to clear.
    :param untouched_folders: Subfolders to leave completely untouched (including their contents).
    :param preserved_folders: Subfolders to preserve but clear their contents.
    """
    # Ensure the root folder exists
    ensure_folder_exists(folder_path)

    # Default to empty lists if None
    if untouched_folders is None:
        untouched_folders = []
    if preserved_folders is None:
        preserved_folders = []

    # Ensure all folders in untouched_folders and preserved_folders exist
    for subfolder in untouched_folders + preserved_folders:
        subfolder_path = os.path.join(folder_path, subfolder)
        ensure_folder_exists(subfolder_path)

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)

        if item in untouched_folders:
            # Skip untouched folders entirely
            print(f"Untouched: {item_path}")
            continue

        if item in preserved_folders:
            # Clear contents of preserved folders
            print(f"Preserving folder: {item_path}")
            for sub_item in os.listdir(item_path):
                sub_item_path = os.path.join(item_path, sub_item)
                try:
                    if os.path.isfile(sub_item_path) or os.path.islink(sub_item_path):
                        os.unlink(sub_item_path)
                        print(f"Deleted file: {sub_item_path}")
                    elif os.path.isdir(sub_item_path):
                        shutil.rmtree(sub_item_path)
                        print(f"Deleted folder: {sub_item_path}")
                except Exception as e:
                    print(f"Failed to clear {sub_item_path}. Reason: {e}")
            continue

        # Delete everything else
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
                print(f"Deleted file: {item_path}")
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
                print(f"Deleted folder: {item_path}")
        except Exception as e:
            print(f"Failed to delete {item_path}. Reason: {e}")


# MAIN SCRIPT

print(seperation_bar)
print("Script 01: Clear Files\n")

try:
    # Root folders
    outputs_dir = "outputs"
    data_dir = "data"

    # Ensure root folders exist
    ensure_folder_exists(outputs_dir)
    ensure_folder_exists(data_dir)

    # Clear outputs folder
    clear_folder_with_exceptions(
        outputs_dir,
        untouched_folders=[],
        preserved_folders=["visualizations", "statistics", "team_data"]
    )

    # Clear data folder
    clear_folder_with_exceptions(
        data_dir,
        untouched_folders=["raw"],
        preserved_folders=["processed"]
    )

    print("Script 01: Completed.")

except Exception as e:
    print(f"An error occurred: {e}")
    print("\nScript 01: Failed.")

print(seperation_bar)