# Candidate Interview Summary Generator

## Overview

The Candidate Interview Summary Generator is a Python-based application that automatically generates concise interview summaries from interview transcripts. The system analyzes the transcript and extracts key information such as skills discussed, candidate strengths, and areas for improvement.

## Objective

To automate the process of summarizing interview discussions and provide recruiters or interviewers with a concise overview of candidate performance.

## Features

* Extracts technical skills mentioned in the interview.
* Identifies candidate strengths.
* Identifies areas for improvement.
* Generates concise and informative summaries.
* Outputs results in JSON format.
* Handles long interview transcripts efficiently.
* Reduces repetition in generated summaries.

## Project Structure

```text
Candidate_Interview_Summary_Generator
│
├── summary_generator.py
├── sample_transcript.txt
└── README.md
```

## Technologies Used

### Programming Language

* Python 3.8+

### Development Tools

* Visual Studio Code (VS Code)
* Git
* GitHub

### Python Libraries

* json (for JSON output generation)

## How to Run

1. Open the project folder.
2. Add the interview transcript to `sample_transcript.txt`.
3. Run the following command:

```bash
python summary_generator.py
```

## Sample Input

```text
Interviewer: What programming languages do you know?

Candidate: I know Python, Java, and SQL.

Interviewer: What are your strengths?

Candidate: My strengths are problem solving and teamwork.

Interviewer: What would you like to improve?

Candidate: I would like to improve my communication skills.
```

## Sample Output

```json
{
    "summary": "Candidate demonstrated knowledge of Python, Java, SQL. Key strengths include Problem Solving, Teamwork. Areas for improvement include Communication Skills."
}
```

## Results

The application successfully extracts relevant information from interview transcripts and generates concise summaries. It provides a structured overview of candidate performance, making interview evaluation faster and more efficient.

## Future Enhancements

* Natural Language Processing (NLP) integration.
* Support for multiple transcript formats.
* Web-based user interface.
* AI-powered summary generation.
* Export summaries to PDF and Excel formats.

## Author

Srihitha Alli

AI & ML Internship Project
