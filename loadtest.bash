old=$(date +"%T")

echo "Current Time: $old"

for i in {1..150}:
do
    curl http://127.0.0.1:5000/usage &
    echo "Executed"
done

now=$(date +"%T")
echo "Old time: $old --> Current Finished: $now"

