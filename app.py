import os
from flask import Flask, request, jsonify, render_template
from typing import List, Dict
import pandas as pd
from dataclasses import dataclass
from datetime import datetime

app = Flask(__name__)

# Thêm config cho production
if os.environ.get('RENDER'):
    app.config.update(
        SESSION_COOKIE_SECURE=True,
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='Lax',
    )

@dataclass
class Student:
    name: str
    elo: int
    knowledge_level: str

@dataclass
class Lesson:
    name: str
    level: str
    lesson_type: str
    required_elo: int
    lesson_url: str = ''

def load_lessons() -> pd.DataFrame:
    """Load lessons from CSV file"""
    return pd.read_csv('lessons.csv', skiprows=1, names=[
        'index', 'name', 'level', 'lesson_type', 'required_elo', 'lesson_url'
    ]).dropna()

def filter_lessons(student: Student, lessons_df: pd.DataFrame) -> Dict[str, List[Dict]]:
    """Filter lessons based on student's level and ELO"""
    filtered_lessons = lessons_df[
        (lessons_df['level'] == student.knowledge_level) & 
        (lessons_df['required_elo'] >= student.elo)
    ]
    
    lesson_categories = {
        'chiến lược': [],
        'chiến thuật': [],
        'cờ tàn': [],
        'extra': [],
        'motif chiếu hết': []
    }

    for _, lesson in filtered_lessons.iterrows():
        category = lesson['lesson_type'].lower()
        if category in lesson_categories:
            lesson_categories[category].append({
                'name': lesson['name'],
                'lesson_url': lesson['lesson_url']
            })

    return lesson_categories

@app.route('/', methods=['GET'])
def index():
    valid_levels = [
        "Found A", "Found B", "Found C",
        "Intermediate A", "Intermediate B", "Intermediate C",
        "Advance A", "Advance B", "Advance C", "Master"
    ]
    return render_template('index.html', levels=valid_levels, datetime=datetime)

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    """Generate lesson plan for a student"""
    try:
        student = Student(
            name=request.form['name'],
            elo=int(request.form['elo']),
            knowledge_level=request.form['knowledge_level']
        )

        valid_levels = [
            "Found A", "Found B", "Found C",
            "Intermediate A", "Intermediate B", "Intermediate C",
            "Advance A", "Advance B", "Advance C", "Master"
        ]
        
        if student.knowledge_level not in valid_levels:
            return render_template('index.html', 
                                error='Trình độ không hợp lệ',
                                levels=valid_levels)

        lessons_df = load_lessons()
        lesson_plan = filter_lessons(student, lessons_df)

        return render_template('index.html',
                            student=student,
                            lesson_plan=lesson_plan,
                            levels=valid_levels,
                            datetime=datetime)

    except Exception as e:
        return render_template('index.html',
                            error=str(e),
                            levels=valid_levels)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=True) 