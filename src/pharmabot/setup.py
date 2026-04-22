from setuptools import setup

package_name = 'pharmabot'

setup(
    name=package_name,
    version='0.1',
    packages=[package_name],
    entry_points={
        'console_scripts': [
            'task_manager=pharmabot.task_manager:main',
            'scheduler=pharmabot.scheduler:main',
            'robot_nav=pharmabot.robot_nav:main',
            'watchdog=pharmabot.watchdog:main',
        ],
    },
)
