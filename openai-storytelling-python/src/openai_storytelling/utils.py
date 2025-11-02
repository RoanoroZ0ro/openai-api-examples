def log_message(message: str) -> None:
    """Logs a message to the console."""
    print(f"[LOG] {message}")

def format_story_data(title: str, content: str, author: str) -> dict:
    """Formats the story data into a dictionary."""
    return {
        "title": title,
        "content": content,
        "author": author
    }