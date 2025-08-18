# Overview

This project demonstrates a Learning to Rank (LTR) machine learning pipeline using a structured approach. 

The demo showcases the complete workflow from data ingestion to model deployment, organised in a modular fashion that would typically be used in production environments.

The project is designed to illustrate best practices for ML pipeline development, including:
- Modular code organisation with separate stages for data processing, model training, and deployment
- Input validation to ensure data quality
- Environment management with isolated requirements for each pipeline step
- MLOps configuration for automated workflow orchestration
- Clear separation between experimentation (notebooks) and production code (src)

That being said, the majority of this task was put in creation of the presentation. As there is limited time to curate a reasonable sample dataset and ML pipeline, **the demo code is only written and stored in python notebooks, and not in the individual python files in the src folder.**

The modelling is intentionally kept simple and does not look into topics like...

    - Pre-commit, CI/CD
    - Exception handling (esp. for model training failures)
    - Model versioning and monitoring
    - Scalability
Please let me know if there are certain topics you would like to discuss or see more evidence of.

# Model pipeline order
pull_data<br />
    ↓<br />
process_data<br />
    ↓<br />
train_model<br />
    ↓<br />
log_model           (not implemented)<br />
    ↓<br />
deploy_model        (not implemented)


# Folder Structure


    - data/                                 (Used to store outputs e.g. Ingested data. Exclude from commits.)
    - notebooks/                            (Experimentation/one-off scripts written in notebooks. Main code base for this example.)
        - scratch_pull_data.ipynb
        - scratch_process_data.ipynb
        - scratch_train_model.ipynb

    - requirements/                         (Requirements files)
        - actual_demo_requirements.txt      (A single requirement file to execute notebooks developed for the demo. Usually would setup one file per step.)
        - pull_data.txt                     (Empty)
        - process_data.txt                  (Empty)
        - train_model.txt                   (Empty)
        - log_model.txt                     (Empty)
        - deploy_model.txt                  (Empty)

    - src/                                  (Contains all python codes)               
        - utils/                            (Contains utility/helper functions)
            - utils.py                      
        - pull_data.py                      (Empty)
        - process_data.py                   (Empty)
        - train_model.py                    (Empty)
        - log_model.py                      (Empty)
        - deploy_model.py                   (Empty)

    - config.yaml                           (Contains model specification)
    - mlops.yaml                            (A mock MLOPs specification file based on Valohai)
    - README.md                             (This document)
    - .gitignore
