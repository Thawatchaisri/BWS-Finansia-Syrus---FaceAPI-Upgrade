# FSS Upgrade Plan

## Introduction
Finansia Syrus has a plan for maintaining the LMS. After the performance test process, they found the bottleneck modules of the system and they want to upgrade all of its modules for security and maintenance purposes.

My team was involved under Bangkok Web Solution to upgrade their old face API module with minimized change and was mostly cost-effective.

## Problem
The current face scan multifactor authentication module is slow and vulnerable to security attacks.

## Solution
Upgrade the face scan multifactor authentication model to a faster, pre-trained, and lightweight model.

## Changed
### New File
1. `FaceAPI\student\.gitignore`       Add ignore for protect PII
2. `FaceAPI\.gitignore`               Add ignore for protect "Config File"
3. `FaceAPI\login_check.py`           Update new login model
4. `FaceAPI\register_on_submit.py`    Refactor method "save file" to new file

### Update
1. `FaceAPI\server.py`                Update imports

### Removed
1. `FaceAPI\logindeepface_v1.py`      Remove deprecated model
2. `FaceAPI\logindeepface_v2.py`      Remove deprecated model
3. `FaceAPI\logindeepface_v4.py`      Remove deprecated model
4. `FaceAPI\out`                      Remove old log; protect leak
5. `FaceAPI\output.log`               Remove old log; protect leak
6. `FaceAPI\web.config`               Remove configuration file for protect leak