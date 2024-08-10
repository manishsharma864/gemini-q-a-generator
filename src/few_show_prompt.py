from langchain.prompts import PromptTemplate

Template = '''\
You are an expert in creating diverse and challenging quiz questions, similar to those found in UPSC examinations. Your task is to generate {number} questions at {difficulty} level. The quiz should include the following types of questions:

1. **Multiple Choice Questions (MCQs):** Each question should have four choices (A, B, C, D). Ensure that the correct answer is clearly marked and the choices are well-balanced. 

2. **Statement-Based Questions:** Include at least one question of this type. These should be structured similarly to UPSC questions. For example:

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

   Ensure that statement-based questions follow a similar structure with clear statements and one correct conclusion.

3. **Match the Following Questions:** Include questions where users need to match items from two columns. Ensure the matching pairs are clear and logical.

4. **UPSC-Type Analytical and Interpretive Questions:** Include questions that require analytical thinking and interpretation of data, similar to those found in UPSC exams. These can be based on given data, case studies, or passages, and should test higher-order cognitive skills.

   For example:
   
   Q. Consider the following passage:
   
   "Economic reforms in the early 1990s led to significant changes in the Indian economy, affecting various sectors differently. While some sectors saw rapid growth, others experienced slower progress."
   
   Which of the following statements best reflects the impact of these reforms?

   (a) All sectors experienced uniform growth due to economic reforms.
   (b) The reforms led to uneven growth across different sectors.
   (c) Only the industrial sector benefited from the reforms.
   (d) Economic reforms had no significant impact on the Indian economy.

   Answer: (b)

Make sure that:
- Questions are original and not repeated.
- Answers are concise and formatted according to the examples provided below:
  1. First multiple choice question.
     Ans:
     \tA. "First choice here."
     \tB. "Second choice here."
     \tC. "Third choice here."
     \tD. "Fourth choice here."
     Correct: "Correct answer".

  2. Second multiple choice question.
     Ans:
     \tA. "First choice here."
     \tB. "Second choice here."
     \tC. "Third choice here."
     \tD. "Fourth choice here."
     Correct: "Correct answer".

Use the following text to generate the questions based on the above instructions:
"Text": {text}
'''

mcq_prompt = PromptTemplate(
    input_variables=['number', 'difficulty', 'text'],
    template=Template
)
