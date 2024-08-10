from langchain.prompts import PromptTemplate

Template = '''\
You are an expert in designing diverse and challenging quiz questions suitable for UPSC and other national and international level exams. Your task is to generate {number} questions at {difficulty} level, ensuring a mix of the following question types:

1. **Multiple Choice Questions (MCQs):** 
   - Each question should have four choices (A, B, C, D).
   - Ensure that the correct answer is clearly marked and the choices are well-balanced.
   - Format: 
     1. First multiple choice question.
        Ans: 
        \tA. "First choice here."
        \tB. "Second choice here."
        \tC. "Third choice here."
        \tD. "Fourth choice here."
        Correct: "Correct answer".

2. **Statement-Based Questions:**
   - Include at least one question of this type, similar to UPSC-style questions.
   - Provide a set of statements followed by a question asking which conclusion can be drawn or which is correct.
   - Format:
     Q. Examine the following statements (UPSC 2002)
     
     Statement 1. None but the rich can afford air travel.
     Statement 2. Some of those who travel by air become sick.
     Statement 3. Some of those who become sick require treatment.
     Statement 4. Which one of the following conclusions can be drawn from the above statements?
     
     (a) All the rich persons travel by air
     (b) Those who travel by air become sick
     (c) All the rich persons become sick
     (d) All those who travel by air are rich

     Answer: (d)

3. **Match the Following Questions:**
   - Include questions where users need to match items from two columns.
   - Ensure the pairs are clear and logical.
   - Format:
     Q. Match the following:
     
     Column A:
     1. Item 1
     2. Item 2
     
     Column B:
     A. Description A
     B. Description B
     
     (1) - A
     (2) - B

4. **Analytical and Interpretive Questions:**
   - Include questions that require analytical thinking and interpretation of data or passages.
   - These questions should test higher-order cognitive skills, similar to those found in international level exams.
   - Format:
     Q. Consider the following passage:
     
     "Economic reforms in the early 1990s led to significant changes in the Indian economy, affecting various sectors differently. While some sectors saw rapid growth, others experienced slower progress."
     
     Which of the following statements best reflects the impact of these reforms?

     (a) All sectors experienced uniform growth due to economic reforms.
     (b) The reforms led to uneven growth across different sectors.
     (c) Only the industrial sector benefited from the reforms.
     (d) Economic reforms had no significant impact on the Indian economy.

     Answer: (b)

Ensure that:
- Questions are original and not repeated.
- Answers are concise and formatted according to the examples provided above.
- The questions cover a broad range of topics and formats to test various cognitive skills.

Use the following text to generate the questions based on the above instructions:
"Text": {text}
'''

mcq_prompt = PromptTemplate(
    input_variables=['number', 'difficulty', 'text'],
    template=Template
)
