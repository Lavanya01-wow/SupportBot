# Support Agent Chatbot for CDPs — How-To Questions

**Table of Contents**  
1. [Overview](#overview)  
2. [Data Sources](#data-sources)  
3. [Core Functionalities](#core-functionalities)  
4. [Bonus Features](#bonus-features)  
5. [Project Structure](#project-structure)  
6. [Installation & Setup](#installation--setup)  
7. [Usage](#usage)  
8. [Evaluation Criteria](#evaluation-criteria)  
9. [Future Improvements](#future-improvements)  
10. [License](#license)

---

## Overview
This project aims to develop a **Support Agent Chatbot** that can answer "how-to" questions related to four Customer Data Platforms (CDPs):
- [Segment](https://segment.com/docs/?ref=nav)
- [mParticle](https://docs.mparticle.com/)
- [Lytics](https://docs.lytics.com/)
- [Zeotap](https://docs.zeotap.com/home/en-us/)

The chatbot should:
1. Interpret user queries about how to perform tasks within each CDP.
2. Retrieve relevant information from the official documentation of these platforms.
3. Handle variations in how questions are phrased, including irrelevant questions.

## Data Sources
The chatbot uses information from the following documentation sites:
- **Segment** Documentation: [https://segment.com/docs/](https://segment.com/docs/?ref=nav)
- **mParticle** Documentation: [https://docs.mparticle.com/](https://docs.mparticle.com/)
- **Lytics** Documentation: [https://docs.lytics.com/](https://docs.lytics.com/)
- **Zeotap** Documentation: [https://docs.zeotap.com/home/en-us/](https://docs.zeotap.com/home/en-us/)

These resources contain the instructions and steps needed to answer "how-to" queries. The chatbot may utilize simple indexing, search APIs, or NLP-based methods to retrieve relevant information from these docs.

## Core Functionalities
1. **Answer "How-To" Questions**  
   - Users can ask platform-specific questions like:  
     - "How do I set up a new source in Segment?"  
     - "How can I create a user profile in mParticle?"  
     - "How do I build an audience segment in Lytics?"  
     - "How can I integrate my data with Zeotap?"  
   - The chatbot will search the respective documentation and return concise steps or guidance.

2. **Extract Information from Documentation**  
   - The chatbot indexes or accesses the official docs for Segment, mParticle, Lytics, and Zeotap.  
   - It then locates and extracts instructions, code snippets, or best practices relevant to the user’s query.

3. **Handle Variations in Questions**  
   - The chatbot should be resilient to different phrasings or question lengths.  
   - It should also handle completely irrelevant questions gracefully (e.g., "Which movie is getting released this week?").

## Bonus Features
1. **Cross-CDP Comparisons**  
   - The chatbot can address questions about differences or similarities in approaches across platforms, e.g., "How does Segment’s audience creation process compare to Lytics’?"

2. **Advanced "How-to" Questions**  
   - Provides guidance on advanced integrations or configurations, such as multi-account setups, debugging tips, or platform-specific deep dives.

## Project Structure
A typical project structure could look like this (adjust as needed based on your tech stack):
```
├── data/
│   ├── segment_docs/...
│   ├── mparticle_docs/...
│   ├── lytics_docs/...
│   └── zeotap_docs/...
├── src/
│   ├── chatbot.py (or chatbot.js)
│   ├── indexer.py (or indexer.js)
│   ├── parser.py (or parser.js)
│   └── ...
├── config/
│   └── settings.yaml (or .env, etc.)
├── tests/
│   └── test_chatbot.py
├── requirements.txt (or package.json)
├── README.md
└── LICENSE
```

**Key Components**:
- **Indexer/Parser**: Extracts and indexes relevant sections from the docs, or sets up a search approach (e.g., simple keyword-based or vector-based using an NLP library).  
- **Chatbot Core**: Processes user queries, matches them against indexed documentation, and returns formatted answers.  
- **Tests**: Contains test cases for question variations, cross-CDP comparisons, and irrelevant queries.

## Installation & Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/cdp-chatbot.git
   cd cdp-chatbot
   ```
2. **Install Dependencies**:
   - If using Python:
     ```bash
     pip install -r requirements.txt
     ```
   - If using Node.js:
     ```bash
     npm install
     ```
3. **Obtain Documentation**:
   - Option 1: **Scrape** or **download** relevant documentation pages as HTML/Markdown/PDF into the `data/` folder.  
   - Option 2: Use a **crawler or API** to retrieve data on demand.

4. **Configure Settings**:
   - In `config/settings.yaml` (or `.env`), specify paths to the data, indexing methods, or other configurations (e.g., your chosen search algorithm).

## Usage
1. **Run the Chatbot**:
   - Python Example:
     ```bash
     python chatbot.py
     ```
   - Node.js Example:
     ```bash
     node chatbot.js
     ```
2. **Ask Questions**:
   - **How-to** queries about any of the four CDPs.  
   - The chatbot will parse the question and look up the relevant steps in the documentation or indexed data.

3. **Cross-CDP Queries**:
   - Example: "Compare Segment’s source setup with mParticle’s."  
   - The chatbot should retrieve relevant info from both docs and present a concise comparison.

4. **Advanced Questions**:
   - Inquire about multi-step processes or complex use cases, e.g. "How do I set up real-time audience streaming from Segment to a data warehouse?"

## Evaluation Criteria
- **Accuracy & Completeness**: How well does the chatbot provide correct and complete answers from the docs?  
- **Code Quality & Build**: Is the code organized, maintainable, and well-documented?  
- **Question Handling**: Does the chatbot handle variations in phrasing, length, and irrelevant questions gracefully?  
- **Bonus Features**: 
  - Cross-CDP comparisons.  
  - Advanced configuration questions or complex use cases.  
- **User Experience**: Ease of interaction and clarity of the chatbot’s responses.


## License
This project is released under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as permitted by the license.

---

