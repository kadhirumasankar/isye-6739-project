# isye-6739-project

Code for Kadhir Umasankar's "Coins in a Pot" simulation project for ISYE-6739 - Statistical Methods, taken at the Georgia Institute of Technology in the Fall of 2021.

## Running the code
If you have `conda` installed, run the following:

```bash
# This is my first time using conda to create and share an environment. Please email me at kadhir.umasankar@gatech.edu if there are any issues with this
conda env create --file=environment.yml
# This should create an environment named 'isye-6739-project'. Activate it by:
conda activate isye-6739-project
# Run the simulation:
python3 dice-game.py
```

## Uninstalling the environment

To uninstall the environment, run the following:

```bash
conda deactivate
conda env remove --name isye-6739-project
```