# XR + YOLO + VLA-Style Robotic Grasping Project Plan

## Project Positioning

Project title suggestion:

**XR-Driven Vision-Language-Action Robotic Grasping System**

Core portfolio narrative:

This project uses a Meta Quest 3 XR headset to collect human hand-tracking demonstrations, YOLO for real-time object perception, and a VLA-style learning pipeline to map visual observations, language/task intent, and XR hand-motion data into robotic grasping actions. Unity is used as the simulation and control environment, with IK-based robotic arm execution and real-time XR interaction.

Target resume bullets:

- Built Vision-Language-Action (VLA)-style models using XR hand-tracking data, improving robotic perception and multimodal learning.
- Integrated Meta Quest 3 XR hardware with Unity robotic platforms to achieve real-time hand-driven control and responsive IK-based robotic manipulation.

## Current Project Base

Already available:

- Unity robotic arm simulation.
- Meta Quest 3 XR headset integration.
- Hand tracking.
- Hand-motion data recording.
- YOLO object detection.
- Object position transmission into Unity.
- IK-based robotic arm grasping.

Goal:

Move from a rule-based XR/YOLO robotic demo to a data-driven robot-learning project that resembles an industrial VLA workflow.

## High-Level Architecture

```text
Meta Quest 3 XR Headset
  -> RGB / scene view
  -> hand tracking
  -> hand pose trajectory
  -> gesture / action phase

YOLO Perception
  -> object class
  -> bounding box
  -> confidence
  -> object center
  -> target object selection

Unity Robot Environment
  -> object world pose
  -> robotic arm joint states
  -> IK target
  -> gripper state
  -> success / failure label

VLA-Style Learning Layer
  -> vision features
  -> language/task instruction
  -> XR human action trajectory
  -> predicted robot action / grasp strategy

Robot Execution
  -> IK target update
  -> gripper open / close
  -> trajectory replay or learned action
  -> real-time feedback
```

## What "VLA" Means in This Project

A full industrial VLA model like RT-2, OpenVLA, or pi-zero is too large for a normal portfolio project. For this project, use a practical VLA-style system:

```text
Vision:
  YOLO object detection features.

Language:
  Simple task instruction text, such as:
  "pick up the red cube"
  "move the bottle to the tray"
  "grasp the nearest object"

Action:
  XR hand trajectory and robot IK/gripper commands.
```

The model does not need to be a giant foundation model. It can be a smaller multimodal policy that learns:

```text
(YOLO features + task instruction + hand trajectory context)
    -> robot action / grasp strategy / IK target correction
```

This is enough to truthfully describe the project as VLA-style multimodal robot learning.

## Phase 1: XR Demonstration Data Collection

Objective:

Turn Meta Quest 3 hand tracking into a useful robot-learning dataset.

Record one row or one sequence per demonstration:

```text
episode_id
timestamp
task_instruction
target_object_class
yolo_bbox_x
yolo_bbox_y
yolo_bbox_w
yolo_bbox_h
yolo_confidence
object_unity_x
object_unity_y
object_unity_z
left_hand_position
left_hand_rotation
right_hand_position
right_hand_rotation
pinch_strength
grip_state
wrist_velocity
hand_to_object_distance
action_phase
robot_ik_target_x
robot_ik_target_y
robot_ik_target_z
robot_gripper_state
success_label
```

Suggested `action_phase` labels:

```text
observe
reach
align
grasp
lift
place
release
fail
```

Implementation tasks:

- Add a Unity data logger for XR hand pose, YOLO output, object world pose, and robot state.
- Save data as CSV for tabular experiments and JSONL for sequence/VLA-style experiments.
- Record 30-50 demonstrations for a prototype, then 100-300 for a stronger portfolio result.
- Add success/failure labels after each grasp attempt.

Portfolio value:

Shows that the project is not only controlling a robot, but building a data flywheel.

## Phase 2: YOLO-Based Visual Perception

Objective:

Use YOLO as the current visual backbone and convert detections into robot-learning features.

YOLO output:

```text
class_id
class_name
confidence
bbox_center_x
bbox_center_y
bbox_width
bbox_height
normalized_area
```

Unity mapping:

```text
image-space bbox center
  -> Unity camera ray
  -> estimated object world position
  -> IK target candidate
```

Add perception features:

```text
is_target_detected
target_confidence
object_screen_distance_from_hand
object_world_distance_from_hand
object_reachability
object_size_estimate
```

Implementation tasks:

- Keep YOLO as the detector for now.
- Normalize all YOLO features before feeding them to ML models.
- Log detection confidence and missing-detection cases.
- Add a fallback behavior if YOLO fails: pause, rescan, or ask for manual XR pointing.

Portfolio value:

Makes YOLO part of a larger perception pipeline instead of a standalone detector.

## Phase 3: XR-to-Robot Action Retargeting

Objective:

Convert human hand movement into robot-action labels.

Basic retargeting:

```text
human hand position near object
  -> robot end-effector target pose

human pinch / grip gesture
  -> gripper close

hand release gesture
  -> gripper open
```

Action representation:

