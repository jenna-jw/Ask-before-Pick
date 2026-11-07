# AskBeforePick

> 모호한 자연어 명령을 받았을 때, 로봇이 맞는 물체를 고르거나 필요할 때 되묻는지를 시뮬레이션에서 평가하는 프로젝트

## Motivation

사람은 로봇에게 정확하게 말하지 않습니다. "마실 거 줘", "그거 저기 치워줘"처럼 모호한 명령을 받았을 때 로봇은 다음 중 하나를 해야 합니다.

- 명확한 경우: 맞는 물체를 골라 실행
- 모호한 경우: "우유와 캔 중 무엇인가요?"처럼 되묻기
- 불가능한 경우: 거절

이 프로젝트는 LLM 기반 명령 해석기가 **언제, 왜 틀리는지**를 측정하고 실패 유형을 분석하는 것을 목표로 합니다.

## Pipeline

| 구성 | 역할 | 파일 |
|---|---|---|
| 장면 | robosuite PickPlace 환경 (우유, 빵, 시리얼, 캔) | - |
| 두뇌 | LLM이 명령을 해석해 물체 선택 또는 되묻기 | `src/interpreter.py` |
| 손 | 선택된 물체를 집는 규칙 기반 실행기 | `src/executor.py` |
| 채점표 | 명령 테스트셋 평가 및 실패 분석 | `src/evaluate.py` |

## Project Structure

```
ask-before-pick/
├── scripts/          # 기능 테스트용 코드
├── src/              # 본 프로젝트 코드
├── data/             # 명령 테스트셋
├── results/          # 실험 결과
└── requirements.txt
```

## Setup (Windows)

```bash
python -m venv robot-env
source robot-env/Scripts/activate
pip install -r requirements.txt
cp robot-env/Lib/site-packages/mujoco/mujoco.dll robot-env/Lib/site-packages/robosuite/utils/
```

- Python 3.13 사용 시 `numpy>=2`로 설치해야 소스 빌드 에러를 피할 수 있음
- robosuite 1.5.1은 mujoco 3.3.x 사용 (4.0은 호환되지 않을 수 있음)
- Windows에서는 robosuite가 `mujoco.dll`을 찾지 못하는 문제가 있어 위 `cp` 명령이 필요함

## Quick Start

```bash
python scripts/lift_scripted.py
```

Lift 환경에서 로봇이 큐브를 집어 올리고 `성공 여부: True`를 출력합니다.

## Progress

- [x] 환경 설치 및 시뮬레이터 실행
- [x] Lift: 스크립트로 큐브 집어 올리기 성공
- [ ] PickPlace: 이름으로 지정한 물체 집기
- [ ] LLM 명령 해석 (되묻기 포함)
- [ ] 명령 테스트셋 평가 및 실패 분석