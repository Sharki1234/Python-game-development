full = [] 
    
def get_questions():
    file = open("23.05.2025\practice.txt","r")
    
    data = file.readlines()

    print(data)
    for datum in data:
        q = datum.split(",")
        print(q)
        question = q[0]
        options = []
        for i in range(1,5):
            options.append(q[i])
        print(options)
        answer = int(q[5])
        dict = {
            "question":question,
            "options":options,
            "answer":options[answer-1]
        }
        full.append(dict)

    print(full)
    file.close()
get_questions
