wd=$(pwd)

# ./CPU_usage.bash &
# ./Mem_usage.bash &

## Pip install the requirements for the API
pip3 install -r requirements.txt

## Run script, execute API in background
$wd/../bootstrap.bash &