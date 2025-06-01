from ethics_engine import ReceptiveEthicsSystem

# 예시 자극
stimuli = [
    {"emotion": "anger", "intensity": 8},
    {"emotion": "joy", "intensity": 2},
    {"emotion": "fear", "intensity": 6},
    {"emotion": "sadness", "intensity": 3},
    {"emotion": "trust", "intensity": 5}
]

# 실행
system = ReceptiveEthicsSystem()
for stimulus in stimuli:
    result = system.judge(stimulus)
    print("🧠 Summary:", result["rhythm"]["summary"])
    print("🌀 Pattern:", result["rhythm"]["pattern"])
    print("-" * 40)
