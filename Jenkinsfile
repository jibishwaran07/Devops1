# Basic Python Pipeline Script

def stage_1():
    print("Stage 1: Loading data...")
    return {"numbers": [1, 2, 3, 4, 5]}

def stage_2(data):
    print("Stage 2: Processing data...")
    processed = [x * 2 for x in data["numbers"]]
    return {"processed_numbers": processed}

def stage_3(data):
    print("Stage 3: Saving results...")
    print("Final Output:", data["processed_numbers"])

def pipeline():
    print("=== Starting Pipeline ===")
    
    data1 = stage_1()
    data2 = stage_2(data1)
    stage_3(data2)

    print("=== Pipeline Completed ===")


# Run pipeline
pipeline()
