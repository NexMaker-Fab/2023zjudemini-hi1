import json

# Function to calculate relative difference (as a percentage)
def calculate_relative_difference(baseline, current):
    if baseline == 0:
        return 0
    return  abs(current - baseline) 

# Function to calculate distance
def calculate_distance(point1, point2):
    return ((point1["x"] - point2["x"])**2 + (point1["y"] - point2["y"])**2)**0.5

def analyze_posture(baseline_data, current_data):
    mode = 'abs'
    # Load data from JSON
    if type(baseline_data) is not dict:
        # print(type(baseline_data))
        baseline_data = json.loads(baseline_data)
    if type(current_data) is not dict:
        # print(type(current_data))
        current_data = json.loads(current_data)

    # Calculate baseline measurements
    baseline_head_tilt = abs(baseline_data["left_eye"]["y"] - baseline_data["right_eye"]["y"])
    baseline_body_tilt = abs(baseline_data["left_shoulder"]["y"] - baseline_data["right_shoulder"]["y"])
    baseline_nose_shoulder_distance = (calculate_distance(baseline_data["nose"], baseline_data["left_shoulder"]) + calculate_distance(baseline_data["nose"], baseline_data["right_shoulder"])) / 2
    print('=========baseline data=========')
    # print(baseline_head_tilt)
    print(baseline_body_tilt)
    # print(baseline_nose_shoulder_distance)
    print('===============================')
    # Calculate current measurements
    current_head_tilt = abs(current_data["left_eye"]["y"] - current_data["right_eye"]["y"])
    current_body_tilt = abs(current_data["left_shoulder"]["y"] - current_data["right_shoulder"]["y"])
    current_nose_shoulder_distance = (calculate_distance(current_data["nose"], current_data["left_shoulder"]) + calculate_distance(current_data["nose"], current_data["right_shoulder"])) / 2
    print('AAAAAA     current data     AAAAAA')
    print(current_head_tilt)
    print(abs(current_body_tilt-baseline_body_tilt))
    # print(current_nose  _shoulder_distance)
    print(current_body_tilt)
    print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    # Calculate deviations from baseline
    head_tilt_deviation = calculate_relative_difference(baseline_head_tilt, current_head_tilt)
    body_tilt_deviation = calculate_relative_difference(baseline_body_tilt, current_body_tilt)
    
    nose_shoulder_deviation = calculate_relative_difference(baseline_nose_shoulder_distance, current_nose_shoulder_distance)

    # Thresholds for deviations
    HEAD_TILT_DEVIATION_THRESHOLD = 12  # Example threshold
    BODY_TILT_DEVIATION_THRESHOLD = 20  # Example threshold
    NOSE_SHOULDER_DEVIATION_THRESHOLD = 20  # Example threshold
    # print('---------------------------------')
    # print(head_tilt_deviation)
    # print(body_tilt_deviation)
    # print(nose_shoulder_deviation)
    # print('---------------------------------')
    # Analyzing the posture
    if mode == 'realative':
        is_head_tilted = head_tilt_deviation > HEAD_TILT_DEVIATION_THRESHOLD
        is_body_tilted = body_tilt_deviation > BODY_TILT_DEVIATION_THRESHOLD
        is_nose_shoulder_distance_normal = nose_shoulder_deviation < NOSE_SHOULDER_DEVIATION_THRESHOLD
    if mode == 'abs':
        is_head_tilted = current_head_tilt > HEAD_TILT_DEVIATION_THRESHOLD
        is_body_tilted =  abs(current_body_tilt-baseline_body_tilt) > BODY_TILT_DEVIATION_THRESHOLD
        is_nose_shoulder_distance_normal = current_nose_shoulder_distance < NOSE_SHOULDER_DEVIATION_THRESHOLD
    # Return results
    return {
        "head_tilt": is_head_tilted,
        "body_tilt": is_body_tilted,
        "nose_shoulder_distance_normal": is_nose_shoulder_distance_normal
    }

# Example usage
baseline_data_example = '''{
    "nose": {"x": 500, "y": 250},
    "left_eye": {"x": 550, "y": 200},
    "right_eye": {"x": 590, "y": 205},
    "left_shoulder": {"x": 450, "y": 350},
    "right_shoulder": {"x": 640, "y": 360}
}'''

current_data_example = '''{
    "nose": {"x": 500, "y": 300},
    "left_eye": {"x": 550, "y": 245},
    "right_eye": {"x": 590, "y": 250},
    "left_shoulder": {"x": 450, "y": 400},
    "right_shoulder": {"x": 640, "y": 410}
}'''

# Analyze posture
posture_analysis = analyze_posture(baseline_data_example, current_data_example)
print(posture_analysis)
