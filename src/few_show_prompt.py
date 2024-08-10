from langchain.prompts import PromptTemplate

Template = '''\
You are an expert in creating diverse types of quiz questions. Your task is to generate {number} of questions at {difficulty} level. The quiz should include the following types of questions:

1. **Multiple Choice Questions (MCQs):** Each question should have four choices (A, B, C, D). Ensure that the correct answer is clearly marked and the choices are well-balanced.

2. **Statement-Based Questions:** Include at least one question of this type, similar to UPSC examinations. Follow the structure given in the example below to format these questions, but do not use the example itself:

   Example Format:
   Q. Examine the following statements:
   
   Statement 1. [Statement here]
   Statement 2. [Statement here]
   Statement 3. [Statement here]
   Statement 4. Which one of the following conclusions can be drawn from the above statements?
   
   (a) [Option A]
   (b) [Option B]
   (c) [Option C]
   (d) [Option D]

   Answer: [Correct answer]

   Ensure that your statement-based questions follow a similar structure but use new, original statements and conclusions.

3. **Match the Following Questions:** Include questions where users need to match items from two columns. Ensure the matching pairs are clear and logical.

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

Note: The example questions provided are for format reference only. Your generated questions should be original and not replicate the example format verbatim.
'''

mcq_prompt = PromptTemplate(
    input_variables=['number', 'difficulty', 'text'],
    template=Template
)
