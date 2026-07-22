import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
from dataclasses import dataclass

class ForceLaw(ABC):
    @abstractmethod
    def acceleration(self, x: np.ndarray, v: np.ndarray, t: float) -> np.ndarray:
        pass

class Gravity(ForceLaw):
    def __init__(self, g: float = 9.81):
        self.g = g
    def acceleration(self, x: np.ndarray, v: np.ndarray, t: float) -> np.ndarray:
        return np.array([0.0, -self.g])


class SpringForce(ForceLaw):
    def __init__(self, k: float, x0: np.ndarray):
        self.k = k
        self.x0 = np.array(x0, dtype=float)
    def acceleration(self, x: np.ndarray, v: np.ndarray, t: float) -> np.ndarray:
        return -self.k * (x - self.x0)


class CombinedForce(ForceLaw):
    def __init__(self, forces):
        self.forces = forces    
    def acceleration(self, x: np.ndarray, v: np.ndarray, t: float) -> np.ndarray:
        a = np.zeros_like(x)
        for f in self.forces:
            a += f.acceleration(x, v, t)
        return a

@dataclass
class PointMass:
    m: float
    x: np.ndarray
    v: np.ndarray

class Simulator:
    def __init__(self, body: PointMass, force: ForceLaw):
        self.body = body
        self.force = force
        self.trajectory = [body.x.copy()]
    def step_euler(self, dt: float, t: float) -> None:
        a = self.force.acceleration(self.body.x, self.body.v, t)
        self.body.v = self.body.v + a * dt
        self.body.x = self.body.x + self.body.v * dt
        self.trajectory.append(self.body.x.copy())
    def run(self, dt: float, total_time: float) -> None:
        steps = int(total_time / dt)
        for i in range(steps):
            self.step_euler(dt, i * dt)    
    def get_trajectory(self) -> np.ndarray:
        return np.array(self.trajectory)

def plot_trajectory(sim: Simulator, title: str):
    traj = sim.get_trajectory()
    
    plt.figure(figsize=(8, 6))
    plt.plot(traj[:, 0], traj[:, 1], 'b-', linewidth=2)
    plt.scatter(traj[0, 0], traj[0, 1], color='green', s=80, label='Старт')
    plt.scatter(traj[-1, 0], traj[-1, 1], color='red', s=80, label='Финиш')    
    plt.xlabel('x (м)')
    plt.ylabel('y (м)')
    plt.title(title)
    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.axis('equal')
    plt.show()

def experiment():
    print("\nЭксперимент 3: Гравитация + упругость")
    print("-" * 40)
    body = PointMass(m=1.0, x=np.array([2.0, 1.0]), v=np.array([0, 0]))
    force = CombinedForce([
        Gravity(g=9.81),
        SpringForce(k=2.0, x0=np.array([0, 0]))
    ])
    sim = Simulator(body, force)
    sim.run(dt=0.01, total_time=8.0)
    traj = sim.get_trajectory()
    print(f"Начальное положение: {traj[0]}")
    print(f"Конечное положение: {traj[-1]}")
    plot_trajectory(sim, "Движение под действием гравитации и упругости")

if __name__ == "__main__":
    experiment()
