# Directory Bookmarking Tool

This set of shell functions provides a simple yet effective way to bookmark directories in your shell environment. You can easily save frequently accessed directories and navigate to them using short, memorable commands. This tool aims to streamline your workflow by minimizing the need to type or remember lengthy directory paths.

## Features

- `cdadd`: Bookmark the current or specified directory with an auto-incremented index.
- `cdgo`: Navigate to a directory associated with a given bookmark index.
- `cdlist`: List all saved bookmarks with their indices and provide functionality to delete any bookmark.

## Getting Started

### Installation

1. Open your shell configuration file (e.g., `~/.bashrc` for Bash or `~/.zshrc` for Zsh).
2. Copy and paste the functions for `cdadd`, `cdgo`, and `cdlist` into the file.
3. Save the file and reload your shell configuration:

    ```sh
    source ~/.bashrc  # or source ~/.zshrc
    ```

### Usage

#### Adding Bookmarks

- To bookmark the current directory:

    ```sh
    cdadd
    ```

- To bookmark a specific directory:

    ```sh
    cdadd /path/to/directory
    ```

#### Navigating to Bookmarked Directories

- To navigate to a bookmarked directory by its index:

    ```sh
    cdgo <index>
    ```

#### Managing Bookmarks

- To list all bookmarks:

    ```sh
    cdlist
    ```

- To delete a bookmark by its index:

    ```sh
    cdlist -d <index>
    ```
