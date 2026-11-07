## Setup (Windows)
python -m venv robot-env
source robot-env/Scripts/activate
pip install -r requirements.txt
cp robot-env/Lib/site-packages/mujoco/mujoco.dll robot-env/Lib/site-packages/robosuite/utils/

- Python 3.13 사용 시 numpy>=2 로 설치해야 소스 빌드 에러를 피할 수 있음
- robosuite 1.5.1은 mujoco 3.3.x 사용 (4.0은 호환 안 될 수 있음)

## Progress
- [x] 환경 설치 및 시뮬레이터 실행
- [x] Lift: 스크립트로 큐브 집어 올리기 성공
- [ ] PickPlace: 이름으로 지정한 물체 집기
- [ ] LLM 명령 해석 (되묻기 포함)
- [ ] 명령 테스트셋 평가 및 실패 분석