```text
delta_x
delta_y
delta_z
delta_rotation_yaw
gripper_command
stop_signal
```

This is close to how practical VLA systems represent robot action: small continuous end-effector deltas plus gripper state.

Implementation tasks:

- Convert XR hand pose into robot end-effector pose.
- Smooth noisy hand tracking with moving average or low-pass filter.
- Add workspace constraints so robot targets stay reachable.
- Record both raw human trajectory and retargeted robot trajectory.
- Add a replay mode: recorded human demo can drive the robot later.

Portfolio value:

Directly supports:

> Integrated XR hardware with robotic platforms to achieve real-time control and responsiveness.

## Phase 4: Baseline Rule-Based Controller

Objective:

Create a baseline for comparison before training models.

Baseline logic:

```text
if YOLO detects target and hand points/pinches:
    move IK target to object position
    close gripper
    lift object
else:
    wait / rescan
```

Metrics:

```text
grasp success rate
average time to grasp
number of failed IK targets
average object localization error
latency from hand motion to robot motion
```

Implementation tasks:

- Build a deterministic version first.
- Log every attempt.
- Use this as the benchmark for learned models.

Portfolio value:

Lets you say the learned layer improves over a rule-based baseline.

## Phase 5: Small VLA-Style Model

Objective:

Train a compact model that maps vision + language + XR action context to robot action.

Input:

```text
YOLO features:
  object class
  bbox center
  bbox size
  confidence
  object Unity position

Language features:
  task instruction
  target object name
  action verb

XR features:
  hand position
  hand velocity
  hand-object distance
  pinch / grip state
  recent trajectory window

Robot state:
  current end-effector pose
  gripper state
  IK reachability
```

Output option A: classification

```text
next_action:
  wait
  reach
  align
  grasp
  lift
  place
  release
```

Output option B: regression

```text
delta_ik_target_x
delta_ik_target_y
delta_ik_target_z
gripper_open_close
```

Recommended first model:

```text
RandomForestClassifier for action phase prediction
RandomForestRegressor for IK target correction
```

Recommended stronger model:

```text
Small PyTorch MLP or LSTM
Input: last N frames of YOLO + XR + robot state
Output: next robot action
```

Recommended portfolio wording:

> I implemented a lightweight VLA-style policy that conditions robot actions on visual object detections, natural-language task commands, and XR hand-tracking demonstrations.

Implementation tasks:

- Start with tabular ML using scikit-learn.
- Then add a sequence model if time allows.
- Compare rule-based control vs learned policy.
- Export predictions back into Unity through Python socket, REST, file polling, or Unity Barracuda/ONNX.

Portfolio value:

Directly supports:

> Built Vision-Language-Action (VLA) models using XR data, improving robotic perception and multimodal learning.

## Phase 6: Real-Time Unity Integration

Objective:

Make Unity use the learned policy in real time.

Runtime loop:

```text
Unity captures XR hand data
Unity receives YOLO detection
Unity sends current observation to model server
Model predicts next action
Unity updates IK target and gripper
Robot arm moves
Unity logs result
```

Suggested communication options:

```text
Option 1: Python Flask/FastAPI model server + Unity HTTP client
Option 2: Python WebSocket server + Unity WebSocket client
Option 3: ONNX export + Unity inference
Option 4: ROS 2 bridge if moving toward real robot platforms
```

Recommended for this project:

Use WebSocket or UDP for responsiveness. Use HTTP only for simpler prototype demos.

Measure:

```text
XR hand tracking FPS
YOLO inference latency
Unity-to-model latency
model inference latency
IK update latency
total end-to-end latency
```

Target:

```text
< 100 ms for responsive XR control
< 200 ms acceptable for portfolio demo
```

Portfolio value:

Gives concrete evidence for "real-time control and responsiveness."

## Phase 7: Multimodal Learning Evaluation

Objective:

Prove that combining XR + vision + language is better than using only one modality.

Run ablation experiments:

```text
Model A: YOLO features only
Model B: XR hand features only
Model C: YOLO + XR
Model D: YOLO + XR + language
```

Metrics:

```text
action prediction accuracy
grasp success prediction F1-score
IK target regression error
grasp success rate
average completion time
latency
```

Suggested plots:

```text
confusion matrix for action phase
feature importance chart
latency breakdown chart
success rate comparison
trajectory visualization
```

Tie-in with course knowledge:

- Decision trees for interpretable action prediction.
- Random forests for robust grasp success prediction.
- Cross-validation to avoid overfitting.
- Feature importance / permutation importance to explain whether YOLO, XR hand distance, or gripper state matters most.
- F1-score if success/failure classes are imbalanced.

Portfolio value:

This turns the project into a real machine learning project, not only a Unity interaction demo.

## Phase 8: Optional OpenVLA / Foundation Model Extension

Objective:

Add a research-facing extension without making the core project too risky.

Optional direction:

```text
Use OpenVLA / LeRobot / SmolVLA-style format as inspiration.
Convert your dataset into:
  observation image
  language instruction
  robot state
  action trajectory
```

Do not make this the main dependency unless the rest of the project is stable.

