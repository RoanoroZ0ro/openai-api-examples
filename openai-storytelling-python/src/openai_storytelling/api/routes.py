from flask import Blueprint, request, jsonify, current_app
import os
from ..services.openai_service import OpenAIService

api = Blueprint('api', __name__)

# read key from environment
_openai_key = os.getenv("OPENAI_API_KEY")
if not _openai_key:
    raise RuntimeError("OPENAI_API_KEY environment variable is required")

openai_service = OpenAIService(api_key=_openai_key)

@api.route('/stories', methods=['POST'])
def create_story():
    data = request.json
    title = data.get('title')
    content = data.get('content')
    author = data.get('author')
    
    if not title or not content or not author:
        return jsonify({'error': 'Title, content, and author are required.'}), 400
    
    story = openai_service.generate_story(title, content, author)
    return jsonify(story), 201

@api.route('/stories', methods=['GET'])
def get_stories():
    stories = openai_service.get_all_stories()
    return jsonify(stories), 200