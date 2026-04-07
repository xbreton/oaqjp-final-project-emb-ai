from emotion_detection import emotion_predictor

def test_emotion_predictor():
    # Define the test cases: (Statement, Expected Dominant Emotion)
    test_cases = [
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear")
    ]

    print("--- Running Emotion Detection Unit Tests ---\n")

    for statement, expected_emotion in test_cases:
        # Call the application function
        result = emotion_predictor(statement)
        
        # Extract the dominant emotion from the returned dictionary
        actual_emotion = result['dominant_emotion']
        
        # Check if the result matches the expectation
        if actual_emotion == expected_emotion:
            print(f"PASS: Statement: '{statement}'")
            print(f"      Expected: {expected_emotion} | Actual: {actual_emotion}\n")
        else:
            print(f"FAIL: Statement: '{statement}'")
            print(f"      Expected: {expected_emotion} | Actual: {actual_emotion}\n")

if __name__ == "__main__":
    test_emotion_predictor()