# SLAM Mapping Lab — Student Handout

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![ROS2](https://img.shields.io/badge/ROS2-Humble-22314E?logo=ros&logoColor=white)
![Webots](https://img.shields.io/badge/Webots-2023+-6499E2?logoColor=white)
![SLAM Toolbox](https://img.shields.io/badge/SLAM-Toolbox-2E8B57)

**Static and Dynamic Environment Mapping** — SLAM with a virtual Unitree Go2.

> **Course:** 4th Year · Informatique (IA) · S7 · 3h30
> **Author:** [@sridath28](https://github.com/sridath28)
> **Reference solution:** published in a separate repository **after** the
> submission deadline, for self-study.

This repository contains the **provided testbed and tooling** for the SLAM
TP. Your instructor's LaTeX handout tells you **what to do**; this repo
gives you the **simulation world, SLAM config, RViz layout, launch files
and report template** so you can focus on mapping and analysis — not on
boilerplate.

> **Robot note:** the world ships with a Go2-like differential-drive body
> so it runs on any Webots install. To use the real Unitree Go2 / G1, see
> `docs/robot_swap_guide.md` (in the reference repo after the deadline) —
> the SLAM results do not change.

---

## Prerequisites (do this **before** the lab)

Ubuntu 22.04 + ROS2 Humble + Webots 2023a+:

```bash
sudo apt install ros-humble-slam-toolbox ros-humble-nav2-map-server \
                 ros-humble-teleop-twist-keyboard ros-humble-webots-ros2* \
                 ros-humble-turtlebot3*
pip install numpy matplotlib
```

Verify: `ros2 pkg list | grep slam_toolbox` returns `slam_toolbox`.

---

## Quick start

```bash
git clone https://github.com/sridath28/slam-mapping-tp-student.git
cd slam-mapping-tp-student

# terminal 1 — Webots + the Go2 driver
ros2 launch slam_mapping_tp go2_sim.launch.py

# terminal 2 — SLAM Toolbox + RViz
ros2 launch slam_mapping_tp slam_online_async.launch.py

# terminal 3 — drive the robot
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

RViz shows a gray map; as you drive, white (free) and black (occupied)
pixels appear. Follow the LaTeX handout step by step.

---

## What is provided vs. what you produce

### Provided in this repo

| Path | What it is |
|---|---|
| `worlds/lab_world.wbt` | Webots world — simulated lab (3 rooms) + Go2-like robot with LiDAR + camera |
| `config/slam_params.yaml` | SLAM Toolbox parameters (resolution, loop closure, scan range) |
| `config/slam_config.rviz` | RViz layout (Map + LaserScan + RobotModel + TF) |
| `launch/go2_sim.launch.py` | Launches Webots + the ROS2 bridge + the Go2 driver |
| `launch/slam_online_async.launch.py` | Launches SLAM Toolbox (async) + RViz |
| `docs/lab_report_template.md` | the report skeleton you fill in |

### You produce (graded)

| Step | You produce | How |
|---|---|---|
| Part A, Step 5 | `maps/lab_static.pgm` + `.yaml` | drive the robot, then `map_saver_cli -f maps/lab_static` |
| Part B, Step 1 | edit `worlds/lab_world.wbt` to add 2–3 moving obstacles | open in a text editor, add a walking person + a moving cart |
| Part B, Step 5 | `maps/lab_dynamic.pgm` + `.yaml` | re-run SLAM in the dynamic world, save the map |
| Part B, Step 6 | 1–2 page comparison report (PDF) | from `docs/lab_report_template.md` |

Submit per [`SUBMISSION.md`](SUBMISSION.md).

---

## Troubleshooting

| Symptom | Fix |
|---|---|
| Blank map in RViz | `/scan` not publishing or `use_sim_time` not set — check `ros2 topic hz /scan` and `slam_params.yaml` has `use_sim_time: true` |
| Map upside-down / rotated | set RViz **Fixed Frame** to `map` (the world uses `NUE`) |
| `map_saver_cli` writes nothing | run it from the repo root; `-f` paths are relative to the CWD |
| Phantom walls even in Part A | driving too fast (>0.5 m/s) — slow to ~0.2 m/s so the LiDAR keeps up |
| Loop closure never triggers | return within 0.5 m of your start pose |
| Go2 proto missing | swap in TurtleBot3 (see `docs/robot_swap_guide.md` in the reference repo) — SLAM results are identical |
| Moving obstacle doesn't move (Part B) | your obstacle needs a controller or a `SliderJoint`+`LinearMotor`; a static `Solid` won't move |

---

## Academic integrity

Group practical (see [`SUBMISSION.md`](SUBMISSION.md) for group size). You
may **discuss the concepts** with peers; you may **not** share maps, world
files, or report text between groups. A complete reference solution exists
in the instructor's repository and is published **after** the deadline —
copying it before submission is plagiarism and will be sanctioned per
HESTIM's academic integrity policy.

---

## License

MIT — see [`LICENSE`](LICENSE).

## Author

**sridath28** — <https://github.com/sridath28>

Issues and pull requests (e.g. fixes to the provided world/config) welcome.
