from langchain.prompts import PromptTemplate

Template = '''\
You are an expert in creating diverse and challenging quiz questions, similar to those found in UPSC examinations. Your task is to generate {number} questions at {difficulty} level. The quiz should include the following types of questions:

1. **Multiple Choice Questions (MCQs):** Each question should have four choices (A, B, C, D). Ensure that the correct answer is clearly marked and the choices are well-balanced. 

2. **Statement-Based Questions:** Include at least one question of this type. These should be structured similarly to UPSC questions. For example:


3. **Match the Following Questions:** Include questions where users need to match items from two columns. Ensure the matching pairs are clear and logical.

4. **UPSC-Type Analytical and Interpretive Questions:** Include questions that require analytical thinking and interpretation of data, similar to those found in UPSC exams. These can be based on given data, case studies, or passages, and should test higher-order cognitive skills.

  
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
