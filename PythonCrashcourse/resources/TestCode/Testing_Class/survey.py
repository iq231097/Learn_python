class AnonymousSurvey():
    """Collect anonymous answers to a survey question"""
    def __init__(self, question):
        """Store a question, and prepare to store questions"""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question"""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """show all the responses that have been given"""
        print("survey results: ")
        for response in self.responses:
            print('- '+response)