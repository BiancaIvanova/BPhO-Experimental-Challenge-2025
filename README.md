# A One-Dimensional Model of the Gravitational Assist Slingshot Effect: An Experimental Study
Bianca Ivanova, Josh Parker, Edward Kim | Sutton Grammar School

_November 2024 - January 2025_

## Abstract

This project investigates the gravitational assist slingshot effect through a simplified one-dimensional model, focusing on energy transfer during collisions between a tennis ball (the "spaceship") and a football (the "planet"). Using a computer-aided tracking algorithm, we precisely measured the velocity and maximum rebound height of both objects during the experiment. A pneumatically-driven testing rig, equipped with adjustable tripods, ensured precise control of the drop height and minimized human error, and the tennis ball was 3D-printed to achieve a consistent weight and bounce. Experimental results showed that, as predicted by our theoretical model, the tennis ball rebounded to a height greater than its initial drop height, confirming the energy transfer predicted in the gravitational assist process. Our experimental results align with our theoretical model, validating the simplified theory used in this study.

## Table of Contents
- [Data](#data)
- [Experiment Setup](#experiment-setup)
- [Matlab Simulations](#matlab-simulations)
- [Image Processing](#image-processing)
- [Post Processing](#data-post-processing)
- [License](#license)

## Data

This repository contains the data used for analysis in the experiment. The raw data, along with other supporting materials, can be found in the following directories:

- **raw_drop_videos**: The original video recordings of all the drop tests.
- **experiment_photographs**: Photographs of the experimental setup and methods.
- **other_data**: Additional data files relevant to the experiment, including our experiment logbook, and final graph.
- **3D_design_models**: 3D models of the automated ball release mechanism, O-ring, and custom tennis ball.
- **image_processor**: Code and resources for the image recognition of the videos.
- **matlab_simulation**: Matlab scripts for simulating the theoretical model.
- **data_post_processor**: Code for post-processing and analysing the experimental data, using _numpy_, _panda_, and _matlplotlib_.

## Experiment Setup

The experimental setup includes:
- A pneumatically-driven testing rig to control the drop height.
- Adjustable tripods to hold the balls in place during testing.
- A computer-aided tracking algorithm for velocity and height measurements.
- A 3D-printed tennis ball to ensure consistency in weight and bounce.

The experiment aimed to replicate the gravitational assist slingshot effect by comparing the rebound height of the tennis ball after collisions with the football.

## MATLAB Simulations

Simulations were conducted in MATLAB to predict the behavior of the system. These simulations served as a comparison for experimental results, providing insight into the expected energy transfer and rebound heights for the tennis ball.

The Matlab scripts can be found in the `matlab_simulation` directory. To run the simulations, use the provided scripts that calculate rebound velocities and heights based on theoretical equations for gravitational assist.

## Image Processing

Image processing techniques were applied to extract the trajectory and rebound height data from the recorded videos. The `image_processor` directory contains code that automates this process.

## Data Post Processing

The post-processing code in the `data_post_processor` directory refines the collected experimental data and calculates the final values used for analysis. The post-processing scripts also perform statistical analysis, including fitting a trendline to the final data and calculating an R-squared value.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 Bianca Ivanova, Josh Parker, Edward Kim  
This work is the property of Bianca Ivanova, Josh Parker, and Edward Kim, of Sutton Grammar School.
