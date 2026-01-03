# Text Analyzer

This project is a simple Python script that reads a text file and
returns:

-   Total word count\
-   Total sentence count\
-   Top 10 most frequent words (ignoring punctuation and numbers)

The script processes the text in lowercase and removes punctuation
before counting.

------------------------------------------------------------------------

## 📂 Files

-   `main.py` --- main script\
-   `sample_text.txt` --- input text file\
-   `requirements.txt` --- project dependencies (none required)

------------------------------------------------------------------------

## ▶️ How to Run

Make sure you have Python installed, then run:

    python main.py

The script will automatically read `sample_text.txt` and print the
results.

------------------------------------------------------------------------

## 🧪 Example Output

    Words count: 245
    Sentences count: 18
    Top 10 words:
    ai 12
    the 9
    to 8
    and 7
    we 5
    is 5
    repeat 4
    tools 4
    are 3
    apps 3

*(values may differ depending on the text)*

------------------------------------------------------------------------

## ✔️ Notes

-   Numbers are ignored when counting words\
-   Punctuation is removed\
-   Text is processed in lowercase
