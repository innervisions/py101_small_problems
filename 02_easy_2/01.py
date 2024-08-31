# 01 - Welcome Stranger
def greetings(names: list, credentials: dict) -> str:
    return (
        f"Hello, {' '.join(names)}! "
        f"Nice to have a {credentials['title']} "
        f"{credentials['occupation']} around."
    )


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.
