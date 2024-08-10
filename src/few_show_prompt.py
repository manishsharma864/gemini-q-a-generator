from langchain.prompts import PromptTemplate

Template = '''\
You are an expert in the creation of multiple choice questions  \
Your job is create a {number} number of multi choice questions in {difficulty} level. \
Make the quiz to test the cognitive and analytical abilities of a user. \
Make the quiz So that it can include match the following and statement based questions like in UPSC examination there should be one statement based question. \
For example the statement based questions should be of example format.\
Q. Examine the following statements (UPSC 2002)\

1.None but the rich can afford air travel.\
2.Some of those who travel by air become sick.\
3.Some of those who become sick require treatment.\
4.Which one of the following conclusions can be drawn from the above statements?\

(a) All the rich persons travel by air\

(b) These who travel by air become sick\

(c) All the rich persons become sick\

(d) All those who travel by air are rich\

Answer: (d) \
This above is example for statement based questions.\
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
