# Receptive Ethics Framework – Full Python Implementation
# By Yeo Gwan-Yeong (2025)
# Licensed under CC BY-NC-SA 4.0
# Structure: SENSE → SUSPEND → CALIBRATE → RHYTHMIZE → JUDGE

from typing import List, Dict, Any

class ReceptiveEthicsSystem:
    def __init__(self):
        self.history: List[Dict[str, Any]] = []
        self.rhythm_memory: List[str] = []

    def sense(self, stimulus: Dict[str, Any]) -> Dict[str, Any]:
        return {
            "emotion": stimulus.get("emotion", "neutral"),
            "intensity": stimulus.get("intensity", 0)
        }

    def suspend(self, emotional_data: Dict[str, Any]) -> Dict[str, Any]:
        if emotional_data["intensity"] > 5:
            return {"paused": True, "reason": "High emotional intensity"}
        return {"paused": False}

    def calibrate(self, emotional_data: Dict[str, Any], pause_info: Dict[str, Any]) -> Dict[str, Any]:
        if pause_info["paused"]:
            return {"calibrated": True, "value": f"Careful processing of '{emotional_data['emotion']}'"}
        else:
            return {"calibrated": True, "value": f"Routine processing of '{emotional_data['emotion']}'"}

    def rhythmize(self, calibration_result: Dict[str, Any]) -> Dict[str, Any]:
        self.rhythm_memory.append(calibration_result["value"])
        pattern = self.rhythm_memory[-3:] if len(self.rhythm_memory) > 5 else self.rhythm_memory
        return {
            "pattern": pattern,
            "summary": f"Judgment shaped by {len(pattern)} recent patterns."
        }

    def judge(self, stimulus: Dict[str, Any]) -> Dict[str, Any]:
        sensed = self.sense(stimulus)
        paused = self.suspend(sensed)
        calibrated = self.calibrate(sensed, paused)
        rhythm = self.rhythmize(calibrated)

        result = {
            "stimulus": stimulus,
            "pause": paused,
            "calibration": calibrated,
            "rhythm": rhythm
        }

        self.history.append(result)
        return result


if __name__ == "__main__":
    system = ReceptiveEthicsSystem()
    stimuli = [
        {"emotion": "anger", "intensity": 8},
        {"emotion": "joy", "intensity": 3},
        {"emotion": "fear", "intensity": 6},
        {"emotion": "sadness", "intensity": 2},
        {"emotion": "trust", "intensity": 4},
        {"emotion": "anger", "intensity": 5}
    ]

    for s in stimuli:
        result = system.judge(s)
        print("Judgment Summary:", result["rhythm"]["summary"])
        print("Detailed Pattern:", result["rhythm"]["pattern"])
        print("-" * 40)
