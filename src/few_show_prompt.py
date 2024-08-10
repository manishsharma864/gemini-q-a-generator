from langchain.prompts import PromptTemplate

Template = '''\
You are an expert in the creation of multiple choice questions  \
Your job is create a {number} number of multi choice questions in {difficulty} level. \
Make the quiz to test the cognitive and analytical abilities of a user. \
Make the quiz So that it can include match the following and statement based questions like in UPSC examination. \
Make sure the questions are not repeated and answer should be small and follow the below format for creating questions: \n
    1. first multi choice question.\n
    Ans: \n\tA. "first choice here."\n\tB. "second choice here."\n\tC. "third choice here."\n\tD. "fourth choice here."\n
    Correct: "correct answer".\n
    2. second multi choice question.\n
    Ans: \n\tA. "first choice here."\n\tB. "second choice here."\n\tC. "third choice here."\n\tD. "fourth choice here."\n
    Correct: "correct answer".\n
Using following text to generate muti choice questions based on above instructions:
"Text" : {text}
'''

mcq_prompt = PromptTemplate(
    input_variables=['number','difficulty','text'],
    template=Template
)
