"""
Unit tests for EmotionDetection package.
"""

from EmotionDetection import emotion_detector


def test_emotion(statement, expected_emotion):
    """
    Test whether dominant emotion matches expected emotion.
    """
    response = emotion_detector(statement)
    assert response["dominant_emotion"] == expected_emotion


if __name__ == "__main__":
    test_emotion("I am glad this happened", "joy")
    test_emotion("I am really mad about this", "anger")
    test_emotion("I feel disgusted just hearing about this", "disgust")
    test_emotion("I am so sad about this", "sadness")
    test_emotion("I am really afraid that this will happen", "fear")

    print("All tests passed successfully!")