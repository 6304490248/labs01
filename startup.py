from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def home():
    return {"message": "Welcome Rakesh! Your FastAPI GET API is working 🎉H"}


@app.put("/insert/{id}")
def insert_student(id: int, student: Student):
    return {
        "message": "Student inserted",
        "id": id,
        "student": student
    }