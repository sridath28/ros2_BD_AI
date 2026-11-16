# Submission — SLAM Mapping TP

## Group size

2–3 students per group. Register your group with the instructor **before**
starting Step 1.

---

## Deliverables

Submit **one ZIP per group**, named
`GROUP_<n>_<lastname1>_<lastname2>.zip`, containing:

| File | Produced in | Required |
|---|---|:---:|
| `maps/lab_static.pgm` + `lab_static.yaml` | Part A, Step 5 | ✅ |
| `maps/lab_dynamic.pgm` + `lab_dynamic.yaml` | Part B, Step 5 | ✅ |
| `worlds/lab_world.wbt` (your edited version with moving obstacles) | Part B, Step 1 | ✅ |
| RViz screenshots — static map | Part A, Step 6 | ✅ |
| RViz screenshots — dynamic map with phantom walls | Part B, Step 4 | ✅ |
| `lab_report.pdf` (1–2 pages, from `docs/lab_report_template.md`) | Part B, Step 6 | ✅ |

> The `.pgm`/`.yaml` pair must come from `ros2 run nav2_map_server
> map_saver_cli -f maps/lab_static` (and `lab_dynamic`) — not hand-drawn.

---

## Where to submit

【submission platform — e.g. Moodle / email / shared folder】 ← fill in before distributing

## Deadline

【date + time】 ← fill in before distributing

## Late policy

【instructor fills in】

---

## Grading (100 pts — matches the LaTeX handout)

| Criterion | Weight |
|---|:---:|
| Part A — static mapping + map quality | 40% |
| Part B — dynamic mapping + analysis | 40% |
| Report quality + map comparison | 20% |

A passing submission must show a **clean static map** (Part A) and a
**degraded dynamic map** with documented phantom walls (Part B) — that
contrast is the whole point of the lab.