Deliverable:

```text
An exported dataset format compatible with future VLA fine-tuning.
```

Portfolio wording:

> Structured XR demonstration data into a VLA-compatible format for future fine-tuning of generalist robot policies.

## Final Demo Design

Demo scenario:

```text
User wears Meta Quest 3.
User says or selects: "Pick up the bottle."
YOLO detects objects in the Unity scene.
User demonstrates or points with tracked hand.
The learned policy predicts reach / grasp / lift actions.
Unity robotic arm executes IK movement.
System logs success and latency.
Dashboard shows YOLO detection, XR hand trajectory, predicted action, and robot execution.
```

Minimum final demo:

- YOLO detects object.
- Quest 3 hand tracking controls or demonstrates grasp.
- Dataset logger records multimodal data.
- Learned model predicts action phase or IK target correction.
- Unity robot uses prediction for IK execution.
- Evaluation chart compares baseline vs learned model.

Strong final demo:

- Natural-language command selects target object.
- VLA-style model predicts next robot action from YOLO + language + XR trajectory.
- Real-time model server controls Unity robot.
- Dashboard shows latency and success metrics.

## Suggested Timeline

### Week 1: Data Logging

- Build XR + YOLO + robot state logger.
- Save CSV/JSONL episodes.
- Add success/failure labels.

### Week 2: Baseline Controller

- Implement rule-based YOLO-to-IK grasping.
- Add XR hand gesture control.
- Measure latency and success rate.

### Week 3: ML Baselines

- Train action phase classifier.
- Train grasp success classifier.
- Train IK correction regressor.
- Add feature importance and validation metrics.

### Week 4: VLA-Style Integration

- Add language command encoding.
- Combine YOLO + XR + language features.
- Run ablation experiments.
- Connect model prediction back to Unity.

### Week 5: Real-Time Demo Polish

- Add WebSocket/UDP runtime loop.
- Add smoothing and safety constraints.
- Add visualization overlay.
- Record final demo video.

### Week 6: Portfolio Packaging

- Write README.
- Add architecture diagram.
- Add model evaluation charts.
- Add resume bullet proof points.
- Export demo clips and screenshots.

## Concrete Feature Checklist

- [ ] Meta Quest 3 hand-tracking data logger.
- [ ] YOLO detection logger.
- [ ] Unity object world-coordinate mapper.
- [ ] Robot IK target logger.
- [ ] Gripper state logger.
- [ ] Success/failure label UI.
- [ ] Rule-based baseline controller.
- [ ] XR hand-to-robot retargeting.
- [ ] Action phase classifier.
- [ ] Grasp success classifier.
- [ ] IK target correction regressor.
- [ ] Language command parser.
- [ ] VLA-style multimodal feature encoder.
- [ ] Real-time model server.
- [ ] Unity runtime inference integration.
- [ ] Latency measurement.
- [ ] Baseline vs learned model evaluation.
- [ ] Feature importance chart.
- [ ] Final project README and demo video.

## Recommended Technical Stack

Unity side:

```text
Unity
Meta XR SDK
XR Interaction Toolkit
C# data logger
Unity IK / Animation Rigging / custom IK
WebSocketSharp or native WebSocket client
```

Vision side:

```text
Python
Ultralytics YOLO
OpenCV
NumPy
```

ML side:

```text
scikit-learn
PyTorch
pandas
matplotlib / seaborn
ONNX optional
```

Runtime communication:

```text
WebSocket for real-time control
HTTP/FastAPI for simple prototype
UDP for very low-latency control signals
```

Future robotics side:

```text
ROS 2
MoveIt 2
ROS-Industrial
Isaac Sim / Isaac Lab
RealSense or ZED
```

## Best Portfolio Framing

Short version:

> Developed a Meta Quest 3 XR-driven robotic grasping system that records human hand demonstrations, detects objects with YOLO, and trains a VLA-style multimodal policy to control a Unity IK robotic arm in real time.

Technical version:

> Built a VLA-style robot learning pipeline using XR hand-tracking demonstrations, YOLO-based visual perception, task-language conditioning, and IK-based robotic control. Logged multimodal trajectories, trained action and grasp-success models, and integrated real-time inference into Unity for responsive robotic manipulation.

Resume bullets:

- Built a VLA-style multimodal policy using Meta Quest 3 XR hand-tracking data, YOLO object detections, and language-conditioned task labels to predict robotic grasp actions.
- Integrated XR hardware with a Unity IK robotic arm through real-time hand tracking, object perception, and low-latency model inference for responsive robot control.
- Collected and structured XR demonstration trajectories into a robot-learning dataset containing visual, language, hand-motion, and robot-state features.
- Evaluated rule-based versus learned grasping policies using success rate, F1-score, IK target error, and end-to-end latency.

## Key Principle

Do not claim that the project trains a full industrial-scale VLA foundation model unless you actually fine-tune one. The strongest honest framing is:

```text
VLA-style multimodal robot learning system
```

or:

```text
lightweight Vision-Language-Action policy trained from XR demonstrations
```

This is credible, technically strong, and still directly aligned with the two target requirements.
