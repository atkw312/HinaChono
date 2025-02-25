echo "Starting FastAPI backend..."
cd backend
uvicorn main:app --host 127.0.0.1 --port 8080 &

sleep 2

echo "Starting frontend server..."
cd ../frontend
serve -s . -l 5500 &

echo "Service is running. Open http://127.0.0.1:5500 in your browser."
wait