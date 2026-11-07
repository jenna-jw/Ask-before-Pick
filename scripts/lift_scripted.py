# scripts/lift_scripted.py
import numpy as np
import robosuite as suite

env = suite.make(
    env_name="Lift",
    robots="Panda",
    has_renderer=True,
    has_offscreen_renderer=False,
    use_camera_obs=False,
    control_freq=20,
)

obs = env.reset()

def move_toward(eef, target, gripper, gain=10.0):
    action = np.zeros(env.action_dim)
    action[:3] = np.clip((target - eef) * gain, -1, 1)  # x, y, z 이동
    action[-1] = gripper                                 # -1: 열기, 1: 닫기
    return action

phases = ["큐브 위로 이동", "내려가기", "집기", "들어올리기"]
phase, phase_steps = 0, 0
print(f"[단계 0] {phases[0]}")

for step in range(500):
    eef = obs["robot0_eef_pos"]
    cube = obs["cube_pos"]

    if phase == 0:
        target = cube + np.array([0, 0, 0.10])
        a = move_toward(eef, target, -1)
        done_phase = np.linalg.norm(eef - target) < 0.01 or phase_steps > 100
    elif phase == 1:
        target = cube
        a = move_toward(eef, target, -1)
        done_phase = np.linalg.norm(eef - target) < 0.01 or phase_steps > 100
    elif phase == 2:
        a = move_toward(eef, cube, 1)
        done_phase = phase_steps > 20          # 그리퍼가 닫힐 시간
    else:
        target = cube + np.array([0, 0, 0.25])
        a = move_toward(eef, target, 1)
        done_phase = False

    if done_phase:
        phase += 1
        phase_steps = 0
        print(f"[단계 {phase}] {phases[phase]}")
    phase_steps += 1

    obs, reward, done, info = env.step(a)
    env.render()

print("성공 여부:", env._check_success())
env.close()