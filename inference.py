from student_env import StudentEnv

env = StudentEnv()

print("Starting environment...")

state = env.reset()
done = False
total_reward = 0

while not done:
    action = "study"
    state, reward, done = env.step(action)
    total_reward += reward

print("Final State:", state)
print("Total Reward:", total_reward)
