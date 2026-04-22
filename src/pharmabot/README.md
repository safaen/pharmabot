# 🏥 PharmaBot — Autonomous Hospital Robot (ROS2)

🚀 Simulation d’un robot autonome de pharmacie hospitalière utilisant ROS2, Nav2 et Gazebo.

---

## 🎯 Objectif

Développer un robot capable de :
- 📦 gérer des demandes de médicaments
- ⏱️ respecter des contraintes temps réel (Hard / Soft / Firm)
- 🤖 naviguer de manière autonome dans un environnement hospitalier
- 🚨 détecter les deadlines critiques

---

## 🧠 Architecture

Task Manager → Scheduler → Robot Navigation → Watchdog

- **Task Manager** : génère les tâches
- **Scheduler** : tri par priorité
- **RobotNav** : navigation via Nav2
- **Watchdog** : surveillance des deadlines

---

## 🏥 Simulation

- Gazebo (environnement hospitalier)
- RViz (visualisation navigation)
- TurtleBot3 (robot simulé)
- Nav2 (path planning)

---

## ▶️ Installation

```bash
git clone https://github.com/safaen/pharmabot.git
cd pharmabot
colcon build
source install/setup.bash
