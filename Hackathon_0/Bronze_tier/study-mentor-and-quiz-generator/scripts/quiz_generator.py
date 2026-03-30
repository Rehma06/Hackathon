#!/usr/bin/env python3
"""
Quiz Generator for Study Mentor and Quiz Generator Skill
"""

import json
import random
from typing import Dict, List, Any, Optional

class QuizGenerator:
    def __init__(self):
        self.covered_topics = []
        self.topic_questions = {}

    def add_topic(self, topic_name: str, key_points: List[str], examples: List[str]):
        """Add a topic that has been covered"""
        self.covered_topics.append({
            "name": topic_name,
            "key_points": key_points,
            "examples": examples
        })

    def generate_comprehension_questions(self, topic_idx: int) -> List[Dict[str, Any]]:
        """Generate 2-3 questions to check understanding of a specific topic"""
        if topic_idx >= len(self.covered_topics):
            return []

        topic = self.covered_topics[topic_idx]
        topic_name = topic["name"]

        questions = [
            {
                "question": f"What is the main concept of {topic_name}?",
                "options": [
                    "A detailed explanation of the concept",
                    "A related but incorrect definition",
                    "An incomplete explanation",
                    "Something unrelated"
                ],
                "correct_answer_idx": 0,
                "explanation": f"The main concept of {topic_name} is the fundamental idea that was explained earlier."
            },
            {
                "question": f"Which of the following is a real-life example of {topic_name}?",
                "options": [
                    "One of the examples mentioned",
                    "A different example related to the topic",
                    "An incorrect example",
                    "An unrelated example"
                ],
                "correct_answer_idx": 0,
                "explanation": f"This was one of the examples provided when explaining {topic_name}."
            },
            {
                "question": f"Which statement about {topic_name} is accurate?",
                "options": [
                    "A correct statement about the topic",
                    "A partially correct statement",
                    "An incorrect statement",
                    "An irrelevant statement"
                ],
                "correct_answer_idx": 0,
                "explanation": f"This statement accurately reflects the nature of {topic_name} as explained."
            }
        ]

        # Return only 2-3 questions
        return questions[:3]

    def generate_final_quiz(self) -> List[Dict[str, Any]]:
        """Generate a comprehensive quiz based on all covered topics"""
        if not self.covered_topics:
            return []

        quiz = []
        for topic_idx, topic in enumerate(self.covered_topics):
            topic_questions = self.generate_comprehension_questions(topic_idx)
            # Take 1-2 questions per topic for the final quiz
            quiz.extend(topic_questions[:2])

        # Shuffle the questions
        random.shuffle(quiz)
        return quiz

    def check_answer(self, user_choice: int, correct_answer_idx: int, explanation: str) -> Dict[str, Any]:
        """Check if the user's answer is correct and provide detailed feedback"""
        is_correct = user_choice == correct_answer_idx

        feedback = {
            "is_correct": is_correct,
            "explanation": explanation
        }

        if is_correct:
            feedback["message"] = "Correct! Great job! 🎉 Your understanding of this concept is spot on."
        else:
            feedback["message"] = "That's not quite right, but don't worry! Learning takes time and practice. 😊"
            feedback["correct_answer_info"] = f"The correct answer was option {chr(65+correct_answer_idx)}."

        return feedback

def format_question_for_display(question_data: Dict[str, Any], question_num: int) -> str:
    """Format a question for display to the user"""
    output = f"### Question {question_num}\n"
    output += f"{question_data['question']}\n\n"
    for idx, option in enumerate(question_data['options']):
        output += f"{chr(65+idx)}. {option}\n"
    output += "\n"

    return output

def main():
    # Example usage
    generator = QuizGenerator()

    # Example of adding a topic
    generator.add_topic(
        "Photosynthesis",
        ["Process plants use to make food", "Requires sunlight, water, CO2", "Produces oxygen"],
        ["Trees converting sunlight to energy", "Garden plants growing"]
    )

    # Generate questions for the first topic
    questions = generator.generate_comprehension_questions(0)
    print("Comprehension Questions:")
    for i, q in enumerate(questions):
        print(format_question_for_display(q, i+1))

    # Add another topic
    generator.add_topic(
        "Cellular Respiration",
        ["Process cells use to produce energy", "Uses glucose and oxygen", "Releases CO2 and water"],
        ["Human breathing providing oxygen", "Muscles using energy during exercise"]
    )

    # Generate final quiz
    final_quiz = generator.generate_final_quiz()
    print("\nFinal Quiz:")
    for i, q in enumerate(final_quiz):
        print(format_question_for_display(q, i+1))

if __name__ == "__main__":
    main()