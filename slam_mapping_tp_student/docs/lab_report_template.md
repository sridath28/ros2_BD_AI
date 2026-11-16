# Lab Report Template — SLAM Mapping TP

**Student name(s):** ____________________________  **Group:** _______  **Date:** ___________

> Fill in each section. Submit this report **plus** the two map files
> (`lab_static.pgm` + `.yaml`, `lab_dynamic.pgm` + `.yaml`) and the RViz
> screenshots as a single PDF or ZIP. Length: 1–2 pages.

---

## 1. Setup (≈ ¼ page)

- Webots version: __________
- Robot used: ☐ Unitree Go2   ☐ Other: __________
- LiDAR scan rate (Hz): _____    Field of view (°): _____
- `/scan`, `/odom`, `/camera/image_raw` visible in `ros2 topic list`? ☐ Yes ☐ No

---

## 2. Part A — Static mapping  (≈ ½ page)

### 2.1 Teleop exploration
- Approx. area covered (% of accessible space): _____
- Time spent driving: _____ min
- Did the map update in real time? ☐ Yes ☐ No

### 2.2 Loop closure (Step 4)
Describe what happened when the robot returned to its start:

____________________________________________________________________

____________________________________________________________________

- Did the map visibly snap/improve? ☐ Yes ☐ No
- Any artifacts introduced by loop closure? ________________

### 2.3 Static map — quality check (Step 6)
| Check | Yes / No |
|---|---|
| All walls present and straight? | |
| Phantom walls in free space? | |
| Gray (unknown) gaps inside rooms? | |
| Resolution correct in YAML (~0.05 m/px)? | |

- Map quality score (1=poor, 5=excellent): _____
- Issues found + likely cause:

____________________________________________________________________

Paste the RViz screenshot of the static map below.

---

## 3. Part B — Dynamic mapping  (≈ ½ page)

### 3.1 Moving obstacles added
- Obstacle 1: __________  trajectory: __________
- Obstacle 2: __________  trajectory: __________

### 3.2 Observed degradation (Step 4)
| Observation | Answer |
|---|---|
| Where did phantom walls appear? | |
| Did SLAM recover when the obstacle moved away? | ☐ Yes ☐ Partial ☐ No |
| Did loop closure still work? | ☐ Yes ☐ No |
| Are there permanent artifacts in the final map? | ☐ Yes ☐ No |

Paste 1–2 RViz screenshots showing phantom walls.

### 3.3 Dynamic map — quality
- Map quality score (1–5): _____
- Permanent artifacts count: _____

---

## 4. Comparison & recommendations  (≈ ¼ page)

Open `lab_static.pgm` and `lab_dynamic.pgm` side by side.

- Which walls are correct in **both** maps? __________________

- Which areas have **phantom walls** in the dynamic map? __________________

- Impact on navigation (phantom wall = blocked path):
____________________________________________________________________

- One proposed fix for dynamic-environment SLAM (e.g. object tracking,
  temporal filtering, people detection, moving-object removal):
____________________________________________________________________

---

## Attachments checklist

- [ ] `lab_static.pgm` + `lab_static.yaml`
- [ ] `lab_dynamic.pgm` + `lab_dynamic.yaml`
- [ ] RViz screenshot(s) — static map
- [ ] RViz screenshot(s) — dynamic map with phantom walls
- [ ] This report (PDF)
