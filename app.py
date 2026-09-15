from fastapi import FastAPI,HTTPException

app=FastAPI(title="Train to grow")

studentlist=[
    {
        "id":20,
        "username":"Ambica"
    },
    {
            "id":21,
            "username":"ram"
    },
    {
            "id":22,
            "username":"pardhu"
    },
    {
            "id":23,
            "username":"pooja"
    }
]
@app.get("/")
async def index() -> str:
    return "Hello students -Train to Grow"

@app.get("/about")
async def about() ->dict:
    return {"company_name":"train to grow"}

@app.get("/students/{s_id}")
async def students(s_id:int):
    for info in studentlist:
        if info["id"]==s_id:
            return f"{info["username"]}"
    raise HTTPException(status_code=404,detail="Student not found")



